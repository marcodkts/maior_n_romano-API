from flask import Flask
from views.search import searchBluePrint

app = Flask(__name__)
app.register_blueprint(searchBluePrint)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True, port='8080')
