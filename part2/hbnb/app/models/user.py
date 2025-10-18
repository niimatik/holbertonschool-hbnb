#!/usr/bin/python3
from app.models.base_class import basemodel
from email_validator import validate_email, EmailNotValidError


class User(basemodel):
    def __init__(self, first_name, last_name, email, is_admin):
        super().__init__()
        if not first_name or not last_name or not email:
            raise ValueError("Empty value !")
        if not validate_email(email):
            raise EmailNotValidError("Incorrect email !")
        if is_admin == "" or type(is_admin) is not bool:
            raise ValueError("is_admin must be True or False !")
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []
        self.reviews = []

    def add_places(self, place):
        self.places.append(place)

    def add_reviews(self, review):
        self.reviews.append(review)
