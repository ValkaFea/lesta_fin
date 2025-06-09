from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import bp
    app.register_blueprint(bp)

    from flasgger import Swagger
    Swagger(app, template={
        "swagger": "2.0",
        "info": {
            "title": "Lesta API",
            "description": "API Documentation",
            "version": "1.0"
        },
        "basePath": "/",
        "schemes": ["http"]
    })

    return app
