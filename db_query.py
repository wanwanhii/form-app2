from app import create_app, db
from app.models import Email

# Flaskアプリケーションのインスタンスを作成
app = create_app()

# アプリケーションのコンテキストを管理する
with app.app_context():
    # データベースからすべてのメールアドレスを取得
    emails = Email.query.all()

    # 結果を表示
    for email in emails:
        print(f"Email: {email.email}, Registered Date: {email.date_registered}")