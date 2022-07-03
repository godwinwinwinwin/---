# coding=utf-8
from flask import Flask, jsonify, render_template
from flask import request
# from flask_sqlalchemy import SQLAlchemy
import pymysql as ps
import Database as db
import get_data
import pymysql
app = Flask(__name__)  # flask框架必备


"""
host=self.mysql_info['host'],
user=self.mysql_info['user'],
password=self.mysql_info['password'],
database=self.mysql_info['database'],
"""

# #连接数据库
# def connect_database():
#     conn = ps.connect(
#         # host='localhost',
#         host='39.106.25.93',
#         user='root',
#         password='123456',
#         database='student',
#         charset='utf8'
#     )
#     return conn

# #向数据库中查询信息
# def search_table_info(table):
#     # 获得游标
#     # conn = connect_database()
#     # cursor = conn.cursor()
#     select = f'select * from {table}'
#     cursor.execute(select)
#     user_info = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return user_info

# #向数据库中添加用户信息
# def add_info(table,info):
#     # 连接数据库，获取数据库中的用户账号，密码信息
#     conn = connect_database()
#     # 获得游标
#     cursor = conn.cursor()
#     try:
#         add = f'insert into {table} values({info["user"]},"{info["password"]}",NOW())'
#         print("add:",add)
#         cursor.execute(add)
#         conn.commit()  # 提交事务执行
#         cursor.close()
#         conn.close()
#         return 1
#     except:
#         error=-1
#         conn.rollback()  # 异常回滚
#         #判断该用户是否已经存在
#         judge_exists=f'select Id from {table} where Id={info["user"]}'
#         #若返回的是1则该用户已经存在，否者就是插入的信息错误！
#         status=cursor.execute(judge_exists)
#         if(status==0):
#             error=-2
#         cursor.close()
#         conn.close()
#         return error

