from database1 import *

# a = []
# with db1.cursor() as cursor:
#     cursor.execute("SELECT * FROM ods_amazon_page_page_info")
#     for row in cursor:
#         log1 = row[0]
#         a.append(log1)

self_aplus = page_info.select().where(page_info.product_asin == "B07CQMZ15D").get()
print(eval(self_aplus.aplus))
