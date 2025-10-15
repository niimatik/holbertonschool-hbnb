#!/usr/bin/python3
from app.models.base_class import basemodel

class Amenity(basemodel):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.places = []

    def add_place(self, place):
        self.places.append(place)
