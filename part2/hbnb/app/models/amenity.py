#!/usr/bin/python3
from base_class import basemodel

class amenity(basemodel):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.places = []

    def add_place(self, place):
        self.places.append(place)
