import pymongo


import pymongo

def main():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["A4dbEmbed"]
    col = db["artiststracks"]
    query = db.artists.aggregate([
            { $lookup:
            {
            from: "tracks",
            localField: "artist_id",
            foreignField: "artist_ids",
            as: "Tracks"
            }
            },
            { $match:
            {
            release_date:{$gt: new ISODate("1950-01-01T:23:59:59"}
            },
            { $group: { _id:"$_id", name: "$name", t_name:"$Tracks.name"}

            ])

    for doc in query:
            print(doc)

if __name__ == "__main__":
    main()
