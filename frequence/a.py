from peewee import *
db = MySQLDatabase('amazon', host='210.45.215.210', port=7306, user='amazon', password='Pai0=Sp&Am')

class Aplus(Model):
   id=AutoField()
   """id=IntegerField(primary_key=True)'"""
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
      database=db
      db_table='page_info'