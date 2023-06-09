from flask import Flask
from config import Config
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    jwt.init_app(app)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .main import main_bp
    app.register_blueprint(main_bp)

    from .faker import faker_bp
    app.register_blueprint(faker_bp)

    from .user import user_bp
    app.register_blueprint(user_bp)

    from .post import post_bp
    app.register_blueprint(post_bp)

    from .api import api_bp
    app.register_blueprint(api_bp)

    from . import models

    @login_manager.user_loader
    def load_user(user_id):
        return models.User.query.get(user_id)

    @app.context_processor
    def context_processor():
        return dict(
            current_user=current_user
        )

    return app


app = create_app()
