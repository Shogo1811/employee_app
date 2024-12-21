from flask import Flask, render_template #, request, redirect, url_for
from flask_migrate import Migrate
from models import db, Employ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sample_user:sample_pass@localhost:5432/sample_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    employees = Employ.query.all()
    return render_template('employ_list.html', employees=employees)

if __name__ == "__main__":
    app.run(debug=True)
