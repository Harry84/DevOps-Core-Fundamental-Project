from application import db
from application.models import Houses, BasicForm

# db.drop_all()
db.create_all()

# new_house = Houses(name="Gryffindor")
# db.session.add(new_house)
# db.session.commit()

# new_house = Houses(name="Hufflepuff")
# db.session.add(new_house)
# db.session.commit()

# new_house = Houses(name="Slytherin")
# db.session.add(new_house)
# db.session.commit()

'''HOW TO DO VARIOUS METHODS - CRUD'''



'''using order by'''
# list_of_houses = Houses.query.order_by(Houses.id).all()
# print(list_of_houses[0].name)

# print(Houses.query.order_by(Houses.id).first())

'''using filter by'''

# list_of_houses = Houses.query.filter_by(id=1).all()
# print(list_of_houses[0].name)

'''using get'''

# list_of_houses = Houses.query.filter_by(id=1).get(1)
# print(list_of_houses.name)

'''using count'''

# list_of_houses = Houses.query.count()
# print(list_of_houses)

'''we can use as many methods as we want in one query between query. but all() count() get() must always be the last one'''

# house_to_update = Houses.query.all.filter_by(id=3).first()
# print(house_to_update)

'''remember this returns an object, so we need to do:'''

# house_to_update.name = "Hufflepuff"

'''now we changed the name we need to push across to the corresponding db entry =>'''

# db.session.commit()

'''to delete'''

# house_to_delete = Houses.query.all.filter_by(id=3).first()
# print(house_to_delete)

# db.session.delete(house_to_delete)
# db.session.commit()

'''so in other words we need to find the object we want to manipulate first i.e. read first, then change then commmit'''

'''using a for loop i.e. "pythonic code" to delete all the games in the db - time saving!'''

# house_to_delete = Houses.query.all()


# for house in house_to_delete:
#     db.session.delete(house)
#     db.session.commit()

'''taking user input to select a houses's id to delete'''

# house_to_delete = input("which house u wanna delete? ")

# houses_to_delete = Houses.query.get(house_to_delete)