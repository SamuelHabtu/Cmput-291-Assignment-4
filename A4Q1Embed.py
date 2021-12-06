import pymongo


def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["A4dbEmbed"]
    print(mydb.list_collection_names())
    
    myquery = {'''db.artiststracks.find
    (
        {'$where':'this.tracks.length > 1'}, 
        {'artist_id':1, 'name':1, 'num_tracks' : {'$size': '$tracks'}}
    );
    '''}
    mydoc = mycol.find(myquery)

if __name__ == "__main__":
    main()
