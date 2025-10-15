#!/usr/bin/python3
from app.models.base_class import basemodel

class review(basemodel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
