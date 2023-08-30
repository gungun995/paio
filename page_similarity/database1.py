from peewee import *

db1 = MySQLDatabase(
    "paio-ods",
    host="210.45.215.210",
    port=6400,
    user="paio",
    password="C@$=[2023]&t!(p@!0)",
)
db2 = MySQLDatabase(
    "paio-stage",
    host="210.45.215.210",
    port=6400,
    user="paio",
    password="C@$=[2023]&t!(p@!0)",
)


class page_info(Model):
    id = AutoField()
    # id=IntegerField(primary_key=True)
    product_asin = CharField()
    title = CharField()
    base_info = CharField()
    feature = CharField()
    price = CharField()
    technical_details = CharField()
    addition_details = CharField()
    rank = CharField()
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
    version = CharField()

    class Meta:
        database = db1
        db_table = "ods_amazon_page_page_info"


class Page(Model):
    """id=IntegerField(primary_key=True)'"""

    product_asin = CharField(collation="utf8mb4_unicode_ci")
    country_code = CharField(collation="utf8mb4_unicode_ci")
    title = CharField(collation="utf8mb4_unicode_ci")
    base_info = TextField()
    feature = TextField()
    price = CharField(collation="utf8mb4_unicode_ci")
    technical_details = TextField()
    addition_details = TextField()
    rank = CharField(collation="utf8mb4_unicode_ci")
    reviews_star = CharField(collation="utf8mb4_unicode_ci")
    fearure_scores = CharField(collation="utf8mb4_unicode_ci")
    aplus = TextField()
    all_reviews = TextField()
    positive_reviews = TextField()
    critical_reviews = TextField()
    product_problems = TextField()
    comptition_asin = TextField()
    sponsored_asin = TextField()
    date = DateField()
    version = CharField()

    class Meta:
        database = db1
        db_table = "ods_amazon_page_product_info"
        primary_key = CompositeKey("product_asin", "country_code", "date")
        collation = "utf8mb4_unicode_ci"
