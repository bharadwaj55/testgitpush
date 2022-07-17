import pymongo
client = pymongo.MongoClient("mongodb://ineuron:mongodb123@cluster0-shard-00-00.fj0eh.mongodb.net:27017,cluster0-shard-00-01.fj0eh.mongodb.net:27017,cluster0-shard-00-02.fj0eh.mongodb.net:27017/?ssl=true&replicaSet=atlas-wfsyum-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name":"Bharadwaj",
    "email" : "Bharadwaj@ineuron.ai",
    "surname" : "vedula"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )

