from flask import Blueprint, request, jsonify
from .models import Result
from . import db
from .schemas import ResultSchema
from flasgger import swag_from

bp = Blueprint("routes", __name__)


@bp.route("/ping")
@swag_from({
    'responses': {
        200: {
            'description': 'Health check endpoint',
            'examples': {
                'application/json': {
                    'status': 'ok'
                }
            }
        }
    }
})
def ping():
    return jsonify({"status": "ok"}), 200


@bp.route("/submit", methods=["POST"])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string',
                        'example': 'Kirill'
                    },
                    'score': {
                        'type': 'integer',
                        'example': 88,
                        'minimum': 0,
                        'maximum': 100
                    }
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Result successfully saved',
            'examples': {
                'application/json': {
                    'message': 'Result saved'
                }
            }
        },
        400: {
            'description': 'Validation error',
            'examples': {
                'application/json': {
                    'error': 'Validation error message'
                }
            }
        }
    }
})
def submit():
    data = request.get_json()
    schema = ResultSchema()
    try:
        validated = schema.load(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    result = Result(name=validated["name"], score=validated["score"])
    db.session.add(result)
    db.session.commit()
    return jsonify({"message": "Result saved"}), 201


@bp.route("/results")
@swag_from({
    'parameters': [
        {
            'name': 'page',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'default': 1,
            'description': 'Page number'
        },
        {
            'name': 'per_page',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'default': 10,
            'description': 'Items per page'
        }
    ],
    'responses': {
        200: {
            'description': 'List of results',
            'examples': {
                'application/json': [
                    {
                        "id": 1,
                        "name": "AnyName",
                        "score": 10,
                        "timestamp": "2023-01-01T12:00:00"
                    }
                ]
            }
        }
    }
})
def results():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    results = Result.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )
    return jsonify([
        {
            "id": r.id,
            "name": r.name,
            "score": r.score,
            "timestamp": r.timestamp.isoformat()
        }
        for r in results.items
    ])
