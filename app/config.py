import os
import uuid


class Config:
    SECRET_KEY = str(uuid.uuid4())
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI',
                                             'sqlite:///employees.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False