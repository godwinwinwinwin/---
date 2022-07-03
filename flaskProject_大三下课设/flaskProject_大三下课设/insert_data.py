import pandas as pd
import Database as db
import analysis as an

def insert_film_data():
    del_sql = 'drop table if exists film'
    db.Database().mysql(del_sql)

    datas = pd.read_csv('new-2班-第5组-爬虫数据.csv', header=0, encoding="UTF-8")
    print(type(datas))

    # #创建mysql的数据库
    # """
    # create table dept(
    #     dept_id int primary key auto_increment,    --dept_id设置为int类型，自增字段，主键
    #     dept_name char(20) not null default '',    --dept_name不能为空，默认值为空字符串
    #     phone char(20)
    # );
    #
    # 查看表中的属性
    # desc tablename
    # """
    sql='create table film( \
         film_id int primary key,name varchar(100) not null,film_url varchar(100) not null,directors varchar(1000) not null,stars varchar(5000) not null,\
         language varchar(100) not null,nation varchar(100) not null,types varchar(100) not null,date varchar(100) not null,img_url varchar(500) not null,len_of_film varchar(100) not null,\
         score float not null,introduction varchar(1000) not null,comment_num int not null\
         )'
    db.Database().mysql(sql)
    for index, row in datas.iterrows():
        sql='insert into film values(\"%d\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%f\",\"%s\",\"%s\")'%(index,row["电影名称"],row["电影链接"],row["导演"]\
        ,row["主演"],row["语言"],row["制片国家/地区"],\
         row["类型"],row["首播"],row["图片链接"],row["片长"],row["豆瓣评分"],row["剧情简介"],row["短评数量"])
        # # print(sql)
        db.Database().mysql(sql)

def insert_hot_film():
    # 建热门电影的表
    # 先将原先的表删除
    del_sql = 'drop table if exists hot_film'
    # 再新建一个表
    db.Database().mysql(del_sql)
    sql = 'create table hot_film(film_id int not null,name varchar(100) not null,img_url varchar(100) not null, hot_value float not null)'
    db.Database().mysql(sql)
    hot_film = an.GetHotFilm()

    for data in hot_film:
        id = data[0]
        name = data[1]
        img_url = data[2]
        hot_value = data[3]
        # 插入id、电影名、图片链接、热播值
        sql = 'insert into hot_film values("%d","%s","%s", "%f")' % (id, name, img_url, hot_value)
        # print(sql)
        db.Database().mysql(sql)
#

insert_film_data()
# insert_hot_film()