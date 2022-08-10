import pymongo
client = pymongo.MongoClient("mongodb+srv://guruswamy:nags1619@cluster0.qdb9ajk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":" guruswamy",
    "email":"guruswamy1623@gmail.com",
    "surname":"na"
}
db1 = client['mongotest']
coll=db1['test']
coll.insert_one(d )