from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.update(
    MONGO_HOST='localhost',
    MONGO_PORT=27017,
    MONGO_USERNAME='bjhee',
    MONGO_PASSWORD='111111',
    MONGO_DBNAME='flask'
)

mongo = PyMongo(app)

# 指定mongoDB的服务器地址，端口，数据库名，用户账号密码
app.config.update(
    MONGO_URI='mongodb://localhost:27017/flask',
    MONGO_USERNAME='bjhee',
    MONGO_PASSWORD='111111'
)
user = {'name': 'Michael', 'age': 18,
        'scores': [{'course': 'Math', 'score': 76}]}
mongo.db.users.insert_one(user)
