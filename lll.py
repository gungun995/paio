import pymysql
from peewee import *
import json
import re


db = MySQLDatabase('ecang', host='210.45.215.210', port=7306, user='ecang', password='Pai0=Sp&Ec')
"""
db = MySQLDatabase('mysql', host='localhost', port=3306, user='root', password='123456')
"""


# 连接到MySQL数据库

# 定义新表的模型类
class NewTable(Model):

    name=CharField()
    id = CharField()
    time = CharField()
    execute_mode = CharField()
    advertising_group = CharField()
    number_of_advertising_products = CharField()
    asin = CharField()
    launch = CharField()
    matching_type = CharField()
    negative_release = CharField()
    operation_type = CharField()
    operation_record = CharField()
    operator = CharField()

    class Meta:
        database = db
        table_name = 'advertisment_info_log2'



NewTable.create_table()

# 查询旧表数据
with db.cursor() as cursor:
    cursor.execute("SELECT * FROM advertisment_info")
    for row in cursor:

        log = row[45]  #45

        log = log.replace("\"", "")

        log = log.replace("'", "\"")

        log=json.loads(log, strict=False)
        for i in range(len(log)):

            dict=log[i]
            new_data = {
                'name': row[2].strip(),  #2
                'id': dict.get('id', '').strip(),
                'time': dict.get('time', '').strip(),
                'execute_mode': dict.get('execute_mode', '').strip(),
                'advertising_group': dict.get('advertising_group', '').strip(),
                'number_of_advertising_products': dict.get('number_of_advertising_products', '').strip(),
                'asin': dict.get('asin', '').strip(),
                'launch': dict.get('launch', '').strip(),
                'matching_type': dict.get('matching_type', '').strip(),
                'negative_release': dict.get('negative_release', '').strip(),
                'operation_type': dict.get('operation_type', '').strip(),
                'operation_record': dict.get('operation_record', '').strip(),
                'operator': dict.get('operator', '').strip(),
            }
            NewTable.create(**new_data)

        """
        log=log.replace("[","")
        log = log.replace("]", "")
        log = log.replace("{", "")
        log = log.replace("}", "")


        log=log.split(",")

        for i in range(int(len(log)/12)):
            dict={}
            data =log[12*i:12*(i+1)]
            for j in range(12):
                da=re.sub(":",",",data[j],1,1)

                da=da.split(",")
                if len(da)==2:
                    dict[da[0].replace("'","").strip()]=da[1].replace("'","").strip()
                else:
                    dict['operator'] = str('').strip()
            """




db.close()


