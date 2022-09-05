from asyncio import tasks
from csv import unregister_dialect
from datetime import date, datetime
import email
from email.policy import default
from enum import unique
from telnetlib import STATUS
from xml.sax.handler import feature_namespace_prefixes
from . import db

from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id              = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.String(5) )
    fname           = db.Column(db.String(150) )
    lname           = db.Column(db.String(150) )
    email           = db.Column(db.String(150), unique=True)
    password        = db.Column(db.String(150) )
    avatar          = db.Column(db.String(200) )
    tasks           = db.relationship('Task')


class Task(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    task_name       = db.Column(db.String(200))
    description     = db.Column(db.String(350) )
    created_by      = db.Column(db.String(150) )
    priority        = db.Column(db.String(15))
    status          = db.Column(db.String(15))
    date_created    = db.Column(db.DateTime, default=datetime.utcnow)
    user_id         = db.Column(db.Integer, db.ForeignKey('user.id'))


