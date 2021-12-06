import pymongo

def main():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["A4dbNorm"]
    col = db["tracks"]
    query = col.find({"$match":{"track_id": "$regex":"/^70/ ",{"avg(danceability)": 1})
    for doc in query:
        print(doc)    

if __name__ == "__main__":
    main()
