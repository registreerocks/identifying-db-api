from .global_vars import IDB
from .general_functions import _generate_id

def _update_id(_id):
    doc = IDB.find_one({"_id": _id})
    if doc:
        doc = _generate_id(doc)
        IDB.insert_one(doc)
        IDB.delete_one({"_id": _id})
        return {'new_id': str(doc['_id'])}
    else:
        return {'ERROR': 'No matching document id.'}, 409

def _update_trait(trait, value, _id):
    IDB.update_one({'_id': _id}, {"$set": {trait: value}}, upsert=False)
    doc = IDB.find_one({"_id": _id})
    if doc:
        doc['_id'] = str(doc['_id'])
        return doc
    else:
        return {'ERROR': 'No matching document id.'}, 409