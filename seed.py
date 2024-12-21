from app import app
from models import db, Employ

# データベースへの接続と初期化
with app.app_context():
    # 初期データのリスト
    seed_data = [
        {"name": "イチロー", "email": "ichiro@example.com", "department": "経理"},
        {"name": "大谷翔平", "email": "ootani@example.com", "department": "法務"},
        {"name": "新庄剛志", "email": "shinjo@example.com", "department": "営業"},
    ]

    # テーブルをクリアしてから新しいデータを挿入（必要に応じて）
    db.session.query(Employ).delete()  # 全削除
    for data in seed_data:
        employee = Employ(name=data["name"], email=data["email"], department=data["department"])
        db.session.add(employee)

    # コミットしてデータを保存
    db.session.commit()
    print("Database seeded successfully!")
