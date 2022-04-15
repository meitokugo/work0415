# coding=utf-8
# 实现了post方法插入json数据到数据库中，使用get方法查询数据库里的数据
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/add/', methods=['POST'])
def add_student():
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()
    student1 = {
        'id': request.json['id'],
        'name': request.json['name'],
        'age': request.json['age']
    }

    sql = 'insert into student values(%s,%s,%s)' % (
        student1['id'], student1['name'], student1['age'])

    cur.execute(sql)
    conn.commit()
    print(sql)
    conn.close()
    return u"done!"


@app.route('/<int:id>/', methods=['GET'])
def query(id):
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()
    sql = "select id,name,age from student where id=" + str(id)
    cur.execute(sql)
    result = cur.fetchall()
    print(sql)
    conn.close()
    return jsonify(
        {
            'id': result[0][0],
            'name': result[0][1],
            'age': result[0][2]
        }
    )


@app.errorhandler(404)
def page_not_found(e):
    res = jsonify({'error': 'not found'})
    res.status_code = 404
    return res


if __name__ == '__main__':
    app.run(debug=True)
