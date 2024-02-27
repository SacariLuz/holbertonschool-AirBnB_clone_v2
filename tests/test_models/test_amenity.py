#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from os import environ
import unittest

class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db', "test for DBStorage")
    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
