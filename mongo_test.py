import pymongo

conn = pymongo.MongoClient('localhost', 27017)

db = conn['maoyandb']

myset = db['myset']

myset.insert_one({'': ''})
