from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] =  "mysql+pymysql://root:password@35.246.83.95:3306/flask_example_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'tangerines' 

db = SQLAlchemy(app)

from application import routes