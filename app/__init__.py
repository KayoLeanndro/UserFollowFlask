import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask.cli import FlaskGroup
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

cli = FlaskGroup(app)

from app.controllers import default

if __name__ == "__main__":
    cli()
