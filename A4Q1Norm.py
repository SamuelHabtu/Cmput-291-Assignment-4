import pymongo


def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["A4dbNorm"]
    print(mydb.list_collection_names())
    mycol = mydb["tracks"]
    myquery = {'''db.artists.group({

    "key":{
            "artists": true
    },
    "initial": {
            "sumtracks": 0
    },
    "reduce": function( obj , prev ){



            prev.sumtracks  = prev.sumtracks  + obj.tracks  - 0;

    },
    "finalize": function( prev ){

    },
    "cond": {
    
    }

    });
    '''}
    mydoc = mycol.find(myquery)

if __name__ == "__main__":
    main()
