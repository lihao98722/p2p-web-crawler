from pymongo import MongoClient

client = MongoClient("localhost:27017")
db = client.test
WEB_PAGES = db.web_pages