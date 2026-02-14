from epl import create_app, db

app = create_app('config.MySQLConfig')  #  ต้องใช้  MySQL จำำำำำไว้้เด้ออออ

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✅ Database tables created!")
    app.run(debug=True)