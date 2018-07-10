from .creation_functions import (_bulk_create_student_entries,
                                 _create_new_student_entry,
                                 _create_university_collection)
from .getter_functions import (_get_all_students, _get_student_by_id,
                               _get_students_by_trait,
                               _get_students_by_trait_regex)
from .update_functions import _update_id, _update_trait


def create_university_collection(body):
    return _create_university_collection(body.get('university_name'))

def create_new_student_entry(body):
    return _create_new_student_entry(body.get('university_name'), body.get('student_data'))

def bulk_create_student_entries(body):
    return _bulk_create_student_entries(body.get('university_name'), body.get('students_data'))

def update_id(body):
    return _update_id(body.get('university_name'), body.get('id'))

def update_address(body):
    return _update_trait(body.get('university_name'), 'address', body.get('address'), body.get('id'))

def get_students_by_first_name(university_name, first_name):
    return _get_students_by_trait(university_name, 'first_name', first_name)

def get_students_by_last_name(university_name, last_name):
    return _get_students_by_trait(university_name, 'last_name', last_name)

def get_students_by_gender(university_name, gender):
    return _get_students_by_trait(university_name, 'gender', gender)

def get_students_by_race(university_name, race):
    return _get_students_by_trait(university_name, 'race', race)

def get_students_by_student_id(university_name, student_id):
    return _get_students_by_trait(university_name, 'student_id', student_id)

def get_students_by_db_id(university_name, db_id):
    return _get_student_by_id(university_name, db_id)

def get_students_by_address(university_name, address):
    return _get_students_by_trait_regex(university_name, 'address', address)

def get_students_by_birth_year(university_name, birth_year):
    return _get_students_by_trait_regex(university_name, 'date_of_birth', birth_year + '-')

def get_students_by_birth_month(university_name, birth_month):
    return _get_students_by_trait_regex(university_name, 'date_of_birth', '-' + birth_month + '-')

def get_all_students(university_name):
    return _get_all_students(university_name)
