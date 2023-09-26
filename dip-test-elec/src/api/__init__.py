from flask_sqlalchemy import SQLAlchemy
from flask import Flask
#from flask_cors import CORS

DB_NAME = "TEST__DB"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}.db'

db = SQLAlchemy(app)