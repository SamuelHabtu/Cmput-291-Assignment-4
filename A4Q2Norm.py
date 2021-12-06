import pymongo

def main():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["A4dbNorm"]
    col = db["tracks"]
    query = col.aggregate([{"$match":{"track_id":{ "$regex":"/^70/ "}} }, {"$group":{"_id":"null", "avg_danceability":{"$avg":"$danceability"}}}])

    for doc in list(query):
        print(doc)    

if __name__ == "__main__":
    main()
