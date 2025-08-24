from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from marshmallow import Schema, fields


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # one-to-many: customer --> reviews
    reviews = relationship("Review", back_populates="customer", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Customer {self.id}, {self.name}>'

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)

    # one-to-many: item --> reviews
    reviews = relationship("Review", back_populates="item", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Item {self.id}, {self.name}, {self.price}>'
    
class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)

    # foreign keys
    customer_id = db.Column(db.Integer, ForeignKey("customers.id"))
    item_id = db.Column(db.Integer, ForeignKey("items.id"))

    # relationships
    customer = relationship("Customer", back_populates="reviews")
    item = relationship("Item", back_populates="reviews")

    def __repr__(self):
        return f'<Review {self.id}, {self.comment}>'
