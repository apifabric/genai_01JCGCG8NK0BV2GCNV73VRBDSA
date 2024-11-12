# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 12, 2024 14:31:18
# Database: sqlite:////tmp/tmp.1AEJ6xGKU1-01JCGCG8NK0BV2GCNV73VRBDSA/holiday_planner/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Destination(SAFRSBaseX, Base):
    __tablename__ = 'destination'
    _s_collection_name = 'Destination'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    country = Column(String(50))

    # parent relationships (access parent)

    # child relationships (access children)
    HolidayList : Mapped[List["Holiday"]] = relationship(back_populates="destination")
    WishlistList : Mapped[List["Wishlist"]] = relationship(back_populates="destination")



class User(SAFRSBaseX, Base):
    __tablename__ = 'user'
    _s_collection_name = 'User'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    date_joined = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    HolidayList : Mapped[List["Holiday"]] = relationship(back_populates="user")
    WishlistList : Mapped[List["Wishlist"]] = relationship(back_populates="user")
    TravelCompanionList : Mapped[List["TravelCompanion"]] = relationship(back_populates="user")



class Holiday(SAFRSBaseX, Base):
    __tablename__ = 'holiday'
    _s_collection_name = 'Holiday'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.id'))
    destination_id = Column(ForeignKey('destination.id'))
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    destination : Mapped["Destination"] = relationship(back_populates=("HolidayList"))
    user : Mapped["User"] = relationship(back_populates=("HolidayList"))

    # child relationships (access children)
    AccommodationList : Mapped[List["Accommodation"]] = relationship(back_populates="holiday")
    ActivityList : Mapped[List["Activity"]] = relationship(back_populates="holiday")
    EventList : Mapped[List["Event"]] = relationship(back_populates="holiday")
    PackingListList : Mapped[List["PackingList"]] = relationship(back_populates="holiday")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="holiday")
    TransportList : Mapped[List["Transport"]] = relationship(back_populates="holiday")
    TravelCompanionList : Mapped[List["TravelCompanion"]] = relationship(back_populates="holiday")
    TravelInsuranceList : Mapped[List["TravelInsurance"]] = relationship(back_populates="holiday")



class Wishlist(SAFRSBaseX, Base):
    __tablename__ = 'wishlist'
    _s_collection_name = 'Wishlist'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.id'))
    destination_id = Column(ForeignKey('destination.id'))
    preferred_travel_date = Column(DateTime)

    # parent relationships (access parent)
    destination : Mapped["Destination"] = relationship(back_populates=("WishlistList"))
    user : Mapped["User"] = relationship(back_populates=("WishlistList"))

    # child relationships (access children)



class Accommodation(SAFRSBaseX, Base):
    __tablename__ = 'accommodation'
    _s_collection_name = 'Accommodation'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    holiday_id = Column(ForeignKey('holiday.id'))
    name = Column(String(100))
    address = Column(String(200))
    cost_per_night = Column(Integer)

    # parent relationships (access parent)
    holiday : Mapped["Holiday"] = relationship(back_populates=("AccommodationList"))

    # child relationships (access children)



class Activity(SAFRSBaseX, Base):
    __tablename__ = 'activity'
    _s_collection_name = 'Activity'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    holiday_id = Column(ForeignKey('holiday.id'))
    name = Column(String(100))
    cost = Column(Integer)

    # parent relationships (access parent)
    holiday : Mapped["Holiday"] = relationship(back_populates=("ActivityList"))

    # child relationships (access children)



class Event(SAFRSBaseX, Base):
    __tablename__ = 'event'
    _s_collection_name = 'Event'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    holiday_id = Column(ForeignKey('holiday.id'))
    name = Column(String(100))
    date = Column(DateTime)

    # parent relationships (access parent)
    holiday : Mapped["Holiday"] = relationship(back_populates=("EventList"))

    # child relationships (access children)



class PackingList(SAFRSBaseX, Base):
    __tablename__ = 'packing_list'
    _s_collection_name = 'PackingList'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    holiday_id = Column(ForeignKey('holiday.id'))
    item_name = Column(String(50))
    quantity = Column(Integer)

    # parent relationships (access parent)
    holiday : Mapped["Holiday"] = relationship(back_populates=("PackingListList"))

    # child relationships (access children)



class Review(SAFRSBaseX, Base):
    __tablename__ = 'review'
    _s_collection_name = 'Review'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    holiday_id = Column(ForeignKey('holiday.id'))
    rating = Column(Integer)
    comment = Column(String(500))

    # parent relationships (access parent)
    holiday : Mapped["Holiday"] = relationship(back_populates=("ReviewList"))

    # child relationships (access children)



class Transport(SAFRSBaseX, Base):
    __tablename__ = 'transport'
    _s_collection_name = 'Transport'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    holiday_id = Column(ForeignKey('holiday.id'))
    type = Column(String(50))
    cost = Column(Integer)

    # parent relationships (access parent)
    holiday : Mapped["Holiday"] = relationship(back_populates=("TransportList"))

    # child relationships (access children)



class TravelCompanion(SAFRSBaseX, Base):
    __tablename__ = 'travel_companion'
    _s_collection_name = 'TravelCompanion'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    holiday_id = Column(ForeignKey('holiday.id'))
    user_id = Column(ForeignKey('user.id'))

    # parent relationships (access parent)
    holiday : Mapped["Holiday"] = relationship(back_populates=("TravelCompanionList"))
    user : Mapped["User"] = relationship(back_populates=("TravelCompanionList"))

    # child relationships (access children)



class TravelInsurance(SAFRSBaseX, Base):
    __tablename__ = 'travel_insurance'
    _s_collection_name = 'TravelInsurance'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    holiday_id = Column(ForeignKey('holiday.id'))
    provider_name = Column(String(100))
    policy_number = Column(String(50))
    cost = Column(Integer)

    # parent relationships (access parent)
    holiday : Mapped["Holiday"] = relationship(back_populates=("TravelInsuranceList"))

    # child relationships (access children)
