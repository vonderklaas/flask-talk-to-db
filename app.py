from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    
    connection_string = URL.create(
        drivername='postgresql',
        username='psql-db_owner',
        password='l1C0IkXSrKqz',
        host='ep-fragrant-glade-a2d997l1.eu-central-1.aws.neon.tech',
        database='psql-db',
        query={'sslmode': 'require'}
    )
    
    # Set the SQLALCHEMY_DATABASE_URI for Flask app
    app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, to suppress a warning
    
    # Initialize SQLAlchemy with the Flask app
    db.init_app(app)
    migrate = Migrate(app, db)

    from models import Person

    # avoid cicrular import
    from routes import register_routes
    register_routes(app, db)
    
    # Initialize Flask-Migrate with the Flask app and SQLAlchemy
    
    return app

# Example of creating the app and engine
# app = create_app()
# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
# print(engine)  # This will print the engine details
