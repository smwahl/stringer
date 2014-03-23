from pymongo import MongoClient, ASCENDING
client = MongoClient('localhost', 27017)

db = client.feed_db     # a database
articles = db.articles  # a collection

article = { "author": "Rena",
            "text": "This is a test!" }

article_id = articles.insert(article)
print "article_id = ", article_id

print "db.collection_names() = ", db.collection_names()

print "one article: ", articles.find_one()

print "article with article_id: ", articles.find_one({"_id": article_id})

# set an index
articles.create_index([("author", ASCENDING)])

#use the index
print "The cursor after setting an index should be BtreeCursor"
print articles.find({"author": "Rena"}).sort("author").explain()["cursor"]
