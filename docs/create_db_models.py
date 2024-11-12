# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    date_joined = Column(DateTime)

    """description: Users participating in holiday planning."""


class Destination(Base):
    __tablename__ = 'destination'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    country = Column(String(50))

    """description: Holiday destinations available for planning."""


class Holiday(Base):
    __tablename__ = 'holiday'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    destination_id = Column(Integer, ForeignKey('destination.id'))
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    """description: Details of each holiday planned by users."""


class Accommodation(Base):
    __tablename__ = 'accommodation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    holiday_id = Column(Integer, ForeignKey('holiday.id'))
    name = Column(String(100))
    address = Column(String(200))
    cost_per_night = Column(Integer)

    """description: Accommodations reserved for holidays."""


class Activity(Base):
    __tablename__ = 'activity'

    id = Column(Integer, primary_key=True, autoincrement=True)
    holiday_id = Column(Integer, ForeignKey('holiday.id'))
    name = Column(String(100))
    cost = Column(Integer)

    """description: Planned activities during holidays."""


class Transport(Base):
    __tablename__ = 'transport'

    id = Column(Integer, primary_key=True, autoincrement=True)
    holiday_id = Column(Integer, ForeignKey('holiday.id'))
    type = Column(String(50))
    cost = Column(Integer)

    """description: Transportations used during holidays."""


class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True, autoincrement=True)
    holiday_id = Column(Integer, ForeignKey('holiday.id'))
    rating = Column(Integer)
    comment = Column(String(500))

    """description: Reviews and ratings of holidays by users."""


class Wishlist(Base):
    __tablename__ = 'wishlist'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    destination_id = Column(Integer, ForeignKey('destination.id'))
    preferred_travel_date = Column(DateTime)

    """description: Users' wishlist of destinations and travel plans."""


