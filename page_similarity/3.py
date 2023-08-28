import jellyfish
import numpy as np
from database import *
# 字符串与编码的字典
string_encoding_dict = {}
with db.cursor() as cursor:
    cursor.execute("SELECT * FROM page_info")
    for row in cursor:
        log1 = row[1] #记录asin
        log2 = row[8]  #45
        if log2:
            string_encoding_dict[log1] = log2

# string_encoding_dict = {
#      'Apple iPhone': 'B01LYEEZVH',
#     'Samsung Galaxy': 'B01LYACFS0',
#     'Apple MacBook Air': 'B00UGBMRKG',
#     'Dell XPS13': 'B00TXZDDAC'
# }

def get_top_3_similar(input_string):
    """
    输入一个字符串编码,返回相似度 top 3 的字符串编码
    """

    # 获取输入字符串对应的编码
    input_encoding = string_encoding_dict[input_string]

    # 计算输入编码与其他编码的相似度
    similarity_scores = []
    for encoding in string_encoding_dict.values():
        if encoding != input_encoding:
            # Jaccard相似度
            jac_sim = jellyfish.jaro_distance(input_encoding, encoding)
            similarity_scores.append(jac_sim)

    # 取相似度top 3的索引
    top_3_idx = np.argsort(similarity_scores)[-3:]

    # 获取top 3字符串
    top_3_strings = [list(string_encoding_dict.keys())[list(string_encoding_dict.values()).index(
        string_encoding_dict.values()[i])] for i in top_3_idx]

    return top_3_strings
# 输入字符串'Apple iPhone'的编码,获取top 3相似字符串
top_3 = get_top_3_similar('B09Z2LTXXK')
print(top_3)
# ['Apple MacBook Air', 'Dell XPS13', 'Samsung Galaxy']

