from application import app, db
from application.models import Houses, Students
from flask import render_template, redirect, url_for, request
from application.models import EnrolForm, HouseAdd
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

# @app.route('/clear')
# def clear():

#     allhouses = db.session.query(Houses).all()

#     for hous in allhouses:
#         db.session.delete(hous)
#         db.session.commit()
    
#     return render_template('index.html', form=form, studentss=students)

# # @app.route('/read')
# # def read():
# #     all_houses = Houses.query.all()
# #     houses_string = ""
# #     for house in all_houses:
# #         houses_string += "<br>"+ house.name
# #     return houses_string

# # @app.route('/update/<name>')
# # def update(name):
# #     first_house = Houses.query.first()
# #     first_house.name = name
# #     db.session.commit()
# #     return first_house.name

# '''Add a new route called /delete that will delete the first entry in the database. Have it return a message to let you know you have deleted the entry.'''

# # @app.route('/clear')
# # def clear():

# #     game_to_delete = Games.query.all()

# #     for game in game_to_delete:
# #         db.session.delete(game)
# #         db.session.commit()
# #         return "Games deleted"

# # '''above for loop not quite working'''

# # @app.route('/delete')
# # def delete():
# #     first_house = Houses.query.first()
# #     db.session.delete(first_house)
# #     db.session.commit()
# #     return "First house deleted"

# # '''Add another route that returns the number of houses in the database.'''

# # @app.route('/count')
# # def count():
# #     list_of_houses = Houses.query.count()
# #     return f"The number of houses in the database is {list_of_houses}"


# '''--------------------------------------'''