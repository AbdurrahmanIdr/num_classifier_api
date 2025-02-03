"""
This module initializes the Flask application, applies CORS settings,
and registers the main blueprint for the application routes.
"""

from flask import Flask
from flask_cors import CORS
from app.routes import main_bp


def create_app():
    """
      Create and configure the Flask application.

      This function initializes the Flask application, applies CORS settings,
      and registers the main blueprint for the application routes.

      Returns:
          Flask: The configured Flask application instance.
      """
    app = Flask(__name__)
    CORS(app)


    app.register_blueprint(main_bp)

    return app
