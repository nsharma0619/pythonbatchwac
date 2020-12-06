from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
   return "<h1>hello this is a heading3</h1>"

@app.route('/welcome')
def welcome():
   return "<h1>Welcome to our websites</h1>"


app.run(debug=True)