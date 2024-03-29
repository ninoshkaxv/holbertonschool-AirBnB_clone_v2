#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60),  ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer(0), nullable=False)
    number_bathrooms = Column(Integer(0), nullable=False)
    max_guest = Column(Integer(0), nullable=False)
    price_by_night = Column(Integer(0), nullable=False)
    latitude = Column(Float(0.0))
    longitude = Column(Float(0.0))
    amenity_ids = []

    reviews = relationship("Review", backref="place", cascade="all, delete")

    @property
    def review(self):
        """Return a list of reviews"""
        list_reviews = storage.all(Review)
        place_reviews = [review for review in list_reviews.values()
                         if review.place_id == self.id]
        return place_reviews
