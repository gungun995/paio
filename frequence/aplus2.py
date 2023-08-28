from a import *

class aplus2(Model):

   name=CharField()

   class Meta:
      database=db
      db_table='aplus2'

aplus2.create_table()
with db.cursor() as cursor:
    cursor.execute("SELECT * FROM comptition_page_info LIMIT 1000")
    for row in cursor:

        log = row[13]  #45
        # log = log.replace("[", "")
        # log = log.replace("]", "")
        # log = log.replace('"', "")
        log = eval(log)
        for i in log:
            object = aplus2(
                name = i
            )
            object.save()
        # print(log)
