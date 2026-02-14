from epl import create_app, db

# เปลี่ยนเป็น 'config.MySQLConfig' เมื่อต้องการใช้ MySQL (epl_v2_db)
app = create_app('config.SQLiteConfig')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✅ Database tables created!")
    app.run(debug=True)
