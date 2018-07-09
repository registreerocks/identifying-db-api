from .global_vars import IDB

def _create_university_collection(university_name):
    IDB[university_name]

def _create_new_student_entry(university_name, student_data):
    return IDB[university_name].insert_one(student_data).inserted_id

def _bulk_create_student_entries(university_name, students_data):
    return IDB[university_name].insert_many(students_data).inserted_ids