from marshmallow import Schema, fields, validate

class ResultSchema(Schema):
    name = fields.String(required=True)
    score = fields.Integer(required=True, validate=validate.Range(min=0, max=100))


# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False