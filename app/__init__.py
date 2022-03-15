from flask import Flask
from config import Config
from app import models

app = Flask(__name__)
app.config.from_object(Config)

from app import routes


if __name__ == "__main__":
    app.run()
