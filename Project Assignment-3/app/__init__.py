from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "fcee2c3c8bdd600b2d083bacc18da6ee" 

from app import routes
