from .global_vars import IDB

def _get_students_by_trait(university_name, trait, value):
    result = list(IDB[university_name].find({trait: value}))
    if result:
        return result
    else:
        return {'ERROR': 'No matching data found.'}

def _get_students_by_trait_regex(university_name, trait, regex):
    result = list(IDB[university_name].find({trait: {"$regex": ".*"+regex+".*"}}))
    if result:
        return result
    else:
        return {'ERROR': 'No matching data found.'}
