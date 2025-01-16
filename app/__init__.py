from flask import Flask, jsonify
from app.extension import db, login_manager, bcrypt, migrate
from app.config import Config
from app.routes.auth import auth_bp
from app.routes.employee import bp
from app.models import user


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # Обработчики ошибок
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error"}), 500

    app.register_blueprint(auth_bp)
    app.register_blueprint(bp)

    # Создание таблиц если еще не созданы
    with app.app_context():
        db.create_all()

    return app
