from flasgger import Swagger
from app import create_app

app = create_app()

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/"
}

Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "Lesta Fin API",
        "description": "API for managing results",
        "version": "1.0.0"
    },
    "consumes": [
        "application/json",
    ],
    "produces": [
        "application/json",
    ],
}, config=swagger_config)
