from flask import Flask, jsonify
import jellyfish
import numpy as np
from database import *

# 字符串与编码的字典
string_encoding_dict = {}
with db.cursor() as cursor:
    cursor.execute("SELECT * FROM page_info")
    for row in cursor:
        log1 = row[1]  # 记录asin
        log2 = row[8]  # 45
        if log2:
            string_encoding_dict[log1] = log2

app = Flask(__name__)


@app.route('/api/get_top_3_similar/<asin>', methods=['GET'])
def get_top_3_similar(asin):
    """
    输入一个字符串编码,返回相似度 top 3 的字符串编码
    """
    # 计算相似度矩阵
    similarity_matrix = []
    for string1, encoding1 in string_encoding_dict.items():
        row = []
        for string2, encoding2 in string_encoding_dict.items():
            # 计算Jaccard相似度
            if string1 != string2:
                jac_sim = jellyfish.jaro_similarity(encoding1, encoding2)
                row.append(jac_sim)
            else:
                jac_sim = 0
                row.append(jac_sim)
        similarity_matrix.append(row)

    # 输入字符串索引
    input_idx = list(string_encoding_dict.keys()).index(asin)

    # 排序相似度矩阵对应行,取最后3个索引
    top_3_idx = np.argsort(similarity_matrix[input_idx])[-3:]

    # 获取top 3字符串
    top_3 = [list(string_encoding_dict.keys())[i] for i in top_3_idx[::-1]]

    results = {
        "top_3_similar": top_3
    }
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)