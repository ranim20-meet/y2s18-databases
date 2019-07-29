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
# add_article("Beethoven", "Ludwig van Beethoven", 8)
# add_article("lizards", "Lizard", 7)
# add_article("sleeping", "Sleep", 9)
# add_article("Beethoven", "Ludwig van Beethoven", 5)
# add_article("lizards", "Lizard", 4)
# add_article("sleeping", "Sleep", 7)
# add_article("Beethoven", "Ludwig van Beethoven", 8)


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
	article = session.query(Knowledge).filter_by(entry_id = key).first()
	print(article)
	return article

def delete_article_by_topic(topic):
	to_delete = session.query(Knowledge).filter_by(topic = topic).delete()
	session.commit()

# delete_article_by_topic("lizards")
# query_all_articles()
	
def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

# delete_all_articles()
# query_all_articles()

def edit_article_rating(article_title,  update_rating):
	article_to_update = session.query(Knowledge).filter_by(title = article_title).first()
	article_to_update.rating = update_rating
	session.commit()

# edit_article_rating("Lizard", 7)
# query_article_by_topic("lizards")

def delete_article_by_rating(threshold):
	to_delete = session.query(Knowledge).filter(threshold > Knowledge.rating).delete()
	session.commit()

# delete_article_by_rating(8)
# query_all_articles()

def query_top_five():
	entries = session.query(Knowledge).all()
	def sorter(entry):
		return -entry.rating
	entries.sort(key = sorter)
	'''
	for entry in entries:
		rate = entry.rating
		if len(top_five) < 5:
			top_five.append(entry)
		else:
			for ent in top_five:
				if rate > ent.rating:
					top_five.append(entry)
					top_five.remove(ent)
	return top_five
	'''
	return entries[:5]
print(query_top_five())


