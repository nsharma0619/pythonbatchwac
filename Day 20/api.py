from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/getresult')
def home():
    dictionary = {
        "name" : "saloi",
        "frndname" : ["neeraj", "janvi"],
        "study" : "iit"
    }
    return dictionary


app.run(debug=True)