from .general_functions import _generate_id
from .global_vars import IDB

def _create_new_student_entry(student_data):
    student_data = _generate_id(student_data)
    return str(IDB.insert_one(student_data).inserted_id)

def _bulk_create_student_entries(students_data):
    students_data = [_generate_id(i) for i in students_data]
    return [str(i) for i in IDB.insert_many(students_data).inserted_ids]
