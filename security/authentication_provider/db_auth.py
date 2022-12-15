from dotmap import DotMap
import sqlalchemy as sqlalchemy
import security.authentication_provider.models as models
from flask import Flask
import safrs

# **********************
# db auth provider TODO
# **********************

def get_user(name):
    """
    Must return a row object with attributes name and role_list
    role_list is a list of row objects with attribute name

    row object is a SQLAlchemy row (could have been a DotMap)
    """
    db = safrs.DB         # Use the safrs.DB, not db!
    session = db.session  # sqlalchemy.orm.scoping.scoped_session
    user = session.query(models.User).filter(models.User.name == name).one()  # fails, no such table
    print(f'get_user: {user}')

    return user


