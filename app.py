import pymongo
import os

MONGO_URI =  os.getenv("MONGO_URI")
# DBS_NAME =  "new_test"
# COLLECTION_NAME = "names"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print('Mongo is connected')
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGO_URI)

#coll = conn[DBS_NAME][COLLECTION_NAME]
allColl = conn["recipes"]["allergensColl"]
reciColl = conn["recipes"]["recipesColl"]

#allColl.insert({"allergens":["celery","gluten","crustaceans","eggs","fish","lupin","milk","mollucs","mustard","nuts","peanuts","sesame seeds","soya",'sulphites']})


newEntries = [{"recipe":"roasted root veg", "cuisine":"british", "section":"vegetarian"},
            {"recipe":"cramed spinash", "cuisine":"british", "section":"vegetarian"},
            {"recipe":"veggie lasagna", "cuisine":"italian", "section":"vegetarian"},
            {"recipe":"carbonara pasta", "cuisine":"italian", "section":"pasta"}]
            
#reciColl.insert_many(newEntries)

chosenNumbers = [0,3,5,10]

#document = reciColl.findOne()

# document = reciColl.find_one({'cuisine': "italian"})

# print(document)

document1 = reciColl.find({"cuisine":"italian"})


def get_record():
    try:
        document = reciColl.find_one({'recipe': 'veggie1'})
    except:
        print("Error accessing the database")
    
    if not document:
        print("")
        print("Error! No results found.")
    
    return document
    
    
def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")

                if update_doc[k] == "":
                    update_doc[k] = v
        
        try:
            reciColl.update_one(doc, {'$set': update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")
            

def get_recordAllergens():
    try:
        document = allColl.find()
    except:
        print("Error accessing the database")
    
    if not document:
        print("")
        print("Error! No results found.")
    
    return document
    
    
#mynewDocument = allColl.find_one()

# for x in mynewDocument:
#     print(x)
#print(mynewDocument)



# mynewDocument = allColl.find_one().allergens[4]
# print(mynewDocument)

findingthem = allColl.find_one({'allergens':'celery'})

for x , y in findingthem:
    print(y)
    
    
