import os

from setuptools import setup, find_packages

setup(
   name='identifying_db_API',
   version='0.1.0',
   maintainer='Sabine Bertram',
   maintainer_email='sabine.bertram@mailbox.org',
   package_dir={'': 'src'},
   packages=find_packages('src'),
   package_data={'swagger_server': ['swagger/swagger.yaml']},

   install_requires=['Flask==1.0.2', 'flask_cors', 'connexion >= 1.1.9', 'pymongo', 'pytest', 'mock'],
)
