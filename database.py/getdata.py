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
        "name":"SivaGnanan",
        "Roll no":99,
        "Class":"B1,B2",
        "Record":"Donkey squard"
    }
]

# def data(a):
#     user = Collection.insert_many(a)
#     print("Insert many data created")

# data(Information2)

# def getAllData():
#     userData = Collection.find({})
#     for i in userData:
#         print(i)

# getAllData()
def getDeleteUser(userId):
    try:
        checkuser = Collection.find_one_and_delete({"_id":ObjectId(userId)})
        if checkuser:
            print("user data deleted")
        else:
            print("user is not found")
    except Exception as e:
        print("something went wrong",e)

getDeleteUser("685ce0bb40969e0c9b0db3e1")