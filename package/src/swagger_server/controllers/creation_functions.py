import hashlib
import json
import random
import time

from .global_vars import IDB


def _create_university_collection(university_name):
    IDB[university_name]
    return True

def _create_new_student_entry(university_name, student_data):
    student_data = _generate_id(student_data)
    return str(IDB[university_name].insert_one(student_data).inserted_id)

def _bulk_create_student_entries(university_name, students_data):
    students_data = [_generate_id(i) for i in students_data]
    return [str(i) for i in IDB[university_name].insert_many(students_data).inserted_ids]

def _generate_id(student_data):
    t = time.time()
    r = random.randint(1,101)
    student_string = json.dumps(student_data)
    hash_object = hashlib.sha256((student_string + str(t) + str(r)).encode())
    student_data['_id'] = hash_object.hexdigest()
    return student_data
