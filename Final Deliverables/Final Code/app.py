from flask import Flask,request, render_template
from DB_OP import signupusersdb ,signinusersdb
import json


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/index')
def index():
    return render_template('index.html')




# API calls

@app.route('/signupusers',methods=['POST'])
def signupusers():
    value = signupusersdb(json.loads(request.get_data())['name'],json.loads(request.get_data())['email'],json.loads(request.get_data())['password'])
    # print(json.loads(request.get_data()))
    return value


@app.route('/signinusers',methods=['POST'])
def signinusers():
    value = signinusersdb(json.loads(request.get_data())['id'],json.loads(request.get_data())['password'])
    return value


if __name__ == '__main__':
    app.run(debug=True)
