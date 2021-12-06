import pymongo

def main():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["A4dbNorm"]
    print(db.list_collection_names())
    col = db["tracks"]
    query = col.aggregate([{ "$group": {"_id":"$artist_ids", "total_length": {"$sum": "$duration"}, "artist_ids":{"$first" :"$artist_ids"} } }])

    for doc in query:
            print(doc)

if __name__ == "__main__":
    main()
