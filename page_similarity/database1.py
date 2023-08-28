from peewee import *
db1 = MySQLDatabase('paio-ods', host='210.45.215.210', port=6400, user='paio', password='C@$=[2023]&t!(p@!0)')
db2 = MySQLDatabase('paio-stage', host='210.45.215.210', port=6400, user='paio', password='C@$=[2023]&t!(p@!0)')

class page_info(Model):
   id=AutoField()
   # id=IntegerField(primary_key=True)
   product_asin=CharField()
   title=CharField()
   base_info=CharField()
   feature = CharField()
   price = CharField()
   technical_details=CharField()
   addition_details=CharField()
   rank=CharField()
   reviews_star = CharField()
   fearure_scores = CharField()
   aplus = CharField()
   all_reviews = CharField()
   positive_reviews = TextField()
   critical_reviews = TextField()
   product_problems = TextField()
   comptition_asin = CharField()
   sponsored_asin = CharField()
   date = DateField()
   version=CharField()
   class Meta:
      database=db1
      db_table='ods_amazon_page_page_info'