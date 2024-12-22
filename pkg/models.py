from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class User(db.Model):
    user_id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    username = db.Column(db.String(100), nullable=False,index=True)
    email= db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable= False)
    role= db.Column(db.Enum('Admin', 'Customer'), default= 'Customer', nullable=False)
    date_reg= db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Product(db.Model):
    prod_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    brand = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    size_ml = db.Column(db.Integer, nullable=False)
    fragrance_family = db.Column(db.String(100), nullable=True)
    top_notes = db.Column(db.String(255), nullable=True)
    middle_notes = db.Column(db.String(255), nullable=True)
    base_notes = db.Column(db.String(255), nullable=True)
    stock = db.Column(db.Integer, default=0, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    class Category(db.Model):
        cat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        name = db.Column(db.String(100), unique=True, nullable=False)
        description = db.Column(db.Text, nullable=True)

    class ProductCategory(db.Model):

        prodcat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        product_id = db.Column(db.Integer, db.ForeignKey('product.prod_id'), nullable=False)
        category_id = db.Column(db.Integer, db.ForeignKey('category.cat_id'), nullable=False)

        # Relationships
        product = db.relationship('Product', backref=db.backref('product_categories', lazy='dynamic'))
        category = db.relationship('Category', backref=db.backref('product_categories', lazy='dynamic'))


class Order(db.Model):

    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.Enum('Pending', 'Shipped', 'Delivered', 'Cancelled'), default='Pending', nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user = db.relationship('User', backref=db.backref('orders', lazy='dynamic'))

