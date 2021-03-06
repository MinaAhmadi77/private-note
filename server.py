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

    data['minutes_to_expire']= 5
    data['port'] = 8000
    data['user'] = "mina412"
    data['pass'] = "minaahmadi77"
    data['url'] = "@project.itbja.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient("mongodb+srv://"+data['user']+":"+data['pass']+data['url'])

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
    return render_template("createUrl.html",note="127.0.0.1:5000/warningPage/"+url,url=url)
    
@app.route("/warningPage/<id>",methods=["GET"])
def warningPage(id):

    note = notes.find_one({"id":id})
    if(note['available']) == True:
        spend = (datetime.now() - note['time']).total_seconds()
        if (spend > data['minutes_to_expire'] * 60):
            notes.update_one({"id":id},{ "$set": { 'available': False } })
            return "not available"
        return render_template("warning_page.html", id = id)
    else:
        return "not available"
@app.route("/showNotePage",methods=["POST"])
def showNotePage():
    id = request.form['btn']
    notes.update_one({"id":id},{ "$set": { 'available': False } })
    print("id", id)
    return render_template("show_note_page.html", text = notes.find_one({"id":id})['note'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
