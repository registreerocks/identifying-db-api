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

def _update_trait(university_name, trait, value, _id):
    IDB[university_name].update_one({'_id': ObjectId(_id)}, {"$set": {trait: value}}, upsert=False)
    doc = IDB[university_name].find_one({"_id": ObjectId(_id)})
    if doc:
        doc['_id'] = str(doc['_id'])
        return doc
    else:
        return {'ERROR': 'No matching document id.'}