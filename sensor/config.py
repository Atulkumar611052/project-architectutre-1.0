import pymongo
import pandas as pd 
import json
from dataclasses import dataclass
# Provide the mongodb localhost url to connect python to mongodb.
import os

@dataclass
class Environmentvariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_access_seceret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")