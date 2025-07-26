from flask import Flask
from extensions import db, login_manager
import os
from models import User, Project

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_manager.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

from routes import *  # This attaches @app.route decorators to the created app

if __name__ == '__main__':
    app.run(debug=True)
