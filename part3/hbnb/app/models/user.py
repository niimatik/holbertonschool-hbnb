#!/usr/bin/python3
from app import bcrypt
from app.models.base_class import basemodel
from email_validator import validate_email, EmailNotValidError


class User(basemodel):
    def __init__(self, first_name, last_name, email, password):
        super().__init__()
        if not first_name or not last_name or not email or not password:
            raise ValueError("Empty value !")
        if not validate_email(email):
            raise EmailNotValidError("Incorrect email !")
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hash_password(password)
        self.is_admin = False
        self.places = []
        self.reviews = []

    def add_places(self, place):
        self.places.append(place)

    def add_reviews(self, review):
        self.reviews.append(review)

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
