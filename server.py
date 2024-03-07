from flask import Flask

app = Flask(__name__)# this is the name of my folder class-107

@app.get("/")
def home():
    return "Hello from flask"

app.run(debug=True) #this applies to changes on the code live