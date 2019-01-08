# encoding:utf-8
from flask import Flask

# 创建实例 实例化对象

app = Flask(__name__)


# 启动实例

# 视图函数
@app.route('/')
def index():
    return '<h2>hehehe这个</h2>'


@app.route('/admin/')
def admin():
    return '<h2>后台管理</h2>'


@app.route('/welcome/<name>')
def welcome(name):
    return '<h2>hellow %s</h2>' % name


@app.route('/classes/<int:uid>')
def classes(uid):
    return '<h2>hellow %d</h2>' % uid


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5055, host='0.0.0.0')  # 0.0.0.0说明所有其他主机都可以访问
