from flask import Flask, request
import json

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

@app.post("/api/products")
def save_products():
# will save a new product
    product = request.get_json()#this writes 
    print (product)

    products.append(product)
    return json.dumps(product)

app.run(debug=True) #this applies to changes on the code live