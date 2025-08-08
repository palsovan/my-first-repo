from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///billing.db'
db = SQLAlchemy(app)

class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Bill {self.id}>'

@app.route('/')
def index():
    bills = Bill.query.all()
    return render_template('index.html', bills=bills)

@app.route('/add_bill', methods=['GET', 'POST'])
def add_bill():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        amount = float(request.form['amount'])
        new_bill = Bill(customer_name=customer_name, amount=amount)
        db.session.add(new_bill)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_bill.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)