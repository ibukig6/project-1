from flask import Flask,render_template,request

app = Flask(__name__)

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
def email():
    email = request.args.get("email")
    password = request.args.get("password")
    return f"{email},{password}"
#http://127.0.0.1:5000/page?email=13&password=12

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ =="__main__":
    app.run(debug=True)