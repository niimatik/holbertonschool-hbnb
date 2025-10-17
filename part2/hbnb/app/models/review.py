#!/usr/bin/python3
from app.models.base_class import basemodel


class Review(basemodel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        if not text:
            raise ValueError("text is empty !")
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
