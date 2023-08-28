from a import *

class aplus1(Model):

   name=CharField()

   class Meta:
      database=db
      db_table='aplus1'

aplus1.create_table()
with db.cursor() as cursor:
    cursor.execute("SELECT * FROM page_info")
    for row in cursor:

        log = row[11]  #45
        # log = log.replace("[", "")
        # log = log.replace("]", "")
        # log = log.replace('"', "")
        log = eval(log)
        for i in log:
            object = aplus1(
                name = i
            )
            object.save()
        # print(log)
