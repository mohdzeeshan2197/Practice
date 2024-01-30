from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def test():
    return "<h1> Hello World</h1>"

@app.route("/first_function")
def test1():
    return "</h> This is My Test 1</h1>"

@app.route("/second_function")
def test2():
    return "</h>This is my Seccond Test Function</h1>"

@app.route("/third_function")
def test3():
    return "</h>This is my Third Function"

@app.route("/in_user")
def input_data():
    data = request.args.get("x")
    return "This is My Input From User {} Thanks You !".format(data)


if __name__ == '__main__':
    app.run(host= "0.0.0.0")