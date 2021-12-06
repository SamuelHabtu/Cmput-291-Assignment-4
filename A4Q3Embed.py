import pymongo

def main()
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["A4dbNorm"]
    
    myquery = {'''db.mydb.aggregate(
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
