from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class Houses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    house_name = SelectField("House Name", choices=[
    ("gryfinndor", "Gryfinndor"), 
        ("slytherin", "Slytherin"), 
        ("hufflepuff", "Hufflepuff")
    ])
    submit = SubmitField('Add Details')