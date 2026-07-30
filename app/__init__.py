# Flask application instance
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config) 
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models
# Imported at bottom to avoid circular imports, a common problem with Flask Applications. - we will see that the routes module needs to import the app variable defined in the script, so putting one of the reciprocal imports at the bottom avoids the error that results from the mutial references between these two files.