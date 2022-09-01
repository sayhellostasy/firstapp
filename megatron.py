from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return """<html><body>

        <h1>Это очень важный заголовок страницы</h1>

        <h2><a href="/firstPage/">Это заголовок поменьше, но тоже важный</a></h2>

        </body></html>"""


@app.route('/firstPage/')
def firstPage():
    return """<html><body>

        <h1>Приветствую тебя, разработчик! </h1>

        <h2><a href="/"><= обратно</a></h3>

        </body></html>"""


if __name__ == '__main__':
    app.run()