class TravelCompanion(Base):
    __tablename__ = 'travel_companion'

    id = Column(Integer, primary_key=True, autoincrement=True)
    holiday_id = Column(Integer, ForeignKey('holiday.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    """description: Travel companions for each holiday."""


class TravelInsurance(Base):
    __tablename__ = 'travel_insurance'

    id = Column(Integer, primary_key=True, autoincrement=True)
    holiday_id = Column(Integer, ForeignKey('holiday.id'))
    provider_name = Column(String(100))
    policy_number = Column(String(50))
    cost = Column(Integer)

    """description: Travel insurance details for holidays."""


class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True, autoincrement=True)
    holiday_id = Column(Integer, ForeignKey('holiday.id'))
    name = Column(String(100))
    date = Column(DateTime)

    """description: Special events planned during holidays."""


class PackingList(Base):
    __tablename__ = 'packing_list'

    id = Column(Integer, primary_key=True, autoincrement=True)
    holiday_id = Column(Integer, ForeignKey('holiday.id'))
    item_name = Column(String(50))
    quantity = Column(Integer)

    """description: Packing list items for holidays."""


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

from datetime import date

user1 = User(username='john_doe', email='john@example.com', date_joined=date(2022, 1, 15))
user2 = User(username='jane_smith', email='jane@example.com', date_joined=date(2023, 2, 20))
user3 = User(username='alice_brown', email='alice@example.com', date_joined=date(2021, 11, 5))
user4 = User(username='bob_jones', email='bob@example.com', date_joined=date(2023, 3, 10))


destination1 = Destination(name='Paris', country='France')
destination2 = Destination(name='Rome', country='Italy')
destination3 = Destination(name='Tokyo', country='Japan')
destination4 = Destination(name='New York', country='USA')


holiday1 = Holiday(user_id=1, destination_id=1, start_date=date(2024, 6, 1), end_date=date(2024, 6, 15))
holiday2 = Holiday(user_id=2, destination_id=2, start_date=date(2023, 7, 10), end_date=date(2023, 7, 20))
holiday3 = Holiday(user_id=3, destination_id=3, start_date=date(2023, 8, 25), end_date=date(2023, 9, 10))
holiday4 = Holiday(user_id=4, destination_id=4, start_date=date(2024, 5, 5), end_date=date(2024, 5, 15))


accommodation1 = Accommodation(holiday_id=1, name='Hotel Parisien', address='123 Paris St', cost_per_night=200)
accommodation2 = Accommodation(holiday_id=2, name='Rome Inn', address='456 Rome Rd', cost_per_night=150)
accommodation3 = Accommodation(holiday_id=3, name='Tokyo Lodge', address='789 Tokyo Ave', cost_per_night=250)
accommodation4 = Accommodation(holiday_id=4, name='NYC Hotel', address='321 NY Blvd', cost_per_night=300)


activity1 = Activity(holiday_id=1, name='Eiffel Tower Visit', cost=50)
activity2 = Activity(holiday_id=2, name='Colosseum Tour', cost=80)
activity3 = Activity(holiday_id=3, name='Mt. Fuji Hike', cost=100)
activity4 = Activity(holiday_id=4, name='Statue of Liberty Visit', cost=60)


transport1 = Transport(holiday_id=1, type='Flight', cost=500)
transport2 = Transport(holiday_id=2, type='Train', cost=200)
transport3 = Transport(holiday_id=3, type='Bus', cost=100)
transport4 = Transport(holiday_id=4, type='Car Rental', cost=300)


review1 = Review(holiday_id=1, rating=5, comment='Amazing experience!')
review2 = Review(holiday_id=2, rating=4, comment='Beautiful sights.')
review3 = Review(holiday_id=3, rating=5, comment='Loved every minute!')
review4 = Review(holiday_id=4, rating=3, comment='Good, but could be better.')


wishlist1 = Wishlist(user_id=1, destination_id=3, preferred_travel_date=date(2024, 11, 5))
wishlist2 = Wishlist(user_id=2, destination_id=4, preferred_travel_date=date(2022, 6, 15))
wishlist3 = Wishlist(user_id=3, destination_id=1, preferred_travel_date=date(2023, 9, 20))
wishlist4 = Wishlist(user_id=4, destination_id=2, preferred_travel_date=date(2025, 4, 10))


travel_companion1 = TravelCompanion(holiday_id=1, user_id=2)
travel_companion2 = TravelCompanion(holiday_id=2, user_id=3)
travel_companion3 = TravelCompanion(holiday_id=3, user_id=4)
travel_companion4 = TravelCompanion(holiday_id=4, user_id=1)


travel_insurance1 = TravelInsurance(holiday_id=1, provider_name='Safe Travels', policy_number='ST12345', cost=100)
travel_insurance2 = TravelInsurance(holiday_id=2, provider_name='Secure Trip', policy_number='ST67890', cost=80)
travel_insurance3 = TravelInsurance(holiday_id=3, provider_name='Travel Guard', policy_number='TGD7890', cost=150)
travel_insurance4 = TravelInsurance(holiday_id=4, provider_name='Holiday Safe', policy_number='HS6789', cost=120)


event1 = Event(holiday_id=1, name='Paris Jazz Festival', date=date(2024, 6, 5))
event2 = Event(holiday_id=2, name='Rome Fashion Week', date=date(2023, 7, 15))
event3 = Event(holiday_id=3, name='Tokyo Anime Expo', date=date(2023, 8, 30))
event4 = Event(holiday_id=4, name='NYC Marathon', date=date(2024, 5, 10))


packing_list1 = PackingList(holiday_id=1, item_name='Sunglasses', quantity=2)
packing_list2 = PackingList(holiday_id=2, item_name='Walking shoes', quantity=1)
packing_list3 = PackingList(holiday_id=3, item_name='Travel Adapter', quantity=2)
packing_list4 = PackingList(holiday_id=4, item_name='Camera', quantity=1)


session.add_all([user1, user2, user3, user4, destination1, destination2, destination3, destination4, holiday1, holiday2, holiday3, holiday4, accommodation1, accommodation2, accommodation3, accommodation4, activity1, activity2, activity3, activity4, transport1, transport2, transport3, transport4, review1, review2, review3, review4, wishlist1, wishlist2, wishlist3, wishlist4, travel_companion1, travel_companion2, travel_companion3, travel_companion4, travel_insurance1, travel_insurance2, travel_insurance3, travel_insurance4, event1, event2, event3, event4, packing_list1, packing_list2, packing_list3, packing_list4])
session.commit()
