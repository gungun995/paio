from flask import Flask, jsonify
import jellyfish
import numpy as np
from database import *
from collections import Counter

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


@app.route('/api/get_top_3_similar/<asin>', methods=['GET'])
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

    # 排序相似度矩阵对应行,取最后5个索引
    top_5_idx = np.argsort(similarity_matrix[input_idx])[-5:]

    # 获取top 3字符串
    top_5 = [string_encoding_dict[a[i]] for i in top_5_idx[::-1]]       # i为索引

    b = []
    for row in top_5:
        aplus = row[11]
        aplus = aplus.replace("\\", '')    # 这里使用了\\转义为\
        aplus = eval(aplus)
        for i in aplus:
            b.append(i)
    # 修改过了 之前在循环内部 虽然最终效果一样，但重复了无效计算
    count = Counter(b)
    most_common = count.most_common(5)
    most_common = [i[0] for i in most_common]



    # results = {
    #     "top_3_similar": b
    # }

    return most_common


if __name__ == '__main__':
    app.run(debug=True)