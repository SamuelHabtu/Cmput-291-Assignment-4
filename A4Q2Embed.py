import pymongo


def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["A4dbEmbed"]
    print(mydb.list_collection_names())
    
    myquery = {'''db.artiststracks.aggregate([
              {$unwind: "$tracks" },     
              {$match:{"tracks.track_id":{ $regex:/^70/ }} }, 
              {$group:{_id:null, avg_danceability:{$avg:"$tracks.danceability"}}}]);
    '''}
    mydoc = mycol.find(myquery)

if __name__ == "__main__":
    main()
