from .global_vars import IDB

def _delete_student_entry(_id):
    doc = IDB.find_one({"_id": _id})
    if doc:
        IDB.delete_one({"_id": _id})
        return True
    else:
        return {'ERROR': 'No matching document id.'}, 409