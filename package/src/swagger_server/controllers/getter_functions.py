from .global_vars import IDB


def _get_student_by_id(_id):
    result = IDB.find_one({'_id': _id})
    if result:
        result['_id'] = str(result['_id'])
        return result
    else:
        return {'ERROR': 'No matching data found.'}, 409

def _bulk_get_students_by_id(_ids):
    students = dict()
    for _id in _ids:
        students[_id] = _get_student_by_id(_id)
    return students

def _get_students_by_trait(trait, value):
    result = list(IDB.find({trait: value}))
    if result:
        return _stringify_object_id(result)
    else:
        return {'ERROR': 'No matching data found.'}, 409

def _get_students_by_trait_regex(trait, regex):
    result = list(IDB.find({trait: {"$regex": ".*"+regex+".*"}}))
    if result:
        return _stringify_object_id(result)
    else:
        return {'ERROR': 'No matching data found.'}, 409

def _get_all_students():
    result = list(IDB.find({}))
    if result:
        return _stringify_object_id(result)
    else:
        return {'ERROR': 'No matching data found.'}, 409

def _stringify_object_id(result):
    stringified_result = []
    for element in result:
        element['_id'] = str(element['_id'])
        stringified_result.append(element)
    return stringified_result

def _bulk_get_student_emails_by_id(_ids):
    students = []
    for _id in _ids:
        students.append(_get_student_by_id(_id)['student_id'] + '@myuct.ac.za')
    return students