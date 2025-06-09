from marshmallow import Schema, fields, validate
import os
from dotenv import load_dotenv


class ResultSchema(Schema):
    name = fields.String(required=True)
    score = fields.Integer(
        required=True,
        validate=validate.Range(min=0, max=100))


load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
