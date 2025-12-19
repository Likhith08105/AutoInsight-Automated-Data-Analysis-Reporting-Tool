from flask import Flask
from app.config import Config
import os

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.getcwd(), "templates"),
        static_folder=os.path.join(os.getcwd(), "static")
    )

    app.config.from_object(Config)

    from app.main import main_bp
    app.register_blueprint(main_bp)

    return app
