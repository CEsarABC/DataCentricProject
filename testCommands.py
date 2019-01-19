import pymongo
import os

MONGO_URI =  os.getenv("MONGO_URI")
DBS_NAME =  "recipes"
COLLECTION_NAME = "nesting"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print('Mongo is connected')
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGO_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]


documents = coll.find({},{'task_name':1}).limit(5)

print(documents)

''' iteration limiting results '''

def printhemall():
    tot = coll.find().count()
    lim = 5
    sheets = coll.find({},{'task_description':1}).limit(lim)
    for itm in sheets:
        tot -= 1
        print(itm)
    while tot != 0:
        entry = input('do you want more?: ')
        if entry == 'y':
            sheets = coll.find({},{'task_description':1}).skip(lim).limit(5)
            for itm1 in sheets:
                tot-=1
                print(itm1)
            lim += 5
        if tot == 0:
               break

printhemall()
                
            