from pymongo import MongoClient
from bson import ObjectId

MongoURL = MongoClient("mongodb://localhost:27017/")

DB = MongoURL["MyProject"]
Collection = DB["User data"]

Information2 = [
    {
        "name": "Kumar", 
        "Roll no": 15,
        "Class": "B1", 
        "Record": "standard"
    },
    {
        "name": "Arumainathan", 
        "Roll no": 19, 
        "Class": "B1", 
        "Record": "Good"
    },
    {
        "name": "SivaGnanan",
        "Roll no": 99,
        "Class": "B1,B2",
        "Record": "Donkey squad"
    }
]


def data(a):
    try:
        user = Collection.insert_many(a)
        print("Inserted document IDs:")
        for uid in user.inserted_ids:
            print(uid)
        return user.inserted_ids
    except Exception as e:
        print("Insertion failed:", e)

def getSpecificUser(userId):
    try:
        obj_id = ObjectId(userId)
        checkuser = Collection.find_one({"_id": obj_id})
        if checkuser:
            print("User found:", checkuser)
        else:
            print("User not found.")
    except Exception as e:
        print("Something went wrong:", e)


inserted_ids = data(Information2)

if inserted_ids:
    print("\nTesting getSpecificUser with a real ID:")
    getSpecificUser(str(inserted_ids[0]))  
