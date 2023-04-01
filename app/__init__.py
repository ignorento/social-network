from flask import Flask
from config import Config
from flask_login import current_user

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .main import main_bp
    app.register_blueprint(main_bp)

    @app.context_processor
    def context_processor():
        return dict(
            current_user=current_user
        )

    return app


app = create_app()
from .main import routes
