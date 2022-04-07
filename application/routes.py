from application import app, db
from application.models import Houses, Students
from flask import render_template, redirect, url_for, request
from application.models import EnrolForm, HouseAdd, HouseRemove, AmendStudent
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
        return redirect(url_for('liststudents'))
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

'''__________________below not working yet___________________________________________'''

@app.route('/amend_student/<prev>', methods=['GET', 'POST'])
def amend_student(prev):
    form = EnrolForm()
    allhouses = db.session.query(Houses).all()
    for i in allhouses:
        form.houseID.choices.append((i.id,i.house_name))

    amended_student = db.session.query(Students).filter_by(student_name=prev).first()
    if request.method == 'POST':
        if amended_student:
            amended_student.student_name = form.name.data
            amended_student.house_id = form.houseID.data
            db.session.commit()
            return redirect(url_for('register'))
    else:
        return render_template('edit_student.html', form=form, allhouses=allhouses)

#making a page to edit students from

@app.route('/edit_student', methods = ['GET','POST'])
def edit_student():
    form = EnrolForm()
    allhouses = db.session.query(Houses).all()
    students = Students.query.join(Houses).all()
    return render_template('edit_student.html', form=form, studentss=students)

#making a list of houses to populate a page - house_list.html

@app.route('/studentlist', methods = ['GET','POST'])
def liststudents():
    allhouses = db.session.query(Houses).all()
    students = Students.query.join(Houses).all()
    return render_template('studentlist.html', studentss=students)

#trying to make a route to delete a house by supplying name to a form or clicking a button on houselist.html - need to specify not to delete houses with existing students
@app.route('/delhouse/<name>',  methods = ['GET', 'DELETE'])
def delhouse(name):
    house_to_delete = db.session.query(Houses).filter_by(house_name=name).first()
    print(str(house_to_delete))
    if house_to_delete == "Gryfinndor" or house_to_delete == "Slytherin" or house_to_delete == "Hufflepuff" or house_to_delete == "Ravenclaw":
        return redirect(url_for('listhouses'))
    elif house_to_delete:
        db.session.delete(house_to_delete)
        db.session.commit()
        return redirect(url_for('listhouses'))
    else:
        return redirect(url_for('register'))

@app.route('/houselist', methods = ['GET','POST'])
def listhouses():
    allhouses = db.session.query(Houses).all()
    return render_template('houselist.html', allhouses=allhouses)


    

    