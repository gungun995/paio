import jellyfish
import numpy as np
from database1 import *
from collections import Counter

# 字符串与编码的字典
string_encoding_dict = {}
a = []
with db1.cursor() as cursor:
    cursor.execute("SELECT * FROM ods_amazon_page_product_info")
    for row in cursor:
        key = row[0]
        a.append(key)
        string_encoding_dict[key] = row


class asin_aplus(Model):
    ASIN = CharField()
    country_code = CharField()
    Aplus = CharField()
    recommend_Aplus = CharField()

    class Meta:
        primary_key = CompositeKey('ASIN', 'country_code')
        database = db2
        db_table = "dwd_asin_aplus"


asin_aplus.create_table()

# 计算相似度矩阵
similarity_matrix = []
for asin1, page1 in string_encoding_dict.items():
    row = []
    for asin2, page2 in string_encoding_dict.items():
        # 计算Jaccard相似度
        if asin1 != asin2:
            if page1[8] and page2[8]:
                jac_sim = jellyfish.jaro_similarity(page1[8], page2[8])
                row.append(jac_sim)
            else:
                jac_sim = 0
                row.append(jac_sim)
        else:
            jac_sim = 0
            row.append(jac_sim)
    similarity_matrix.append(row)

for asin in a:
    self_aplus = Page.get(Page.product_asin == asin) #这种写法应该就是使用model类里面的方法了，对应的可以使用countrycode = self_aplus.country_code这种形式获取列
    # self_aplus = Page.select().where(Page.product_asin == asin).get() 这种写法也行 但看上去好笨 也可简化为
    # self_aplus = string_encoding_dict[asin]  这种写法是cursor提供的，要用的话是这样：aplus1 = self_aplus[11]
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
        # aplus = aplus.replace("\\", "")  # 这里使用了\\转义为\
        aplus = eval(aplus)
        for i in aplus:
            b.append(i)
    # 修改过了 之前在循环内部 虽然最终效果一样，但重复了无效计算
    count = Counter(b)
    most_common = count.most_common(5)
    most_common = [i[0] for i in most_common]
    # 求出自身A+标签和国别信息
    aplus1 = eval(self_aplus.aplus)
    countrycode = self_aplus.country_code
    # 页面已有的A+标签不用在推荐列表里面再显示一次
    most_common1 = []
    for i in most_common:
        if i not in aplus1:
            most_common1.append(i)
    # 以下为错误操作
    # for i in most_common:
    #     if i in self_aplus:
    #         most_common.remove(i)
    # 存表
    object = asin_aplus(
        ASIN=asin, country_code=countrycode, Aplus=str(aplus1), recommend_Aplus=str(most_common1)
    )
    try:
        object.save(force_insert=True)
    except IntegrityError :
        object.save()
