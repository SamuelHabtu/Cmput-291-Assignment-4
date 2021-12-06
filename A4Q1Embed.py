import pymongo

def main():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["A4dbEmbed"]
    col = database["artiststracks"]
    query = col.find(
        {'$where':'this.tracks.length > 1'}, 
        {'artist_id':1, 'name':1, 'num_tracks' : {'$size': '$tracks'}})
    
    for doc in query:
        print(doc)

if __name__ == "__main__":
    main()
