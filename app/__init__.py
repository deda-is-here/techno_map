from flask import Flask
from config import Config
from app import models
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
data_base = SQLAlchemy(app)
migrate = Migrate(app, data_base)

from app import routes, models


if __name__ == "__main__":
    app.run()
