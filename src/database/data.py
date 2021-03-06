from datetime import datetime
from decimal import *

from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey, create_engine, Numeric
from sqlalchemy import event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# decimal operations settings
getcontext().rounding = ROUND_HALF_UP
Base = declarative_base()


# customer has a one-to-many relationship with template, where customer is the parent
class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    alias = Column(String)
    firm_name = Column(String)
    last_name = Column(String)
    first_name = Column(String)
    tax_id = Column(String, nullable=False)
    address = Column(String)
    postal_code = Column(String)
    city = Column(String)
    payment = Column(Boolean)
    template = relationship("Template")


# product has many-to-many relationship with template, where template is the parent
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    symbol = Column(String)
    unit = Column(String, nullable=False)
    unit_net_price = Column(Numeric(precision=2), nullable=False)
    vat_rate = Column(Numeric(precision=2), nullable=False)
    per_month = Column(Boolean, nullable=False)


class Settings(Base):
    __tablename__ = "settings"
    id = Column(Integer, primary_key=True)
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)


class Numbering(Base):
    __tablename__ = "numbering"
    id = Column(Integer, primary_key=True)
    month = Column(Integer)
    number = Column(Integer)

    def __init__(self):
        self.date = datetime.now().month
        self.number = 1


# association table for the products-template many-to-many relationship
association_table = Table('association', Base.metadata,
                          Column('product_id', Integer, ForeignKey('products.id')),
                          Column('template_id', Integer, ForeignKey('template.id')))


# template implements one-to-one relationship with customer and one-to-many relationship with product
class Template(Base):
    __tablename__ = "template"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey(Customer.id))
    product = relationship("Product", uselist=False, secondary=association_table)
    quantity = Column(Numeric)

    @property
    def net_val(self):
        return self.quantity * self.product.unit_net_price

    @property
    def tax_val(self):
        return self.net_val * self.product.vat_rate

    @property
    def gross_val(self):
        return self.net_val + self.tax_val

    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.quantity = Decimal(0.0)


engine = create_engine('sqlite:///invoices.db')

# Create a session to handle updates.
Session = sessionmaker(bind=engine)
# Initalize the database if it is not already.
Base.metadata.create_all(engine)
