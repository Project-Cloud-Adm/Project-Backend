from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/Hello", methods = ["GET", "POST"])
def hello_name():
    if request.method == "POST":
        name = request.form ["name"]
        return "Hello {}".format(name)
    else:
        return '''
        <form method = "post">
            <label for = "name">Enter your name: </label>
            <input type= "text" id = "name" name = "name">
            <input type = "submit" value = "Submit">
        </form>
    '''

if __name__ == "__main__":
    app.run()
