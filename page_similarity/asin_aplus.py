import jellyfish
import numpy as np
from database1 import *
from collections import Counter

# 字符串与编码的字典
string_encoding_dict = {}
a = []
with db1.cursor() as cursor:
    cursor.execute("SELECT * FROM ods_amazon_page_page_info")
    for row in cursor:
        log1 = row[1]
        a.append(log1)
        string_encoding_dict[row[1]] = row


class asin_aplus(Model):
    ASIN = CharField()
    Aplus = CharField()
    recommend_Aplus = CharField()

    class Meta:
        database = db2
        db_table = "dwd_asin_aplus"


asin_aplus.create_table()

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

for asin in a:
    # 将原表中的aplus数据格式化为列表
    # aplus = page_info.select(page_info.aplus)
    self_aplus = page_info.select().where(page_info.product_asin == asin).get()
    # print(eval(self_aplus.aplus))

    # 输入字符串索引
    input_idx = list(string_encoding_dict.keys()).index(asin)

    # 排序相似度矩阵对应行,取最后5个索引
    top_5_idx = np.argsort(similarity_matrix[input_idx])[-5:]

    # 获取top 5字符串
    top_5 = [string_encoding_dict[a[i]] for i in top_5_idx[::-1]]  # i为索引

    b = []
    for row in top_5:
        aplus = row[11]
        aplus = aplus.replace("\\", "")  # 这里使用了\\转义为\
        aplus = eval(aplus)
        for i in aplus:
            b.append(i)
    # 修改过了 之前在循环内部 虽然最终效果一样，但重复了无效计算
    count = Counter(b)
    most_common = count.most_common(5)
    most_common = [i[0] for i in most_common]
    # 求出自身A+标签
    self_aplus = eval(self_aplus.aplus)
    # 页面已有的A+标签不用在推荐列表里面再显示一次
    most_common1 = []
    for i in most_common:
        if i not in self_aplus:
            most_common1.append(i)
    # 以下为错误操作
    # for i in most_common:
    #     if i in self_aplus:
    #         most_common.remove(i)
    # 存表
    object = asin_aplus(
        ASIN=asin, Aplus=str(self_aplus), recommend_Aplus=str(most_common1)
    )
    object.save()
