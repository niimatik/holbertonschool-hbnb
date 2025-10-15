#!/usr/bin/python3
from app.models.base_class import basemodel

class User(basemodel):
    def __init__(self, first_name, last_name, email, password, is_admin):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.__password = password
        self.is_admin = is_admin
        self.places = []
        self.reviews = []

    def add_places(self, place):
        self.places.append(place)

    def add_reviews(self, review):
        self.reviews.append(review)
