from flask import Flask
app = Flask(__name__)

@app.route('/')
def hellow_world():
    return "Hello WWWWorld"

if __name__ == '__main__':
    app.run(debug = True)

