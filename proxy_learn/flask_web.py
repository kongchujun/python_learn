from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, root!"

@app.route('/user/test/')
def hellos():
    return "Hello, this is the web Flask server response!"


if __name__ == '__main__':
    app.run(host='localhost', port=8888)
