from flask import Flask
from db import db
import pymysql
from blueprint import auth, home
from models import User, HundredThings
import time



app = Flask(__name__)
app.debug = True
app.register_blueprint(auth.bp)
app.register_blueprint(home.home)

# 配置数据库
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://mingminglove:mingminglove@175.178.187.98:3306/mingminglove"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
pymysql.install_as_MySQLdb()
# db.create_all()
db.init_app(app)




@app.route('/')
def hello_world():
    ts = time.time()
    ts = str(ts)
    hundred = HundredThings()
    hundred.id = ts
    hundred.username = 'admin'
    hundred.thing = '一起吃饭'
    hundred.done = 1
    db.session.add(hundred)
    db.session.commit()
    return 'Hello World!'



if __name__ == '__main__':
    app.run()
