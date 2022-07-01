from flask import Flask, render_template, request,redirect,url_for
import pymongo
from datetime import datetime
import string
import random
import json
import socket
app = Flask(__name__)
data = {}

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/typeNote",methods=["POST"])
def typeNote():
    note= request.form['note'] 
    # randomURL = randomLink()
    # notes.insert_one({"id":randomURL,"text":note,"inserted_time":datetime.today(),"destroyed":False})
    return render_template("createUrl.html",note=note)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
