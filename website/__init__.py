import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.urandom(64)

    from .auth import auth
    from .views import views

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
