from flask import Flask, render_template, request,redirect,url_for
import pymongo
from datetime import datetime
import string
import random
import json
import socket
app = Flask(__name__)
data = {}
def random_func():
    letters = string.ascii_lowercase
    link=''.join(random.choice(letters) for i in range(10)) 
    return link
try:
        with open("config.json", "r") as config:
            data = json.load(config)
            print(data)
except:

    data['expiretime']= 10
    data['port'] = 8000
    data['DBusername'] = "mina412"
    data['DBpassword'] = "minaahmadi77"
    data['DBurl'] = "@project.itbja.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient("mongodb+srv://"+data['DBusername']+":"+data['DBpassword']+data['DBurl'])

db = client['database']

notes= db['notes']

@app.route("/")
def index():
    return render_template("home_page.html")


@app.route("/typeNote",methods=["POST"])
def typeNote():
    note= request.form['note'] 
    url = random_func()
    notes.insert_one({"id":url,"time":datetime.today(),"note":note,"available":True})
    return render_template("createUrl.html",note="127.0.0.1:5000/notePage/"+url,url=url)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
