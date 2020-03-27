from .authentication import requires_auth, requires_scope
from .creation_functions import (_bulk_create_student_entries,
                                 _create_new_student_entry)
from .delete_functions import _delete_student_entry
from .getter_functions import (_bulk_get_student_emails_by_id,
                               _bulk_get_students_by_id, _get_all_students,
                               _get_student_by_id, _get_students_by_trait,
                               _get_students_by_trait_regex)
from .update_functions import _update_id, _update_trait


@requires_auth
@requires_scope('admin')
def create_new_student_entry(body):
    return _create_new_student_entry(body)

@requires_auth
@requires_scope('admin')
def bulk_create_student_entries(body):
    return _bulk_create_student_entries(body)

@requires_auth
@requires_scope('student')
def update_id(body):
    return _update_id(body.get('id'))

@requires_auth
@requires_scope('student')
def update_address(body):
    return _update_trait('address', body.get('address'), body.get('id'))

@requires_auth
@requires_scope('admin')
def get_students_by_first_name(first_name):
    return _get_students_by_trait('first_name', first_name)

@requires_auth
@requires_scope('admin')
def get_students_by_last_name(last_name):
    return _get_students_by_trait('last_name', last_name)

@requires_auth
@requires_scope('admin')
def get_students_by_gender(gender):
    return _get_students_by_trait('gender', gender)

@requires_auth
@requires_scope('admin')
def get_students_by_race(race):
    return _get_students_by_trait('race', race)

@requires_auth
@requires_scope('admin', 'lecturer', 'student')
def get_students_by_student_id(student_id):
    return _get_students_by_trait('student_id', student_id)

@requires_auth
@requires_scope('admin', 'lecturer', 'student')
def get_student_by_db_id(db_id):
    return _get_student_by_id(db_id)

@requires_auth
@requires_scope('admin', 'lecturer')
def bulk_get_students_by_id(body):
    return _bulk_get_students_by_id(body.get('db_ids'))

@requires_auth
@requires_scope('admin')
def get_students_by_address(address):
    return _get_students_by_trait_regex('address', address)

@requires_auth
@requires_scope('admin')
def get_students_by_birth_year(birth_year):
    return _get_students_by_trait_regex('date_of_birth', birth_year + '-')

@requires_auth
@requires_scope('admin')
def get_students_by_birth_month(birth_month):
    return _get_students_by_trait_regex('date_of_birth', '-' + birth_month + '-')

@requires_auth
@requires_scope('admin')
def get_all_students():
    return _get_all_students()

@requires_auth
@requires_scope('student')
def delete_student_entry(id):
    return _delete_student_entry(id)

@requires_auth
@requires_scope('registree')
def bulk_get_student_emails_by_id(body):
    return _bulk_get_student_emails_by_id(body.get('db_ids'))
