'''FlaskApp'''
from flask import Flask, render_template, request

app = Flask(__name__)

'''
Endpoint /
'''
@app.route('/')
def hello_world():
    '''Endpoint'''
    return 'Hello, World!'
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    '''Endpoint'''
    if request.method == 'GET':
        return render_template('hello.html')
    if request.method == 'POST':
        name = request.form['name']
        return f'hello, {name}!'
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()
