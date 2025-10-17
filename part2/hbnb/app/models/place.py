#!/usr/bin/python3
from app.models.base_class import basemodel


class Place(basemodel):
    def __init__(self, title, description, price,
                 latitude, longitude, owner_id):
        super().__init__()
        if not title:
            raise ValueError("title is empty !")
        self.title = title
        self.description = description
        if price < 0:
            raise ValueError("Your place must cost at least 0€")
        self.price = price
        if latitude < -90 or latitude > 90:
            raise ValueError(
                "The latitude or your place must be between -90 and 90"
            )
        self.latitude = latitude
        if longitude < -180 or longitude > 180:
            raise ValueError(
                "The longitude of your place must be between -180 and 180"
            )
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = []  # List to store related amenities
        self.reviews = []  # List to store related reviews

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