#榜单页面
# @app.route('/list_movie')
# def list_movie():
#     return render_template('list.html')
#
# # 各种类型电影的页面
# @app.route('/movieTyes')
# def movietypes():
#     return render_template("movie.html")
#
# #注册页面
# # @app.route('/register')
# # def register():
# #     return render_template('register.html')
# #
# # #登入页面
# # @app.route('/login')
# # def login():
# #     return render_template('login.html')
# #
# # #主页
# # @app.route('/')
# # def index():
# #     #获取top250
# #     top250 = get_data.get_top250()
# #     #获取热播电影
# #     hot_movie=get_data.get_hot_film()
# #     data = dict()
# #     data["top250"] = top250
# #     data["hot_movie"]=hot_movie
# #     print(type(request.headers["Cookie"]))
# #     cookie=request.headers["Cookie"]
# #     print(cookie)
# #     cookie=cookie.split(";")
# #     if(len(cookie)>1):
# #         username = cookie[1].split("=")[1]
# #         data["login_status"] = "已登入"
# #         if(username=="null"):
# #             data["login_status"] = "游客"
# #         return render_template('index.html',**data)
# #     data["login_status"]="游客"
# #     return render_template('index.html',**data)
#
# #电影详情页面
# @app.route('/details/<index>')
# def details(index):
#     print(int(index))
#     sql=f'select * from film where film_id={int(index)}'
#     con=db.Database('film')
#     data=con.get_data(sql)
#     return render_template('detailsPage.html',**{"data":data[0]})
#
# #各人中心页面
# @app.route('/user_mid')
# def user_mid():
#     data=dict()
#     print(type(request.headers["Cookie"]))
#     cookie = request.headers["Cookie"]
#     print(cookie)
#     cookie = cookie.split(";")
#     #根据cookie中的用户信息渲染页面
#     if (len(cookie) > 1):
#         data["login_status"] = "已登入"
#         return render_template('user_mid.html')
#     data["login_status"] = "游客"
#     return render_template('user_mid.html')
#
# #将用户注册信息写入数据库中
# @app.route('/register_To_database',methods=["POST","GET"])
# def register_To_database():
#     user_info=dict()
#     code = 1
#     info = "注册成功！"
#     print('-----------')
#     if request.method == "POST":
#         if (request.form["user_id"] != "" and request.form["user_password"] != "" and request.form["user_name"]):
#             user_info['user_id']=request.form["user_name"]
#             # print("user_type:",type( user_info['user']))
#             user_info['user_password']=request.form["user_password"]
#             user_info['user_name'] = request.form['user_name']
#             user_info['user_info'] = '这个人很懒，没什么可说的...'
#             #YYYY-MM-DD HH:mm:ss
#             print(user_info)
#             #根据返回的状态判断是否注册成功
#             # res_status=add_info('students',user_info)
#             isExist_sql = 'create table if not exists user(user_id varchar(10) not null, user_password varchar(10) not null, user_name varchar(20) not null, user_info varchar(100))'
#             db.Database.mysql(isExist_sql)
#             con = db.Database('user')
#             info1="values('%s','%s', '%s', '%s')"%(user_info['user_id'],user_info['user_password'], user_info['user_name'], user_info['user_info'])
#             res_status=con.insert_info(info1)
#             print("status:",res_status)
#             if(res_status==1):
#                 res = {
#                     "code": code,
#                     "info": info
#                 }
#                 return res
#             else:
#                 con=db.Database('user_info')
#                 info1=f"user={user_info['user']}"
#                 sign=con.select_info(info1)
#                 if(sign==1):
#                     info = '该账号已经存在！'
#                     code=-1
#         res = {
#             "code": code,
#             "info": info
#         }
#         return res;
#
# #密码验证
# @app.route('/user_authentication',methods=["POST","GET"])
# def user_authentication():
#     #连接数据库，获取数据库中的用户账号，密码信息
#     # user_info=search_table_info('students')
#     # print('user_info:',user_info)
#     code = 1
#     info = "登入成功！"
#     #出错情况
#     error=-1
#     print(type(request.form["name"]))
#     if request.method == "POST":
#         con=db.Database('user')
#         #判断用户是否有输入用户和密码
#         if (request.form["name"] != "" and request.form["password"] != ""):
#             info = f"user={request.form['name']} and password={request.form['password']}"
#             res = con.select_info(info)
#             print()
#             if (res != 1):
#                 code = -1
#                 info = "账号或者密码错误！"
#         else:
#             if (request.form["name"] == "" and request.form["password"] != ""):
#                 code = -1
#                 info = "输入的账号不能为空"
#             elif (request.form["name"] != "" and request.form["password"] == ""):
#                 code = -1
#                 info = "输入的密码不能为空！"
#             else:
#                 code = -1
#                 info = "输入的密码和账号不能为空"
#         res={
#             "code":code,
#             "info":info
#         }
#         return res
#
#
# # 获取数据(首页电影数据)
# #获取热播数据
# #获取top250电影数据
# #获取最近电影数据
# # @app.route('/get_filmdata',methods=["POST","GET"])
# # def get_filmdata():
# #     if request.method=="POST":
# #         # 获取top250
# #         re_data = get_data.get_top250()
# #         data = dict()
# #         data["top250"] = re_data
# #         return data
#
# #榜单数据
# @app.route('/get_list_data',methods=["POST","GET"])
# def get_list_data():
#     if request.method == "POST":
#         #热播口碑榜
#         #猜你喜欢榜
#         #豆瓣TOP250
#         data = dict()
#         print(request.form["type"])
#         if(request.form["type"]=="热映口碑榜"):
#             #获取热播电影榜
#             re_data = get_data.get_top250()
#             print(re_data)
#             data["data"] = re_data
#         elif(request.form["type"]=="猜你喜欢榜"):
#             #
#             print("------------")
#         else:
#             print("else")
#             re_data = get_data.get_top250()
#             print(re_data)
#             data = dict()
#             data["data"] = re_data
#         return data

# 数据分析
@app.route('/')
def get_analysis_data():
    sql = 'select name, score from film order by score DESC limit 5'
    info = db.Database().get_data(sql)
    data = []
    k = 1
    for i in info:
        # name = '"' + i[0] + '"'
        data.append(i[0])
        data.append(i[1])
    print(data)
    return render_template('analysis.html', **{"data":data})


if __name__ == '__main__':
    app.run(debug=True) # flask框架必备