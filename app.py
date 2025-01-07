from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_migrate import Migrate
from models import db, Employ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sample_user:sample_pass@localhost:5432/sample_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# セッション用に必要
app.secret_key = 'XXXX'

# ハードコードされた認証情報
USERNAME = 'admin'
PASSWORD = 'admin'

# ログイン実装前
@app.route('/')
def index():
    employees = Employ.query.all()
    return render_template('employee_list.html', employees=employees)

#　ログイン実装時
# @app.route('/')
# def index():
#     # if 'user' not in session:  # ログインチェック
#     #     return redirect(url_for('login'))

#     # ページ番号と検索キーワードを取得
#     page = request.args.get('page', 1, type=int)
#     per_page = 10  # 1ページあたりの表示件数
#     search = request.args.get('search', '', type=str)

#     # 検索条件を追加
#     query = Employ.query
#     if search:
#         query = query.filter(
#             Employ.name.ilike(f'%{search}%') |
#             Employ.email.ilike(f'%{search}%') |
#             Employ.department.ilike(f'%{search}%')
#         )

#     # ページングを適用
#     employees = query.paginate(page=page, per_page=per_page)

#     return render_template(
#         'employee_list.html',
#         user=session['user'],
#         employees=employees,
#         search=search
#     )

# ログイン機能実装
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if username == USERNAME and password == PASSWORD:
#             session['user'] = username  # セッションにユーザー情報を保存
#             flash('ログインに成功しました！', 'success')
#             return redirect(url_for('index'))
#         else:
#             flash('ログインに失敗しました。ユーザー名またはパスワードが間違っています。', 'danger')
#     return render_template('login.html')

# @app.route('/logout')
# def logout():
#     session.pop('user', None)  # セッションからユーザー情報を削除
#     session.pop('_flashes', None)  # 既存のフラッシュメッセージをクリア
#     flash('ログアウトしました。', 'info')
#     return redirect(url_for('login'))

# Postメソッド
# @app.route('/add', methods=['GET', 'POST'])
# def add_employee():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         department = request.form['department']
#         new_employee = Employ(name=name, email=email, department=department)
#         db.session.add(new_employee)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('employee_form.html', employee=None)

# @app.route('/edit/<int:id>', methods=['GET', 'POST'])
# def edit_employee(id):
#     employee = Employ.query.get_or_404(id)
#     if request.method == 'POST':
#         employee.name = request.form['name']
#         employee.email = request.form['email']
#         employee.department = request.form['department']
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('employee_form.html', employee=employee)

# @app.route('/delete/<int:id>', methods=['POST'])
# def delete_employee(id):
#     employee = Employ.query.get_or_404(id)
#     db.session.delete(employee)
#     db.session.commit()
#     return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
