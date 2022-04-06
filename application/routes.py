from application import app, db
from application.models import Houses, Students
from flask import render_template, redirect, url_for, request
from application.models import EnrolForm, HouseAdd, AmendStudent
import pdb

@app.route('/', methods = ['GET', 'POST'])
@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = EnrolForm()
    students = Students.query.join(Houses).all()
    allhouses = db.session.query(Houses).all()
    for i in allhouses:
        form.houseID.choices.append((i.id,i.house_name))

    if request.method == 'POST':
        new_student = Students(student_name=form.name.data,house_id=form.houseID.data)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('register'))
        
    return render_template('index.html', form=form, studentss=students)


@app.route('/addhouses', methods = ['GET','POST'])
def addhouses():
    allhouses = db.session.query(Houses).all()
    form = HouseAdd()
    if request.method == 'POST':
        new_house = Houses(house_name=form.name.data)
        db.session.add(new_house)
        db.session.commit()
        return redirect(url_for('register'))
    else:
        return render_template('addhouses.html', form=form, allhouses=allhouses)

@app.route('/delete_student/<name>')
def delete_student(name):
    student_to_delete = db.session.query(Students).filter_by(student_name=name).first()
    if student_to_delete:
        db.session.delete(student_to_delete)
        db.session.commit()
        return redirect(url_for('register'))
    else:
        return redirect(url_for('register'))

@app.route('/clearall')
def clearall():

    allstudents = db.session.query(Students).all()

    for studs in allstudents:
        db.session.delete(studs)
        db.session.commit()
    
    return redirect(url_for('register'))


@app.route('/count_students')
def count_students():
    num_of_students = Students.query.count()
    return f"The number of students in the database is {num_of_students}"


@app.route('/update/<name>')
def update(name):
    first_student = Students.query.first()
    first_student.student_name = name
    db.session.commit()
    return redirect(url_for('register'))

@app.route('/amend_student/<prev>', methods=['GET', 'POST'])
def amend(prev):
    form = AmendStudent()
    students = Students.query.join(Houses).all()
    allhouses = db.session.query(Houses).all()
    if request.method == 'POST':
        amended_student = db.session.query(Students).filter_by(student_name=prev).first()
        amended_student.student_name = request.form.get('name')
        db.session.commit()
        return redirect(url_for('register'))
    else:
        return render_template('amend_student.html', form=form, amended_student=amended_student)
    