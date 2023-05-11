from flask import Flask,render_template,request,g
import sqlite3 as sql                          #↑
#from flask import g----------------------------↑在這上面，一種省略寫法
DATABASE = 'database.db'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_python():
    return "<p>Hello, python!</p>"

@app.route("/name/<name>")
def name(name):
    print('Type:',type(name))
    return name

@app.route("/number/<int:number>")
def number(number):
    print('Type:',type(number))
    return f"{number}"

@app.route("/page")
def page():
    x="1234"
    dict1 = {"abc":1324,"name":"tom"}
    return render_template("page.html",a=x,b=dict1)
#def email():
#    email = request.args.get("email")
#    password = request.args.get("password")
#    return f"{email},{password}"
#http://127.0.0.1:5000/page?email=13&password=12

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        name =request.form.get("account")
        password=request.form.get("password")
        if name == "123" and password =="123":
            type ="成功"
            return render_template("page2.html",id=name,ps=password,type=type)
        else:
            type="登入失敗"
            return render_template("login.html",type=type)
    else:
        return render_template("login.html")

@app.route("/users")
def users():
    with get_db() as cur: #with get_db().cursor() as cur:
        cur.row_factory = sql.Row
        cur = cur.cursor() #上面的註解可以把這行省略
        cur.execute("select * from Users")
        data = cur.fetchall()
        cur.close()
    return render_template("users.html",data = data)


if __name__ =="__main__":
    app.run(debug=True)