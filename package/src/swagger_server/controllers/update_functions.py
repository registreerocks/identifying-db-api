from bson.objectid import ObjectId
from .global_vars import IDB

def _update_id(university_name, _id):
    doc = IDB[university_name].find_one({"_id": ObjectId(_id)})
    if doc:
        doc['_id'] = ObjectId()
        IDB[university_name].insert_one(doc)
        IDB[university_name].delete_one({"_id": ObjectId(_id)})
        return {'new_id': str(doc['_id'])}
    else:
        return {'ERROR': 'No matching document id.'}

def _update_address(university_name, address, _id):
    IDB[university_name].update_one({'_id': _id}, {"$set": {"address": address}}, upsert=False)
    doc = IDB[university_name].find_one({"_id": ObjectId(_id)})
    if doc:
        return doc
    else:
        return {'ERROR': 'No matching document id.'}