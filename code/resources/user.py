'''
This deals with User Resource, which consists of get, put, update and delete methods.
And Users Resource, which consists of get method.
'''
import datetime
from flask_restful import Resource, reqparse
from models.user import UserModel

class User(Resource):
    '''
    Class that represents User Resource.
    Defines post, get, delete, update methods of user resource.
    '''
    parser = reqparse.RequestParser()
    parser.add_argument('id',
                        type=int,
                        required=False,
                        help="First Name cannot be blank!"
                        )
    parser.add_argument('firstname',
                        type=str,
                        required=True,
                        help="First Name cannot be blank!"
                        )

    parser.add_argument('lastname',
                        type=str,
                        required=True,
                        help="Last Name cannot be blank!"
                        )
    parser.add_argument('address',
                        type=str,
                        required=True,
                        help="Address cannot be blank!"
                        )
    parser.add_argument('phone',
                        type=int,
                        required=True,
                        help="Phone cannot be blank!"
                        )

    def post(self):
        '''
        To save given new user details.
        '''
        user = User.parser.parse_args()
        if UserModel.find_by_phone(user['phone']):
            return {'message': "An user with phone number: {} already exits. \
                So please enter valid phone number".format(user['phone'])}, 400

        current_datetime = str(datetime.date.today().strftime("%d/%m/%Y"))
        new_user = UserModel(user['firstname'], user['lastname'],
                             user['address'], user['phone'], current_datetime, current_datetime)

        try:
            new_user.save_to_db()
        except Exception:
            return {"message": "An Exception Occured, Please Try Again"}, 500

        return {"message": "User Created", "details": new_user.json()}, 201

    def get(self, search_type, value):
        '''
        To retrieve the details of the user under different search conditions. i.e.,
        1. First Name
        2. Last Name
        3. Phone Number
        4. Id
        5. First Name and Last Name
        '''
        if search_type == "firstname":
            user = UserModel.find_by_firstname(value)
            if user:
                return {'users': list(map(lambda x: x.json(), user))}
            return {"message": "No such User Found"}, 404

        elif search_type == "lastname":
            user = UserModel.find_by_lastname(value)
            if user:
                return {'users': list(map(lambda x: x.json(), user))}
            return {"message": "No such User Found"}, 404

        elif search_type == "phone":
            user = UserModel.find_by_phone(value)
            if user:
                return {'users': list(map(lambda x: x.json(), user))}
            return {"message": "No such User Found"}, 404

        elif search_type == "id":
            user = UserModel.find_by_id(value)
            if user:
                return user.json()
            return {"message": "No such User Found"}, 404

        else:
            fname, lname = value.split(",")
            user = UserModel.find_by_first_and_last_name(fname, lname)
            if user:
                return {'users': list(map(lambda x: x.json(), user))}
            return {"message": "No such User Found"}, 404

    def put(self):
        '''
        To Update the user details by id. If that Id doesn't exists it'll create a new user.
        '''
        data = User.parser.parse_args()
        user = UserModel.find_by_id(data['id'])
        if user:
            user.firstname = data['firstname'].capitalize()
            user.lastname = data['lastname'].capitalize()
            user.address = data['address'].capitalize()
            user.phone = data['phone']
            user.updation_date = str(
                datetime.date.today().strftime("%d/%m/%Y"))
            mid_result = {'users': list(
                map(lambda x: x.json(), UserModel.find_by_phone(user.phone)))}
            if len(mid_result['users']) > 1 or mid_result['users'][0]['id'] != user.id \
                or mid_result['users'][-1]['id'] != user.id:
                return {'message': "An user with phone number: {} already exits. \
                    So please enter valid phone number".format(user.phone)}, 400
        else:
            current_datetime = str(datetime.date.today().strftime("%d/%m/%Y"))
            user = UserModel(data['firstname'].capitalize(), data['lastname'].capitalize(
            ), data['address'].capitalize(), data['phone'], current_datetime, current_datetime)

            if UserModel.find_by_phone(user.phone):
                return {'message': "An user with phone number: {} already exits. \
                    So please enter valid phone number".format(user.phone)}, 400

        user.save_to_db()
        return user.json(), 200

    def delete(self, user_id):
        '''
        To delete the user from database.
        '''
        user = UserModel.find_by_id(user_id)
        if user:
            try:
                user.delete_from_db()
                return {"message": "User Deleted"}, 200
            except Exception:
                return {"message": "An Exception Occured, Please Try Again"}, 500

        return {"message": "No such User Found"}, 404


class Users(Resource):
    '''
    This class represents Users Resource.
    Defines get method for this resource.
    '''
    def get(self):
        '''
        To retrive all the users in the database.
        '''
        users = UserModel.query.all()
        return {'number_of_users': len(users), 'users': list(map(lambda x: x.json(), users))}
