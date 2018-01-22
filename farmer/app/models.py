from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Table
from sqlalchemy.orm import relationship

"""
You can use the extra Flask-AppBuilder fields and Mixin's
AuditMixin will add automatic timestamp of created and modified by who
"""

assoc_Farmer_field = Table('Farmer_field', Model.metadata,
                         Column('id', Integer, primary_key=True),
                         Column('Farmer_id', Integer, ForeignKey('farmer.id')),
                         Column('field_id', Integer, ForeignKey('field.id'))
                         )


class Field(Model):
    id = Column(Integer, primary_key=True,autoincrement=True)
    kind = Column(String(450,collation='utf8_bin'))

    def __repr__(self):
        return self.kind


class Location(Model):
    id = Column(Integer, primary_key=True,autoincrement=True)
    Country = Column(String(450,collation='utf8_bin'))
    State = Column(String(450,collation='utf8_bin'))
    City = Column(String(450,collation='utf8_bin'))
    Part = Column(String(450,collation='utf8_bin'))
    village = Column(String(450,collation='utf8_bin'))

    def __repr__(self):
        return self.State + " - " + self.City + " - " + self.Part + " - " + self.village


class Farmer(Model):
    id = Column(Integer, primary_key=True,autoincrement=True)
    username = Column(String(450))
    password = Column(String(450))
    name = Column(String(450,collation='utf8_bin'))
    family = Column(String(450,collation='utf8_bin'))
    mobile = Column(String(450))
    phone = Column(String(450))
    NationalNumber = Column(String(450))
    email = Column(String(450))
    location_id = Column(Integer, ForeignKey('location.id'), nullable=False)
    Location = relationship("Location")
    fields = relationship('Field', secondary=assoc_Farmer_field, backref='Farmer')

    def __repr__(self):
        return self.name+" "+self.family


class Request(Model):
    id = Column(Integer, primary_key=True,autoincrement=True)
    Farmer_id = Column(Integer, ForeignKey('farmer.id'), nullable=False)
    Farmer_request = relationship("Farmer")


# class UserField(Model):
