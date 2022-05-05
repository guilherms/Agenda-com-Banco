from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask('app')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))
  password = db.Column(db.String(30))
  created_at = db.Column(db.String(100))
  updated_at = db.Column(db.String(100))

class contacts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))
  phone = db.Column(db.String(100))
  image = db.Column(db.String(100)) 
  user_id = db.Column(db.Integer)
  created_at = db.Column(db.String(100))
  updated_at = db.Column(db.String(100))

contatos=[
  {'name': 'João da Silva'},
  {'name': 'Maria Souza'},
]


@app.route('/')
def index():
  user = users.query.all()
  new_contacts = contacts.query.all()
  return render_template('index.html', user=user, new_contacts=new_contacts, contatos=contatos)

@app.route('/create', methods=['POST'])
def create():
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  contatos.append({
    'name': name, 'email': email, 'phone': phone
  })
  new_user = users(name=name, email=email)
  new_contacts = contacts(name=name, email=email, phone=phone)
  db.session.add(new_user)
  db.session.add(new_contacts)
  db.session.commit()
  return redirect('/')

if __name__ == '__main__':
  db.create_all()
  app.run(host='0.0.0.0', port=8080)