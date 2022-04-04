'''
This file deals with entire unit testcases written to test the application.
'''
import unittest
import json
import datetime
from app import app
from db import db


class UserTestCases(unittest.TestCase):
    '''
    This Class consists of multiple test cases to check the application
    is working properly under all conditions or not.

    Methods
    ---------
    setUp(self)
    test_00_create_user_success(self)
    test_01_get_all_users_success(self)
    test_02_get_users_by_firstname_success(self)
    test_03_get_users_by_lastname_success(self)
    test_04_get_users_by_firstandlastname_success(self)
    test_05_get_users_by_id_success(self)
    test_06_get_users_by_phone_success(self)
    test_07_update_user_success(self)
    test_11_create_user_failure(self)
    test_12_get_users_by_firstname_failure(self)
    test_13_get_users_by_lastname_failure(self)
    test_14_get_users_by_firstandlastname_failure(self)
    test_15_get_users_by_id_failure(self)
    test_16_get_users_by_phone_failure(self)
    test_17_update_user_failure(self)
    test_18_update_user_failure(self)
    test_19_delete_user_failure(self)
    test_20_delete_user_success(self)
    test_99_delete_database(self)
    '''

    def setUp(self):
        '''
        To Set Up the app with appropriate configuration.
        '''
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/users_sample'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['TESTING'] = True
        with app.app_context():
            db.create_all()
        self.tester = app.test_client(self)
        return self.tester

    def test_00_create_user_success(self):
        '''
        This test will checks whether the user will be stored in user
        if appropriate details are given
        '''
        current_datetime = str(datetime.date.today().strftime("%d/%m/%Y"))
        new_user = {'firstname': "Shika", 'lastname': "Khan", 'address': "Delhi",
                    'phone': 3624881264, 'creation_date': current_datetime,
                    'updation_date': current_datetime}
        response = self.tester.post('/user', data=new_user)
        new_user_1 = {'firstname': "Vikas", 'lastname': "Patel", 'address': "Kashmir",
                      'phone': 8723409752, 'creation_date': current_datetime,
                      'updation_date': current_datetime}
        self.tester.post('/user', data=new_user_1)
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], "User Created")

    def test_01_get_all_users_success(self):
        '''
        This test will check whether there are 2 users in the database or not.
        '''
        response = self.tester.get('/users')
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['number_of_users'], 2)

    def test_02_get_users_by_firstname_success(self):
        '''
        This test will check the results of searching userwith first name are correct or not.
        '''
        search_string = "Shika"
        response = self.tester.get('/user/firstname/'+search_string)
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 200)
        for i in data['users']:
            self.assertEqual(i['firstname'], search_string)

    def test_03_get_users_by_lastname_success(self):
        '''
        This test will check the results of searching user with last name are correct or not.
        '''
        search_string = "Khan"
        response = self.tester.get('/user/lastname/'+search_string)
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 200)
        for i in data['users']:
            self.assertEqual(i['lastname'], search_string)

    def test_04_get_users_by_firstandlastname_success(self):
        '''
        This test will check the results of searching user with first name and \
            last name are correct or not.
        '''
        search_string1 = "Shika"
        search_string2 = "Khan"
        response = self.tester.get(
            '/user/firstlastname/'+search_string1+","+search_string2)
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 200)
        for i in data['users']:
            self.assertEqual(i['firstname'], search_string1)
            self.assertEqual(i['lastname'], search_string2)

    def test_05_get_users_by_id_success(self):
        '''
        This test will check the results of searching user with user id are correct or not.
        '''
        search_string = 1
        response = self.tester.get('/user/id/'+str(search_string))
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['firstname'], "Shika")
        self.assertEqual(data['lastname'], 'Khan')
        self.assertEqual(data['address'], "Delhi")
        self.assertEqual(data['phone'], 3624881264)

    def test_06_get_users_by_phone_success(self):
        '''
        This test will check the results of searching user with phone number are correct or not.
        '''
        search_string = 3624881264
        response = self.tester.get('/user/phone/'+str(search_string))
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 200)
        for i in data['users']:
            self.assertEqual(i['phone'], 3624881264)

    def test_07_update_user_success(self):
        '''
        This test will check the results of updating user details are correct or not.
        '''
        current_datetime = str(datetime.date.today().strftime("%d/%m/%Y"))
        new_user = {'id': 1, 'firstname': "Vikas", 'lastname': "Bhat", 'address': "Mumbai",
                    'phone': 7831594681, 'creation_date': current_datetime,
                    'updation_date': current_datetime}
        response = self.tester.put('/user', data=new_user)
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['firstname'], "Vikas")
        self.assertEqual(data['lastname'], 'Bhat')
        self.assertEqual(data['address'], "Mumbai")
        self.assertEqual(data['phone'], 7831594681)

    def test_11_create_user_failure(self):
        '''
        This test will check whether the storing user details will fail or not
        if inputted phone number is already exists in the database or not.
        '''
        current_datetime = str(datetime.date.today().strftime("%d/%m/%Y"))
        new_user = {'firstname': "Shika", 'lastname': "Khan", 'address': "Delhi",
                    'phone': 7831594681, 'creation_date': current_datetime,
                    'updation_date': current_datetime}
        response = self.tester.post('/user', data=new_user)
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            data['message'], "An user with phone number: 7831594681 already exits. \
                So please enter valid phone number")

    def test_12_get_users_by_firstname_failure(self):
        '''
        This test will check the results of searching user with first name
        results user not found if no such first name exists in database.
        '''
        search_string = "ShikaShika"
        response = self.tester.get('/user/firstname/'+search_string)
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], "No such User Found")

    def test_13_get_users_by_lastname_failure(self):
        '''
        This test will check the results of searching user with last name
        results user not found if no such last name exists in database.
        '''
        search_string = "KhanKhan"
        response = self.tester.get('/user/lastname/'+search_string)
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], "No such User Found")

    def test_14_get_users_by_firstandlastname_failure(self):
        '''
        This test will check the results of searching user with first and last name
        results user not found if no such first and last name exists in database.
        '''
        search_string1 = "ShikaShika"
        search_string2 = "KhanKhan"
        response = self.tester.get(
            '/user/firstlastname/'+search_string1+","+search_string2)
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], "No such User Found")

    def test_15_get_users_by_id_failure(self):
        '''
        This test will check the results of searching user with fid
        results user not found if no such id exists in database.
        '''
        search_string = 25
        response = self.tester.get('/user/id/'+str(search_string))
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], "No such User Found")

    def test_16_get_users_by_phone_failure(self):
        '''
        This test will check the results of searching user with phone number
        results user not found if no such phone number exists in database.
        '''
        search_string = 9624881264
        response = self.tester.get('/user/phone/'+str(search_string))
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], "No such User Found")

    def test_17_update_user_failure(self):
        '''
        The test which check if the result is phone number already exists if user tried to update
        phone number which is already exists in the database or not.
        '''
        current_datetime = str(datetime.date.today().strftime("%d/%m/%Y"))
        new_user = {'id': 1, 'firstname': "Vikas", 'lastname': "Bhat", 'address': "Mumbai",
                    'phone': 8723409752, 'creation_date': current_datetime,
                    'updation_date': current_datetime}
        response = self.tester.put('/user', data=new_user)
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            data['message'], "An user with phone number: 8723409752 already exits. \
                    So please enter valid phone number")

    def test_18_update_user_failure(self):
        '''
        The test which check if the result is phone number already exists if user tried to
        create user with phone number which is already exists in the database or not.
        '''
        current_datetime = str(datetime.date.today().strftime("%d/%m/%Y"))
        new_user = {'id': 5, 'firstname': "Vikas", 'lastname': "Bhat", 'address': "Mumbai",
                    'phone': 8723409752, 'creation_date': current_datetime,
                    'updation_date': current_datetime}
        response = self.tester.put('/user', data=new_user)
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            data['message'], "An user with phone number: 8723409752 already exits. \
                    So please enter valid phone number")

    def test_19_delete_user_failure(self):
        '''
        Test to check whether the result is no such user found if
        incorrect user id is provided.
        '''
        delete_user_id = 20
        response = self.tester.delete('/user/'+str(delete_user_id))
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], "No such User Found")

    def test_20_delete_user_success(self):
        '''
        Test to check whether the user will be deleted or not\
        if appropriate user id is provided
        '''
        delete_user_id = 1
        response = self.tester.delete('/user/'+str(delete_user_id))
        data = json.loads(response.data.decode('utf8').replace("'", '"'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "User Deleted")

    def test_99_delete_database(self):
        '''
        This method will delete the created contents in the database.
        '''
        with app.app_context():
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
