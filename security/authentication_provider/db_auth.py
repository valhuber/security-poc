from dotmap import DotMap
import sqlalchemy as sqlalchemy
import security.authentication_provider.models as models
from flask import Flask
import safrs

# **********************
# db auth provider TODO
# **********************

users = DotMap()

def get_user(name):
    """
    Must return a row object with attributes name and role_list
    role_list is a list of row objects with attribute name

    row object is a SQLAlchemy row (could have been a DotMap)
    """

    def flask_db_read_all_users(config_filename=None, host="localhost"):
        """ 
        there has *got* to be a better way of doing this 

        within a running flask app, we want to open the AdminDB (not userdb) and read 1 (or all) users
        """
        app = Flask("demo_app")
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///" + 'authentication-db.sqlite',
                        SESSION_COOKIE_SAMESITE="Lax",  # <<--- Strict
                        SQLALCHEMY_BINDS={'admin': "sqlite:///" + 'authentication-db.sqlite'},
                        SECRET_KEY="Change me !!",
                        SQLALCHEMY_TRACK_MODIFICATIONS=False,
                        FLASK_DEBUG=True)
        db = safrs.DB
        db.init_app(app)
        with app.app_context():
            # user = db.session.query(models.User).filter(models.User.name == name).one()
            db_users = db.session.query(models.User).all()
            for each_user in db_users:
                users[each_user.name] = each_user
        return

    if not users:
        host = "localhost"
        port = 5656
        flask_db_read_all_users(host=host)
    user = users[name]
    return user


