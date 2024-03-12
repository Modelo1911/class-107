import pymongo
import certifi


con_str = "mongodb+srv://guillermoescobar11:Glockformula85@cluster107.dlcb2nq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster107"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("Cluster107test")