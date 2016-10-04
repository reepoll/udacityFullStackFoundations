import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import	relationship
from sqlalchemy import create_engine

Base = declarative_base()

# Create class code

# Restaurant Class
class Restaurant(Base):
	"""docstring for ClassName"""
	__tablename__ = 'restaurant'

	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	


# MenuItem Class
class MenuItem(Base):
	__tablename__ = 'menu_item'

	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	course = Column(String(250))
	description = Column(String(250))
	price = Column(String(8))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)


engine = create_engine('sqlite:///retaurantmenu.db')

Base.metadata.create_all(engine)


