from flask import Flask, render_template,request,redirect
from forms import Fetch, Add
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///patient.db'
app.config['SECRET_KEY'] = '123456'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    retype = db.Column(db.String(120)) 
    First_name = db.Column(db.String(50), nullable=False)
    Last_name = db.Column(db.String(50), nullable=False)
    id_number = db.Column(db.String(20), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    def __repr__(self):
        return f"patient('{self.username}', '{self.email}', '{self.password}', '{self.retype}', '{self.First_name}', '{self.Last_name}', '{self.id_number}', '{self.date_of_birth}')"


with app.app_context():
    db.create_all()

patients = []



   
@app.route('/commoninfo/add', methods=['GET', 'POST'])
def add():
   form = Add()
   if request.method == 'GET':
       return render_template('add.html', form=form)
   
   elif request.method == 'POST'  and form.validate_on_submit():
           username = form.username.data
           email = form.email.data
           password = form.password.data
           retype = form.retype.data
           First_name = form.First_name.data
           Last_name = form.Last_name.data
           id_number = form.id_number.data
           date_of_birth = form.date_of_birth.data

           patient = Patient(username=username, email=email, password=password, retype=retype, First_name=First_name, Last_name=Last_name, id_number=id_number, date_of_birth=date_of_birth)
           p_id=Patient.query.filter_by(id_number=id_number).first() 

           if p_id:
               return "Patient already exists"
           else:
                db.session.add(patient)
                db.session.commit()
                patients.append({'username': username,
                    'email': email,
                    'password': password,
                    'retype': retype,
                    'First_name': First_name,
                    'Last_name': Last_name,
                    'id_number': id_number,
                    'date_of_birth': date_of_birth
                    })
                return redirect('/commoninfo/fetch')
              
@app.route('/commoninfo/fetch', methods=['GET', 'POST'])
def fetch():
    form = Fetch()
    if request.method == 'GET':
        return render_template('fetch.html', form=form)
    
    elif request.method == 'POST':
        id_number = form.id_number.data
        p_id = Patient.query.filter_by(id_number=id_number).first()
        if p_id:
            return (
                f"Patient Name: {p_id.username}, "
                f"Unique ID: {p_id.id_number}, "
                f"Birthdate: {p_id.date_of_birth}"
            )
        else:
            error = "Patient does not exist."
            return render_template('fetch.html', form=form, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
