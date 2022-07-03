import Database as da
import pymysql
import pandas as pd
#查询数据
con=da.Database("user_info")

update='set password=245637 where user=12346'
con.updata_info(update)
# resdata=res.select_info()
# info='user=1234567902'
# select=res.select_info(info)
# info=dict()
# insert='values(123456,3haiuf)'
# primary='123456'
# info["data"]=insert
# info["primary"]=primary
# resdata=res.insert_info(info)

# res.delect_info('user=1234567')


# for r in resdata:
#     print(r)
#
#
# res=da.Database("user_info")
# resdata=res.select_info()

# conn = pymysql.connect(
#     # host='localhost',
#     host='localhost',
#     user='root',
#     password='',
#     database='film_database',
#     charset='utf8'
# )
#
# cursor=conn.cursor()
# #查看列名即属性
# #DESC name_of_the_table;
# sql="desc user_info"
# cursor.execute(sql)
# # col=cursor.description
# # print(col)
# res=cursor.fetchall()