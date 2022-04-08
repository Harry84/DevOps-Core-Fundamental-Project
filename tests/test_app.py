from flask import url_for, request, redirect, render_template
from flask_testing import TestCase

from application import app, db
from application.models import Students, Houses, EnrolForm 

class TestBase(TestCase):
    def create_app(self):
 
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        
        db.drop_all()
        db.create_all()
        # Create test houses
        for hous in ['red', 'yellow', 'green', 'blue', 'orange']:
            houses = Houses(house_name=hous)
        # save houses to database
            db.session.add(houses)
        db.session.commit()

        sample = {'Jessica':1,'Henry':2,'Giles':3,'Esme':4}
        for stud in sample:
            students = Students(student_name=stud,house_id=sample[stud])
            db.session.add(students)
        db.session.commit()

    def tearDown(self):
        
        db.session.remove()
        db.drop_all()

# Write a test class to test Read functionality
class TestRead(TestBase):
    def test_index_get(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"red",response.data)
        self.assertIn(b"yellow",response.data)
        self.assertIn(b"blue",response.data)
        self.assertIn(b"green",response.data)
        self.assertIn(b"Jessica",response.data)
        self.assertIn(b"Henry",response.data)
        self.assertIn(b"Giles",response.data)
        self.assertIn(b"Esme",response.data)


    def test_readHous(self):
        response = self.client.get(url_for('addhouses'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Add",response.data)


    def test_read_house_list(self):
        response = self.client.get(url_for('listhouses'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"red",response.data)
        self.assertIn(b"yellow",response.data)
        self.assertIn(b"blue",response.data)
        self.assertIn(b"green",response.data)

    def test_read_student_list(self):
        response = self.client.get(url_for('liststudents'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Jessica",response.data)
        self.assertIn(b"Henry",response.data)
        self.assertIn(b"Giles",response.data)
        self.assertIn(b"Esme",response.data)

    def test_read_edit_student(self):
        response = self.client.get(url_for('edit_student'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Add",response.data)

    def test_read_edit_house(self):
        response = self.client.get(url_for('edit_house'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Add",response.data)


# Write a test to test Post functionality i.e. adding a new student to the db or adding a new house to the db

class TestAdd(TestBase):
    def test_add_student(self):
        response = self.client.post(url_for('register'), data = dict(name="TestStud",houseID=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'TestStud', response.data)

    def test_add_house(self):
        response = self.client.post(url_for('addhouses'), data = dict(name="TestHouse"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'TestHouse', response.data)

# Write tests to test delete functionality
class TestDelete(TestBase):
#removing an existing student and then trying to remove a non existing student to check else statement
    def test_delete_student(self):
        response = self.client.get(url_for('delete_student', name="Esme"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Esme', response.data)
        response = self.client.get(url_for('delete_student', name="Boris"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
#removing an existing house and then trying to remove a non existing house to check else statement
    def test_delete_house(self):
        response = self.client.get(url_for('delhouse', name="orange"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'orange', response.data)
        response = self.client.get(url_for('delhouse', name="purple"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

#deleting all students
    def test_delete_students(self):       
        response = self.client.get(url_for('clearall'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'TestHouse', response.data)

class TestCount(TestBase):
    def test_count_students(self):
        response = self.client.get(url_for('count_students'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"4", response.data)

class TestUpdate(TestBase):
    def test_update_student(self):
        response = self.client.get(url_for('update', name="Marie"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Marie', response.data)
        self.assertNotIn(b'Jessica', response.data)

    def test_amend_student(self):
        response = self.client.post(url_for('amend_student', prev="Jessica"),
        data = {"name": "Marie", "houseID": 1},
        follow_redirects=True)
        self.assertIn(b'Marie', response.data)
        # response = self.client.post(url_for('amend_student', prev="namenotpresent"),
        # self.assertEqual(response.status_code, 200)

    def test_amend_house(self):
        response = self.client.post(url_for('amend_house', old="green"),
        data = {"name": "white"},
        follow_redirects=True)
        self.assertIn(b'white', response.data)

#for any routes that access the database, test an item we know is in the db is in the html code for the page that displays that route:
class TestData(TestBase):

    def test_register_get(self):
        response = self.client.get(url_for('register'))
        assert "Esme" in response.data.decode()
        assert "green" in response.data.decode()

    def test_studentlist_get(self):
        response = self.client.get(url_for('liststudents'))
        assert "Esme" in response.data.decode()
        assert "Henry" in response.data.decode()

    def test_houselist_get(self):
        response = self.client.get(url_for('listhouses'))
        assert "red" in response.data.decode()
        assert "yellow" in response.data.decode()

    def test_addhouses_get(self):
        response = self.client.get(url_for('addhouses'))
        assert "add" in response.data.decode()

    def test_amend_student_get(self):
        response = self.client.post(url_for('amend_student', prev="Jessica"),
        data = {"name": "Marie", "houseID": 1},
        follow_redirects=True)
        assert "Hogwarts" in response.data.decode()

    def test_amend_house_get(self):
        response = self.client.post(url_for('amend_house', old="green"),
        data = {"name": "white"},
        follow_redirects=True)
        assert "Hogwarts" in response.data.decode()

    


#decode makes the page a string
        
        



