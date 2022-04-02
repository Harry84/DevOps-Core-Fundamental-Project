from application import app, db
from application.models import Houses, BasicForm
from flask import Flask, render_template, request


@app.route('/add')
def add():
    new_house = Houses(name="New House")
    db.session.add(new_house)
    db.session.commit()
    return "Added new house to database"

@app.route('/read')
def read():
    all_houses = Houses.query.all()
    houses_string = ""
    for house in all_houses:
        houses_string += "<br>"+ house.name
    return houses_string

@app.route('/update/<name>')
def update(name):
    first_house = Houses.query.first()
    first_house.name = name
    db.session.commit()
    return first_house.name

'''Add a new route called /delete that will delete the first entry in the database. Have it return a message to let you know you have deleted the entry.'''

# @app.route('/clear')
# def clear():

#     game_to_delete = Games.query.all()

#     for game in game_to_delete:
#         db.session.delete(game)
#         db.session.commit()
#         return "Games deleted"

'''above for loop not quite working'''

@app.route('/delete')
def delete():
    first_house = Houses.query.first()
    db.session.delete(first_house)
    db.session.commit()
    return "First house deleted"

'''Add another route that returns the number of houses in the database.'''

@app.route('/count')
def count():
    list_of_houses = Houses.query.count()
    return f"The number of houses in the database is {list_of_houses}"


'''--------------------------------------'''

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        house_name = form.house_name.data

        new_house = Houses(name=str(house_name))
        db.session.add(new_house)
        db.session.commit()

        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply both first and last name and choose a house"
        else:
            message = f'Thank you, {first_name} {last_name}, welcome to {house_name}'

    return render_template('home.html', form=form, message=message)