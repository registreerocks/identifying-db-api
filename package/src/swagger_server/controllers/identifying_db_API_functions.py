from .creation_functions import (_bulk_create_student_entries,
                                 _create_new_student_entry,
                                 _create_university_collection)

from .update_functions import _update_id


def create_university_collection(body):
    return _create_university_collection(body.get('university_name'))

def create_new_student_entry(body):
    return _create_new_student_entry(body.get('university_name'), body.get('student_data'))

def bulk_create_student_entries(body):
    return _bulk_create_student_entries(body.get('university_name'), body.get('students_data'))

def update_id(body):
    _update_id(body.get('universtiy_name'), body.get('id'))

def update_student_address():
    pass
