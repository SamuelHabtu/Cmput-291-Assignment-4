def main():
    import pymongo
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["A4dbNorm"]
    mycol = mydb[tracks]
    myquery = {db.artists.find({'$where':'this.tracks.length > 1'}, {'artist_id':1, 'name':1, 'num_tracks' : {'$size': '$tracks'}})}
    mydoc = mycol.find(myquery)
    pass

if __name__ == "__main__":
    main()
