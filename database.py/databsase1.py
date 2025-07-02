from pymongo import MongoClient
from bson import ObjectId

# Corrected the port number to 27017
MongoURL = MongoClient("mongodb://localhost:27017/")

DB = MongoURL["MyProject"]  
Collection = DB["User data"]  

Information = {
    "name": "Baskar", 
    "Roll no": 99999,
    "Class": "A3", 
    "Record": "poor"
}

def userdetail(data):
    user = Collection.insert_one(data)
    print("Insert one data created")

userdetail(Information)


# Information2= [
# {
#     "name": "Kumar", 
#     "Roll no": 15,
#     "Class": "B1", 
#     "Record": "standard"
# },

# {
#     "name": "Arumainathan", 
#     "Roll no": 19, 
#     "Class": "B1", 
#     "Record": "Good"
# },

# {
#     "name":"SivaGnanan",
#     "Roll no":99,
#     "Class":"B1,B2",
#     "Record":"Donkey squard"

# }

# ]
# def data(a):
#     user=Collection.insert_many(a)
#     print("Insert many data created")

# data(Information2)

