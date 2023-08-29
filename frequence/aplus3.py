from page_similarity.database1 import *


class aplus(Model):
    name = CharField()

    class Meta:
        database = db2
        db_table = "aplus"


aplus.create_table()
with db2.cursor() as cursor:
    cursor.execute("SELECT recommend_Aplus FROM dwd_asin_aplus")
    for log in cursor:
        # log = log.replace("[", "")
        # log = log.replace("]", "")
        # log = log.replace('"', "")
        log = eval(log[0])
        for i in log:
            object = aplus(name=i)
            object.save()
        # print(log)
