import pymongo


import pymongo

def main():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["A4dbEmbed"]
    col = db["artiststracks"]
    query = col.aggregate()
    for doc in query:
            print(doc)

if __name__ == "__main__":
    main()
