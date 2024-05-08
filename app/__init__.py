import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask.cli import FlaskGroup
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}?client_encoding=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

cli = FlaskGroup(app)

from app.controllers import default

if __name__ == "__main__":
    cli()
