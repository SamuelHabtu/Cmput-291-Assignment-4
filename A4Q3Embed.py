import pymongo

def main()
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["A4dbNorm"]
    
    myquery = {'''db.artiststracks.aggregate(
    [
    { $unwind: "$tracks" },
        { $group: 
        {
            _id:"$artist_id", 
            total_length: {$sum: "$tracks.duration"}, 
            artist_ids:{$first :"$artist_id"} 
        } 
    }
    ]
);
    '''}
    mydoc = mycol.find(myquery)
    

if __name__ == "__main__":
    main()
