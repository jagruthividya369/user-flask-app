'''
This file deals User Model, which consists of multiple methods
that interacts with the database to serve multiple requests.
'''

import datetime
from db import db

class UserModel(db.Model):
    """
    A class to represent a User Model.
    ...

    Attributes
    ----------
    firstname : string
        first name of the user.
    lastname : string
        last name of the user.
    address : string
        address of the user.
    phone : int
        Phone Number of the user.
    creation_date : string
        Date of creation of the user in form of string.
    updation_date : string
        Date of Updation of th euser in form of string.

    Class Methods
    -------
    find_by_id(cls, _id)
    find_by_firstname(cls, firstname)
    find_by_lastname(cls, firstname)
    find_by_phone(cls, phone)
    find_by_first_and_last_name(cls, fname, lname):

    Methods
    -------
    json(self)
    save_to_db(self)
    delete_from_db(self)
    update_date(self)
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(15))
    lastname = db.Column(db.String(15))
    address = db.Column(db.String(15))
    phone = db.Column(db.BigInteger)
    creation_date = db.Column(db.String(12))
    updation_date = db.Column(db.String(12))

    def __init__(self, firstname, lastname, address, phone, creation_date, updation_date):
        self.firstname = firstname.capitalize()
        self.lastname = lastname.capitalize()
        self.address = address.capitalize()
        self.phone = phone
        self.creation_date = creation_date
        self.updation_date = updation_date

    def json(self):
        '''
        To return the UserModel Object in a json format
        '''
        return {"id": self.id,
                "firstname": self.firstname,
                "lastname": self.lastname,
                "address": self.address,
                "phone": self.phone,
                "creation_date": self.creation_date,
                "updation_date": self.updation_date}

    @classmethod
    def find_by_id(cls, _id):
        '''
        To Find a user in the database by Id.
        '''
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_firstname(cls, firstname):
        '''
        To Find a user in the database by First Name.
        '''
        return cls.query.filter_by(firstname=firstname).all()

    @classmethod
    def find_by_lastname(cls, lastname):
        '''
        To Find a user in the database by Last Name.
        '''
        return cls.query.filter_by(lastname=lastname).all()

    @classmethod
    def find_by_phone(cls, phone):
        '''
        To Find a user in the database by Phone Number.
        '''
        return cls.query.filter_by(phone=phone).all()

    @classmethod
    def find_by_first_and_last_name(cls, fname, lname):
        '''
        To Find a user in the database by both First Name and Last Name.
        '''
        return cls.query.filter_by(firstname=fname).filter_by(lastname=lname).all()

    def save_to_db(self):
        '''
        To Add a user into the database
        '''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        '''
        To delete the User from the database
        '''
        db.session.delete(self)
        db.session.commit()

    def update_date(self):
        '''
        Updating the details of the user and timestamp for updation_date
        '''
        db.session.query.update(
            {'updation_date': datetime.datetime.now()}, synchronize_session=False)
