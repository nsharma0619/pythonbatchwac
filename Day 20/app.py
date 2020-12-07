from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
   return render_template("index.html")

@app.route('/welcome')
def welcome():
   return render_template("welcome.html")

@app.route('/dummy')
def dummy():
   user_name = "janvi"
   msg = "hello janvi this is your 19th python class."
   friends_list = ['Neeraj', 'janvi', 'shakya', 'vidhi', 'pari']
   return render_template("dummy.html", user_name=user_name, msg=msg, friends_list=friends_list)


@app.route('/variable/<productId>')
def variable(productId):
   return productId


@app.route('/redirectme')
def redirectme():
   return redirect(url_for('dummy'))

app.run(debug=True, port=8000)

# CRUD = c-create post
# r-read  get
# # u-update put
# d-delete delete

