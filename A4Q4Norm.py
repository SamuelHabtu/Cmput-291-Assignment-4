import pymongo

def main()
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["A4dbNorm"]
    print(mydb.list_collection_names())
    mycol = mydb["tracks"]
    myquery = {'''db.artists.aggregate([
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

]); 
                 '''}
    mydoc = mycol.find(myquery)
    

if __name__ == "__main__":
    main()
