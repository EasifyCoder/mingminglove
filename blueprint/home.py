from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from blueprint import auth
from models import HundredThings, DaysMatter
import json
import time
from db import db
import datetime


home = Blueprint('home', __name__, url_prefix='/api/home')

@home.route('/getHundredThings', methods=['GET', 'POST'])
def hundredthings():
    token = request.headers.get("Authorization")
    verified = auth.verify_token(token)

    # 如果verified为True，则表明token合法
    if verified:
        username = auth.get_username_from_token(token)
        # 根据用户名获取其所有行的信息
        HundredThingsList = HundredThings.query.filter(HundredThings.username == username).all()

        # 返回字典result，result中有code状态码和data字典，data中有两个list，分别是已经做完的事情done和未做完的事情undone
        result = {}
        data = {}
        done = []
        undone = []
        for i in HundredThingsList:
            if i.done == 1:
                print(i.username)
                done.append(i.thing)
            else:
                undone.append(i.thing)
        data['done'] = done
        data['undone'] = undone

        result['code'] = 200
        result['data'] = data
        print(result)
        return result
    else:
        return ""

# 获取DaysMatters数据接口
@home.route('/getDaysMatters', methods=['GET', 'POST'])
def DaysMatters():
    token = request.headers.get("Authorization")
    verified = auth.verify_token(token)

    # 如果verified为True，则表明token合法
    if verified:
        username = auth.get_username_from_token(token)
        # 根据用户名获取其所有行的信息
        DaysMattersList = DaysMatter.query.filter(DaysMatter.username == username).all()

        # 返回字典result，result中有code状态码和data字典，data中有两个list，分别是已经做完的事情done和未做完的事情undone
        result = {}
        data = {}
        dataList = []
        for i in DaysMattersList:
            data['description'] = i.description
            date = i.date.strftime('%Y-%m-%d') # 转换成规范的格式
            data['date'] = date
            # 计算时间天数
            today = datetime.date.today()
            diff = (today - i.date).days # 时间天数的差
            data['days'] = diff

            dataList.append(data)


        result['code'] = 200
        result['data'] = dataList
        print(result)
        return result
    else:
        return ""

@home.route('/submitThing', methods=['GET', 'POST'])
def submitThing():
    token = request.headers.get("Authorization")
    verified = auth.verify_token(token)

    # 如果verified为True，则表明token合法
    if verified:
        username = auth.get_username_from_token(token)
        data = json.loads(request.data)  # 将json字符串转为dict字典
        thing = data["name"]
        done = data["done"]
        ts = time.time()
        ts = str(ts)
        hundred = HundredThings()
        hundred.id = ts
        hundred.username = username
        hundred.thing = thing
        hundred.done = done
        db.session.add(hundred)
        db.session.commit()
    return {'code': 200}

















