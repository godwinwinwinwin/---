import Database as db
import datetime

# 处理热门电影
def GetHotFilm():
    temp = db.Database("film")
    data = temp.select_info()
    today = str(datetime.date.today()).split('-')
    today_year = int(today[0])
    today_month = int(today[1])
    li = []

    for row in data:
        if row[8] == 'NONE':
            continue
        elif len(row[8]) == 4:
            # 获取id
            temp = []
            id = row[0]
            temp.append(id)
            # 获取短评数量
            short_comment = row[13]
            # 获取名字
            name = row[1]
            temp.append(name)
            # 获取图片连接
            src = row[9]
            temp.append(src)
            # 获取时间
            year = int(row[8])
            score = (int(short_comment) + 1) / ((int(year) - int(today_year)) * 12 + 1) ** 1.5
            temp.append(score)

        else:
            # 获取id
            temp = []
            id = row[0]
            temp.append(id)
            # 获取短评数量
            short_comment = row[13]
            # 获取名字
            name = row[1]
            temp.append(name)
            # 获取图片连接
            src = row[9]
            temp.append(src)
            # 获取时间
            date = row[8].split('-')
            year = date[0]
            month = date[1]
            score = (int(short_comment) + 1) / (((int(year) - int(today_year)) * 12 + (int(month) - int(today_month))) ** 2 + 1)
            temp.append(score)
        if len(temp) != 0:
            li.append(temp)
    return li