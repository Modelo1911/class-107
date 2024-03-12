from flask import Flask, request
import json
from config import db

app = Flask(__name__)# this is the name of my folder class-107

@app.get("/")
def home():
    return "Hello from flask"

@app.get("/testing")
def test():
    return "hello from a diffrent page" 

@app.get("/about")
def about():
    me = {"name": "Guillermo Escobar"}
    return json.dumps(me)

@app.get("/version")
def version():
    version = {"name": "mouse", "version": "2", "build": 12345}
    return json.dumps(version)

products = []
@app.get("/api/products")#this reads
def get_products():
    return json.dumps(products)

def fix_id(obj):
    obj["_id"]=str(obj["_id"])
    return obj


@app.post("/api/products")
def save_products():
# will save a new product
    product = request.get_json()#this writes 
    #print (product)

    #products.append(product) = this will push to the local storage 
    db.products.insert_one(product) # this will push into the online database

    return json.dumps(fix_id(product))

app.run(debug=True) #this applies changes on the code live