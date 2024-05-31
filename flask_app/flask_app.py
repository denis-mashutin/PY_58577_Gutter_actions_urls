from flask import Flask
from router import router

app = Flask(__name__)
app.register_blueprint(router, url_prefix='prefix1/')


@app.route('flask_app/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world():
    return 'Hello, World!'


@app.get('flask_app/get')
def get():
    pass


if __name__ == '__main__':
    app.run()
