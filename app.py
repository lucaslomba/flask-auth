from flask import Flask
from models.user import User
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "Your secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)
