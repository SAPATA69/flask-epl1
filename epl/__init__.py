import os
from flask import Flask
from epl.extensions import db, migrate
from epl.core.routes import core_bp
from epl.clubs.routes import club_bp
from epl.players.routes import player_bp


def create_app(config_class='config.SQLiteConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.secret_key = b'hguyfdrerdfguhiophgytrt'

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(core_bp, url_prefix='/')
    app.register_blueprint(club_bp, url_prefix='/clubs')
    app.register_blueprint(player_bp, url_prefix='/players')

    return app