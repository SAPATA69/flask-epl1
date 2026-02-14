class Config:
    SECRET_KEY = 'dev-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class SQLiteConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///epl_v2.sqlite3'


class MySQLConfig(Config):
    # ชื่อ database  ดูจาก HeidiSQL ในรูป ฮาฟผม
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/epl_s02_db'
