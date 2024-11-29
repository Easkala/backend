from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def init_db(app):
    """Initialize the database with Flask app."""
    app.config.from_object("config.Config")  # Load configurations
    db.init_app(app)                         # Bind SQLAlchemy to app
    Migrate(app, db)                         # Enable migrations
