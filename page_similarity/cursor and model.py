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


self_aplus = string_encoding_dict['B07B9WW6R2']
print(self_aplus)

# 所得为元组，因此只能使用aplus1 = self_aplus[11]这种，而不能countrycode = self_aplus.country_code