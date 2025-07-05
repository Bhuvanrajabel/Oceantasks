from pymongo import MongoClient

URL = MongoClient("mongodb://localhost:27017/")
DB = URL["Students"]
Collection = DB["Records"]

Information = [
    {"name": "Kevin", "marks": [99, 67, 45, 77, 56]},
    {"name": "dev", "marks": [99,45, 78, 55, 89]},
    {"name": "Bhuvan", "marks": [100, 99, 90, 67, 34]},
    {"name": "vinxav", "marks": [34, 45, 56, 67, 78]},
    {"name": "kishanth", "marks": [56, 56, 66, 45, 67]},
    {"name": "nathan", "marks": [99, 89, 75, 78, 74]},
    {"name": "Naren", "marks": [45, 34, 56, 67, 23]},
    {"name": "Mani", "marks": [35, 54, 56, 76, 12]},
    {"name": "pavi", "marks": [35, 45, 21, 84, 45]},
    {"name": "Guru", "marks": [45, 66, 98, 45, 44]}
]

def userdata(scores):
    Collection.delete_many({})  
    result = Collection.insert_many(scores)
    print("Data Created:", len(result.inserted_ids))


def add_total_marks():
    students = Collection.find()
    for student in students:
        total = sum(student["marks"])
        Collection.update_one(
            {"_id": student["_id"]},
            {"$set": {"total": total}}
        )
    print("Total marks added.")


def assign_ranks():
    sorted_students = Collection.find().sort("total", -1)
    rank = 1
    for student in sorted_students:
        Collection.update_one(
            {"_id": student["_id"]},
            {"$set": {"rank": rank}}
        )
        rank += 1
    print("Ranks assigned based on total marks.")

def display_students():
    for student in Collection.find().sort("rank", 1):
        print(f"Rank {student['rank']}: {student['name']} - Total: {student['total']}")

userdata(Information)
add_total_marks()
assign_ranks()
display_students()
