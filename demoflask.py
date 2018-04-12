# *_* coding:utf-8 *_*
from flask import Flask, redirect, flash
from flask import render_template

from forms import LoginForm

app = Flask(__name__)
app.config.from_object("config")


# 默认展示
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index')
def index():
    user = {"nickname": "zhxin"}
    posts = [{
        "author": {"nickname": "John"},
        "body": "beautiful day in Portland"
        }, {
        "author": {"nickname": "Ajax"},
        "body": "beautiful day in aruili"
        }]
    return render_template("index.html",
                           title = "Home",
                           user = user,
                           posts = posts)


# 跳转到登录页面
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    # 验证通过
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect("/index")
    return render_template("login.html", title = "Sign in", form = form, providers = app.config['OPENID_PROVIDERS'])


if __name__ == '__main__':
    app.run()
