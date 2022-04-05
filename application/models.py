# from wtforms_sqlalchemy.fields import QuerySelectField
from application import db 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError



class Houses(db.Model):
    __tablename__ = 'houses'
    id = db.Column(db.Integer, primary_key=True)
    house_name = db.Column(db.String(30), nullable=False)
    students = db.relationship('Students', backref='house_idbr')

class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(30), nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey('houses.id'), nullable=False)

class EnrolForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    houseID = SelectField("houses", choices = [])
    submit = SubmitField('Sort me oh Hat!')

class HouseAdd(FlaskForm):
    name = StringField("Subject Name", validators=[DataRequired()])
    submit = SubmitField('Add')


'''above here______________________'''

# class Houses(db.Model):
#     __tablename__ = 'houses'
#     id = db.Column(db.Integer, primary_key=True)
#     house_name = db.Column(db.String(30), nullable=False)
#     students = db.relationship('Students', backref='house_idbr')

# class Staff(db.Model):
#     __tablename__ = 'staff'
#     id = db.Column(db.Integer, primary_key=True)
#     staff_name = db.Column(db.String(30), nullable=False)
#     house_id = db.Column(db.Integer, db.ForeignKey('houses.id'), nullable=False)