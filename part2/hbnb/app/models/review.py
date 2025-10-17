#!/usr/bin/python3
from app.models.base_class import basemodel


class Review(basemodel):
    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        if not text or not rating or not place_id or not user_id:
            raise ValueError("text is empty !")
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id
