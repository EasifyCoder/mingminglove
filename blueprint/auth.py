from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import json
from models import User
import jwt
key = "secret"


bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    data = json.loads(request.data)  # 将json字符串转为dict字典
    username = data["username"]
    password = data["password"]
    # 从数据库查询，根据username进行查询
    user_info = User.query.filter(User.username==username).first()
    # 如果用户名和密码匹配，则返回token和200状态码
    if user_info and password == user_info.password:
        token_info = {
            "username": username,
            "password": password
        }
        # 对用户信息进行编码，生成token。用户信息中要包括用户名和密码
        code = 200
        encoded_token = jwt.encode(token_info, key, algorithm="HS256")
    else:
        code = 401
        encoded_token = None


    result = {
        "code": code,
        "token": encoded_token
    }
    return result

# 用于验证token是否合法
def verify_token(token, key=key):
    decoded = jwt.decode(token, key, algorithms="HS256")
    username = decoded["username"]
    password = decoded["password"]
    # 判断用户名和密码是否存在，是否匹配
    # 从数据库查询，根据username进行查询
    user_info = User.query.filter(User.username == username).first()
    # 如果用户名存在，且和密码匹配，则返回True
    if user_info and password == user_info.password:
        return True
    else:
        return False

# 从token中获取用户名
def get_username_from_token(token):
    decoded = jwt.decode(token, key, algorithms="HS256")
    username = decoded["username"]
    return username