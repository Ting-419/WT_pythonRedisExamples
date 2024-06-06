from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')

# Select your database and collection
db = client['ecommerce']
collection = db['products']

# documents = collection.find()
# for document in documents:
#     print(document)

# documents = collection.find({'category': 'Electronics'}).sort('price')
# documents = collection.find({'category': 'Electronics'}).sort('stock')
documents = collection.find({'$and': [{'price': {'$lt': 200}}, {'stock': {'$lt': 35}}]}).sort('stock')

for document in documents:
    print(document)
