from app import create_app, db
from app.models import Email

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # データベースのテーブルを作成
    app.run(debug=True)