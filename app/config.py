import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Config:
    SECRET_KEY = ''
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:12345678@localhost/clinica'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    # TESTING = True
