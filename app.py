from flask import Flask, render_template, request, redirect, url_for
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
    return render_template('employee_list.html', employees=employees)

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        department = request.form['department']
        new_employee = Employ(name=name, email=email, department=department)
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('employee_form.html', employee=None)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    employee = Employ.query.get_or_404(id)
    if request.method == 'POST':
        employee.name = request.form['name']
        employee.email = request.form['email']
        employee.department = request.form['department']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('employee_form.html', employee=employee)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_employee(id):
    employee = Employ.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
