import Database as db

#数据分析

#获取豆瓣top250
def get_top250():
    con=db.Database("film")
    sql='select * from film  order by score desc limit 15;'
    data=con.get_data(sql)
    #d[11]豆瓣评分,9图片
    return data



#获取最近上映的电影


#获取hot_film（热播电影）
def get_hot_film():
    table = "hot_film"
    db.Database(table)
    get_hot_film_sql = 'select * from hot_film order by hot_value DESC '
    data = db.Database().get_data(get_hot_film_sql)
    name_imgUrl = []
    for row in data:
        temp = []
        # print(row[0])
        temp.append(row[0])
        temp.append(row[1])
        temp.append(row[2])
        name_imgUrl.append(temp)

    return name_imgUrl[:15] # 返回的是列表,其中元素也为列表
    # 例如[,'天才计划', 'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2873885713.jpg']

get_hot_film()


#获取各种类型的电影
