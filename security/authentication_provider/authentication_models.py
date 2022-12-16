# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://valhuber.github.io/ApiLogicServer/Project-Rebuild/#rebuilding

from safrs import SAFRSBase

import safrs
db = SQLAlchemy()
BaseSecurity = declarative_base()
metadata = BaseSecurity.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *
########################################################################################################################



class Role(SAFRSBase, BaseSecurity, db.Model, UserMixin):
    __tablename__ = 'Role'
    __bind_key__ = 'security_bind'


    id = Column(Integer, primary_key=True)
    name = Column(Text)

    UserRoleList = relationship('UserRole', cascade_backrefs=True, backref='role')


class User(SAFRSBase, BaseSecurity, db.Model, UserMixin):
    """ the user table """
    __tablename__ = 'User'
    __bind_key__ = 'security_bind'

    name = Column(Text)
    id = Column(Integer, primary_key=True)
    notes = Column(Text)

    UserRoleList = relationship('UserRole', cascade_backrefs=True, backref='user')


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


class UserRole(SAFRSBase, BaseSecurity, db.Model, UserMixin):
    __tablename__ = 'UserRole'
    __bind_key__ = 'security_bind'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    user_id = Column(ForeignKey('User.id'))
    role_id = Column(ForeignKey('Role.id'))
    notes = Column(Text)

    # see backref on parent: role = relationship('Role', cascade_backrefs=True, backref='UserRoleList')
    # see backref on parent: user = relationship('User', cascade_backrefs=True, backref='UserRoleList')
