from database1 import *

# a = []
# with db1.cursor() as cursor:
#     cursor.execute("SELECT * FROM ods_amazon_page_page_info")
#     for row in cursor:
#         log1 = row[0]
#         a.append(log1)

# self_aplus = Page.select().where(Page.product_asin == "B07CQMZ15D").get() 与下行代码输出一样，只是不同的写法，这种更复杂
self_aplus = Page.get(Page.product_asin == "B07CQMZ15D")
print(eval(self_aplus.aplus))
