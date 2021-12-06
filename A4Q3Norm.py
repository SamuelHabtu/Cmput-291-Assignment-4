import pymongo

def main()
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["A4dbNorm"]
    print(mydb.list_collection_names())
    mycol = mydb["tracks"]
    myquery = {'''db.tracks.aggregate(
    [
        { $group: {_id:"$artist_ids", 
        total_length: {$sum: "$duration"}, 
        artist_ids:{$first :"$artist_ids"} } }
    ]
    );
    '''}
    mydoc = mycol.find(myquery)
    

if __name__ == "__main__":
    main()
