import pymysql

class Database:
    def __init__(self,table_name=""):
        # self.database_name=database_name
        self.table_name=table_name
        # self.mysql_info=mysql_info
    #连接数据库
    def connect_database(self):
        conn = pymysql.connect(
            # host='localhost',
            host='localhost',
            user='root',
            password='123',
            database='film_database',
            charset='utf8'
        )
        return conn
    #获取表的列名
    def get_colomn_name(self,len):
        conn = self.connect_database()
        cursor = conn.cursor()
        sql=f"desc {self.table_name}"
        cursor.execute(sql)
        col=cursor.fetchall()
        col_name=[]
        for c in col[:len]:
            col_name.append(c[0])
        return col_name
    #功能
    #查询信息
    #删除信息
    #插入信息
    #更改信息
    #自定义mysql语句
    # 创建数据库表
    def select_info(self,info=""):
        conn=self.connect_database()
        cursor = conn.cursor()
        #获取整张表信息
        if(len(info)==0):
            select = f'select * from {self.table_name}'
            cursor.execute(select)
            user_info = cursor.fetchall()
            cursor.close()
            conn.close()
            return user_info

        else:
            #(["1235",["e3ufhgi]])
            # col=self.get_colomn_name(len(info))
            select=f'select * from {self.table_name} where '+info
            print(select)
            res=0
            try:
                res = cursor.execute(select)
            except:
                conn.rollback()  # 异常回滚
                print("无法查询到该信息！")
            if (res == 0):
                code=-1
            else:
                code=1
            cursor.close()
            conn.close()
            return code

    def delect_info(self,info):
        # 连接数据库，获取数据库中的用户账号，密码信息
        conn = self.connect_database()
        # 获得游标
        cursor = conn.cursor()
        delete=f"delete from {self.table_name} where "+info
        print(delete)
        code=1
        try:
            cursor.execute(delete)
            conn.commit()  # 数据表内容有更新，必须使用到该语句
            print("删除成功！")
        except:
            conn.rollback()  # 异常回滚
            code=-1
            print("删除失败！")
        cursor.close()
        conn.close()
        return code

    def insert_info(self,info):
        # 连接数据库，获取数据库中的用户账号，密码信息
        conn = self.connect_database()
        # 获得游标
        cursor = conn.cursor()
        # add = f'insert into {self.table_name} ' + info
        # print("add:", add)
        # cursor.execute(add)
        # cursor.close()
        # conn.close()
        try:
            add = f'insert into {self.table_name} '+info
            print("add:", add)
            cursor.execute(add)
            conn.commit()  # 提交事务执行
            cursor.close()
            conn.close()
            return 1
        except:
            error = -1
            conn.rollback()  # 异常回滚
            print("error")
            cursor.close()
            conn.close()
            return error

    def updata_info(self,info):
        # 连接数据库，获取数据库中的用户账号，密码信息
        conn = self.connect_database()
        # 获得游标
        cursor = conn.cursor()
        #UPDATE runoob_tbl SET runoob_title='学习 C++' WHERE runoob_id=3;
        update=f'update {self.table_name} '+info
        print(update)
        code=1
        try:
            cursor.execute(update)
            conn.commit()
            print("更改成功！")
        except:
            conn.rollback()  # 异常回滚
            code=1
            print("更改失败！")
        cursor.close()
        conn.close()
        return code

    def mysql(self,sql):
        # 连接数据库，获取数据库中的用户账号，密码信息
        conn = self.connect_database()
        # 获得游标
        code=1
        cursor = conn.cursor()
        # cursor.execute(sql)
        # conn.commit()
        try:
            cursor.execute(sql)
            conn.commit()
            print("成功！")
        except:
            conn.rollback()  # 异常回滚
            print("输入的语句出错！")
            print(sql)
            code=-1
        cursor.close()
        conn.close()
        return code

    def get_data(self,sql):
        # 连接数据库，获取数据库中的用户账号，密码信息
        conn = self.connect_database()
        # 获得游标
        data=""
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            data=cursor.fetchall()
            print("成功！")
        except:
            conn.rollback()  # 异常回滚
            print("输入的语句出错！")
        cursor.close()
        conn.close()
        return data


