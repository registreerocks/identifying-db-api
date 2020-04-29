import mock
import pymongo
import pytest
from bson.objectid import ObjectId

from src.swagger_server.controllers.getter_functions import \
    _bulk_get_student_emails_by_id

@mock.patch('pymongo.collection.Collection.find_one')
def test_bulk_get_student_emails_by_id(mock_mongo_find_one):
  mock_mongo_find_one.return_value = _mock_student_data()
  assert _bulk_get_student_emails_by_id(['5d7a4090b61d9af587ffa1b4']) == ['DOEKIM001@myuct.ac.za']


def _mock_student_data():
  return {
    '_id': ObjectId('5d7a4090b61d9af587ffa1b4'),
    'first_name': 'Kim',
    'last_name': 'Doe',
    'gender': 'diverse',
    'race': 'blue',
    'address': 'Somewhere nice',
    'student_id': 'DOEKIM001'
  }