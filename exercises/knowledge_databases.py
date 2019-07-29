from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic, title, rating):
	article_object = Knowledge(
		topic = topic,
		title = title,
		rating = rating)
	session.add(article_object)
	session.commit()
	
# add_article("lizards", "Lizard", 6)
# add_article("sleeping", "Sleep", 10)
# add_article("Beethoven", "Ludwig van Beethoven", 9)

def query_all_articles():
	articles = session.query(Knowledge).all()
	print(articles)
	return articles

#query_all_articles()

def query_article_by_topic(topic):
	articles = session.query(Knowledge).filter_by(topic = topic).all()
	print(articles)
	return articles

#query_article_by_topic("lizards")

def query_article_by_rating(threshold):
	articles = session.query(Knowledge).filter(Knowledge.rating < threshold).all()
	print(articles)
	return articles

#query_article_by_rating(10)

def query_article_by_primary_key(key):
	article =

def delete_article_by_topic():
	pass
	
	

def delete_all_articles():
	pass

def edit_article_rating():
	pass
