from pymongo import MongoClient

# ✅ Use correct port: 27017
MongoURL = MongoClient("mongodb://localhost:27017/")

# Connect to database and collection
DB = MongoURL["Stud record"]
Collection = DB["Mydata"]

# Your data
Information = [
    {
        "name": "Guna",
        "mobile no": "48993453457",
        "Marks": [21, 32, 43, 54, 64],
        "Address": "jdhidfhuias",
        "email": "sdfhsidhfifuishdufhdu"
    },
    {
        "name": "raju",
        "Mobile no": "23847239423",
        "Marks": [32, 43, 65, 76, 86],
        "Address": "osdkflsadkfl",
        "email": "adkfjad"
    },
    {
        "name": "ramu",
        "Mobile no": "384374",
        "Marks": [21, 21, 12, 43, 54],
        "Address": "sdfsdf",
        "email": "lkji"
    },
    {
        "name": "ragu",
        "Mobile no": "665656564",
        "Marks": [21, 43, 65, 76, 98],
        "Address": "sdfhsdfh",
        "email": "sdfjdflja"
    },
    {
        "name": "dad",
        "Mobile no": "38472374",
        "Marks": [22, 33, 44, 55, 66],
        "Address": "adkfasdjkfha",
        "email": "sdfhasdfhas"
    },
    {
        "name": "nani",
        "Mobile no": "23431",
        "Marks": [22, 11, 44, 77, 88],
        "Address": "sadfhdiofh",
        "email": "sddfhsdfhas"
    }
]

# Insert data function
def data(a):
    try:
        user = Collection.insert_many(a)
        print("Insert many data created")
        print("Inserted IDs:")
        for uid in user.inserted_ids:
            print(uid)
    except Exception as e:
        print("Error inserting documents:", e)

# Call function
data(Information)
