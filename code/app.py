from flask_restful import Api
from flask import Flask
from resources.user import User, Users
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sjvsecretkey'
api = Api(app)


@app.before_first_request
def create_tables():
    '''
    Method to create tables in the database before the first request.
    '''
    db.create_all()


api.add_resource(User, '/user',
                 '/user/<string:search_type>/<value>',
                 '/user/<int:user_id>'
                 )
api.add_resource(Users, '/users')

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)

db.init_app(app)

