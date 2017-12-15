from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Table
from sqlalchemy.orm import relationship

"""
You can use the extra Flask-AppBuilder fields and Mixin's
AuditMixin will add automatic timestamp of created and modified by who
"""

# assoc_users_field = Table('user_field', Model.metadata,
#                          Column('id', Integer, primary_key=True),
#                          Column('user_id', Integer, ForeignKey('user.id')),
#                          Column('field_id', Integer, ForeignKey('field.id'))
#                          )


class Field(Model):
    id = Column(Integer, primary_key=True)
    kind = Column(String(450))

    def __repr__(self):
        return self.kind


class Location(Model):
    id = Column(Integer, primary_key=True)
    Country = Column(String(450))
    State = Column(String(450))
    City = Column(String(450))
    Part = Column(String(450))
    village = Column(String(450))

    def __repr__(self):
        return self.State + " - " + self.City + " - " + self.Part + " - " + self.village


class User(Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(450))
    password = Column(String(450))
    name = Column(String(450))
    family = Column(String(450))
    mobile = Column(String(450))
    phone = Column(String(450))
    NationalNumber = Column(String(450))
    email = Column(String(450))
    location_id = Column(Integer, ForeignKey('location.id'), nullable=False)
    Location = relationship("Location")
    # fields = relationship('Field', secondary=assoc_users_field, backref='User')

    def __repr__(self):
        return self.name+" "+self.family


class Request(Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_request = relationship("User")


# class UserField(Model):
