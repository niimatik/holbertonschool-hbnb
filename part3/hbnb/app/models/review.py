#!/usr/bin/python3
from app.models.base_class import basemodel
from app import db


class Review(basemodel):
    __tablename__ = 'reviews'

    text = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        if not text or not rating or not place_id or not user_id:
            raise ValueError("Some fields are empty !")
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5 !")
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id
