from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

	__tablename__ = 'interests'
	entry_id = Column(Integer, primary_key=True)
	topic = Column(String)
	title = Column(String)
	rating = Column(Integer)

	def __repr__(self):
		if_good = ("If you want to learn about {}, you should look at the Wikipedia article called {}. We gave this article a rating of {} out of 10!").format(
				self.topic,
				self.title,
				self.rating)
		if self.rating < 7:
			return if_good+ " Unfortately, this article does not have a better rating. Maybe this is an article that should be replaced soon!"
		return if_good

