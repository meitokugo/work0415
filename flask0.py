# coding=utf-8
# 实现了post方法插入json数据到数据库中，使用get方法查询数据库里的数据
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)
# 路由URL规则


@app.route('/add/', methods=['POST'])
# 数据库操作
def add_student():
    # 链接到info.db数据库
    # 打开数据库API，创建一个cursor,接受一个单一的可选参数cursorClass
    conn = sqlite3.connect('info.db')
    #
    cur = conn.cursor()
    student1 = {
        'id': request.json['id'],
        'name': request.json['name'],
        'age': request.json['age']
    }
# 插入
    sql = 'insert into student values(%s,%s,%s)' % (
        student1['id'], student1['name'], student1['age'])

    cur.execute(sql)
    conn.commit()
    print(sql)
    conn.close()
    return u"done!"

# 查询


@app.route('/<int:id>/', methods=['GET'])
# 将字典转换成json数据格式return json.dumps(t.ensure_ascii = False)
# 使用json.dumps转换的在前端显示数据JSON字符串
# json.load字符串转换成字典
# 使用flask的jsonify转换后，前台显示为json对象
def query(id):
    conn = sqlite3.connect('info.db')
    # 返回数据库游标，用于操作数据库
    cur = conn.cursor()
    sql = "select id,name,age from student where id=" + str(id)
    # 执行sql语句，insert update delete
    cur.execute(sql)
    #
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

# 响应错误。


@app.errorhandler(404)
def page_not_found(e):
    res = jsonify({'error': 'not found'})
    res.status_code = 404
    return res


if __name__ == '__main__':
    app.run(debug=True)
