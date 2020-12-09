from os import environ as env

import pymongo

def _health_check():
    try:
        client = pymongo.MongoClient(
            'mongodb://mongodb:27017/', 
            username=env.get('MONGO_USERNAME'), 
            password=env.get('MONGO_PASSWORD'),
            serverSelectionTimeoutMS=1
        )
        client.server_info()
        return {
            "status": "ok",
            "info": {
                "mongo-identify": {
                    "status": "up"
                }
            },
            "error": {},
            "details": {
                "mongo-identify": {
                    "status": "up"
                }
            }
        }, 200
    except pymongo.errors.ServerSelectionTimeoutError as err:
        return {
            "status": "error",
            "info": {},
            "error": {
                "mongo-identify": {
                    "status": "down"
                }
            },
            "details": {
                "mongo-identify": {
                    "status": "down"
                }
            }
        }, 503