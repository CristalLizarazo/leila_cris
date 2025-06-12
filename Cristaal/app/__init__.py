from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .config import Config

# Extensiones
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(test_config=None):
    app = Flask(__name__)

    # Si viene config de prueba, úsala. Si no, usa la de producción
    if test_config:
        app.config.update(test_config)
    else:
        app.config.from_object(Config)

    # Inicializa las extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Importar y registrar rutas
    from .routes.auth_routes import auth_bp
    from .routes.book_routes import book_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(book_bp)

    return app
