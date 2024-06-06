from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')

# Select your database and collection
db = client['ecommerce']
collection = db['products']

# Define the aggregation pipeline
pipeline = [
    {"$group": {"_id": "$category", "count": {"$sum": 1}}}
]

# Execute the aggregation query
result = collection.aggregate(pipeline)

# Print the result in a pretty format
print("Category Counts:")
for doc in result:
    print(doc)