class Config:
    SECRET_KEY = 'dev-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class SQLiteConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///epl_v2.sqlite3'


class MySQLConfig(Config):
    # ชื่อ database ตรงตามที่อาจารย์สอน (ดูจาก HeidiSQL ในรูป)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/epl_v2_db'
