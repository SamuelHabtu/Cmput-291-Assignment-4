import pymongo

def main():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["A4dbEmbed"]
    col = db["artiststracks"]
    query = col.aggregate([{"$unwind": "$tracks"}, {"$group": {"_id": "$artist_id", "total_length": {"$sum": "$tracks.duration"}, "artist_ids": {"$first": "$artist_id"}}}])

    for doc in query:
            print(doc)

if __name__ == "__main__":
    main()
