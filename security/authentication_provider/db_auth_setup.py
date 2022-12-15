import sqlalchemy as sqlalchemy
import models as models
from flask import Flask
import safrs

def create_app(config_filename=None, host="localhost"):
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
        # db.create_all()
        # db.create_all(bind='admin')
        # create_admin_api(app, port=port, host=host)
        sam = models.User(name='Sam')
        db.session.add(sam)
        db.session.commit()

        read_sam = session.query(models.User).filter(models.User.name == "Sam").one()
        print(f'Read Sam: {read_sam}')

        user = db.session.query(User).filter_by(username="admin").one_or_none()
        if not user:
            user = User(username="admin")
            db.session.commit()
        # db.session.commit()

    return app

host = "localhost"
port = 5656
app = create_app(host=host)

if __name__ == "__main__":
    app.run(host=host)

