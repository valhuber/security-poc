# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://valhuber.github.io/ApiLogicServer/Project-Rebuild/#rebuilding

from safrs import SAFRSBase

import safrs

Base = declarative_base()
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *
########################################################################################################################



class Role(SAFRSBase, Base):
    __tablename__ = 'Role'

    id = Column(Integer, primary_key=True)
    name = Column(Text)

    UserRoleList = relationship('UserRole', cascade_backrefs=True, backref='role')


class User(SAFRSBase, Base):
    __tablename__ = 'User'

    name = Column(Text)
    id = Column(Integer, primary_key=True)
    notes = Column(Text)

    UserRoleList = relationship('UserRole', cascade_backrefs=True, backref='user')


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


class UserRole(SAFRSBase, Base):
    __tablename__ = 'UserRole'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('User.id'))
    role_id = Column(ForeignKey('Role.id'))
    notes = Column(Text)

    # see backref on parent: role = relationship('Role', cascade_backrefs=True, backref='UserRoleList')
    # see backref on parent: user = relationship('User', cascade_backrefs=True, backref='UserRoleList')
