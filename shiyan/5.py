import jellyfish
import numpy as np
# 字符串与编码的字典
string_encoding_dict = {
     'Apple iPhone': 'B01LYEEZVH',
    'Samsung Galaxy': 'B01LYACFS0',
    'Apple MacBook Air': 'B00UGBMRKG',
    'Dell XPS13': 'B00TXZDDAC'
}


def get_top_3_similar(input_string):
    """
    输入一个字符串编码,返回相似度 top 3 的字符串编码
    """
    # 相似度矩阵
    similarity_matrix = []

    for string1, encoding1 in string_encoding_dict.items():
        row = []
        for string2, encoding2 in string_encoding_dict.items():
            # 计算Jaccard相似度
            jac_sim = jellyfish.jaro_similarity(string1, string2)
            row.append(jac_sim)
        similarity_matrix.append(row)

        # 输入字符串索引
    input_idx = list(string_encoding_dict.keys()).index(input_string)

    # 排序相似度矩阵对应行,取最后3个索引
    top_3_idx = np.argsort(similarity_matrix[input_idx])[-3:]

    # 获得top 3 字符串编码
    top_3_encoding = [list(string_encoding_dict.values())[i] for i in top_3_idx[::-1]]

    return top_3_encoding

# 输入字符串'Apple iPhone'的编码,获取top 3相似字符串
top_3 = get_top_3_similar('Apple iPhone')
print(top_3)
# ['Apple MacBook Air', 'Dell XPS13', 'Samsung Galaxy']

# 输入字符串'Dell XPS13'的编码,获取top 3相似字符串
# top_3 = get_top_3_similar('B00TXZDDAC')
# print(top_3)
# ['Apple MacBook Air', 'Apple iPhone', 'Samsung Galaxy']