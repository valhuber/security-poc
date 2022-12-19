from dotmap import DotMap
import sqlalchemy as sqlalchemy
import security.authentication_provider.sql.authentication_models as authentication_models
from flask import Flask
import safrs

# **********************
# db auth provider
# **********************

def get_user(name, password):
    """
    Must return a row object with attributes name and role_list
    role_list is a list of row objects with attribute name

    row object is a SQLAlchemy row (could have been a DotMap)
    """
    db = safrs.DB         # Use the safrs.DB, not db!
    session = db.session  # sqlalchemy.orm.scoping.scoped_session
    user = session.query(authentication_models.User).filter(authentication_models.User.id == name).one()
    # print(f'get_user: {user}')  # TODO many calls... cache?
    return user


