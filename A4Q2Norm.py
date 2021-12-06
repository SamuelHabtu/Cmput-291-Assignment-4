import pymongo

def main()
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["A4dbNorm"]
    print(mydb.list_collection_names())
    mycol = mydb["tracks"]
    myquery = {'''db.tracks.aggregate([{$match:{track_id:{ $regex:/^70/ }} }, {$group:{_id:'', avg_danceability:{$avg:"$danceability"}}}]);'''}
    mydoc = mycol.find(myquery)
    

if __name__ == "__main__":
    main()
