import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask.cli import FlaskGroup
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:/Users/1241304057/AppData/Roaming/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

cli = FlaskGroup(app)

from app.controllers import default

if __name__ == "__main__":
    cli()
