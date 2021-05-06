from flask import Flask 
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:root@34.105.238.207/todo_list_Database"

db =SQLAlchemy(app)

from application import routes