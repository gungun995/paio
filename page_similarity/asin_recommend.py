from flask import Flask, jsonify
import jellyfish
import numpy as np
from database import *

# 字符串与编码的字典
string_encoding_dict = {}
a = []
with db.cursor() as cursor:
    cursor.execute("SELECT * FROM page_info")
    for row in cursor:
        log1 = row[1]
        a.append(log1)
        string_encoding_dict[row[1]] = row

app = Flask(__name__)

@app.route("/api/get_top_3_similar/<asin>", methods=["GET"])
def get_top_3_similar(asin):
    """
    输入一个字符串编码,返回相似度 top 3 的字符串编码
    """
    # 计算相似度矩阵
    similarity_matrix = []
    for string1, row1 in string_encoding_dict.items():
        row = []
        for string2, row2 in string_encoding_dict.items():
            # 计算Jaccard相似度
            if string1 != string2:
                if row1[8] and row2[8]:
                    jac_sim = jellyfish.jaro_similarity(row1[8], row2[8])
                    row.append(jac_sim)
                else:
                    jac_sim = 0
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
    top_3 = [string_encoding_dict[a[i]] for i in top_3_idx[::-1]]  # i为索引

    top_3_results = []
    for row in top_3:
        sub_result = {
            "asin": row[1],
            "title": row[2],
            "rank": row[8],
            "review_stars": row[9],
            "aplus": row[11],
        }
        top_3_results.append(sub_result)

    results = {"top_3_similar": top_3_results}
    # results = {
    #     "top_3_similar": [row[1] for row in top_3],
    #     "title": [row[2] for row in top_3],
    #     "rank": [row[8] for row in top_3],
    #     "review_stars": [row[9] for row in top_3],
    #     "aplus": [row[11] for row in top_3],
    #     # 其余字段同样返回
    # }
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
