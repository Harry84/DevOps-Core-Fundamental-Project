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

    # def __repr__(self):
    #     return 'Choose {}'.format(self.house_name)

class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(30), nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey('houses.id'), nullable=False)

class EnrolForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    houseID = SelectField("houses", choices = [])
    submit = SubmitField('Sort me non-random Hat!')

class HouseAdd(FlaskForm):
    name = StringField("House Name", validators=[DataRequired()])
    submit = SubmitField('Add')

class HouseRemove(FlaskForm):
    name = StringField("House Name", validators=[DataRequired()])
    submit = SubmitField('Remove')

class AmendStudent(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    houseID = SelectField("houses", choices = [])
    submit = SubmitField('Add')

class HouseForm(FlaskForm):
    name = StringField("Enter your preferred new house name", validators=[DataRequired()])
    # houseID = SelectField("houses", choices = [])
    submit = SubmitField('Submit')

