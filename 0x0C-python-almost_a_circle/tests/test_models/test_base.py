#!/usr/bin/python3
"""Unittest eviroment for Base Class"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for base"""

    @classmethod
    def setUpClass(cls):
        """Set of attributes for class Base"""
        Base.__nb_objects = 0
        cls.base1 = Base()
        cls.base2 = Base()
        cls.base3 = Base(12)
        cls.base4 = Base(1.2)
        cls.base5 = Base("cero")
        cls.rectangle1 = (20, 7, 1, 10)
        cls.rectangle2 = (3, 6)

    def test_001_create(self):
        """Creates Base class"""
        self.assertTrue(self.base1)

    def test_002_create(self):
        """Base with a specified id"""
        self.base1.id = 5
        self.assertEqual(self.base1.id, 5)

    def test_003_id(self):
        """Revising if incrementing right"""
        self.base1.id = 1
        test = self.base1.id
        test2 = self.base2.id
        self.assertEqual(test, test2 - 1)

    def test_004_id(self):
        """Additional incrementing tests"""
        test = self.base1.id
        test2 = self.base2.id
        test3 = self.base3.id
        self.assertEqual(test, test2 - 1)
        self.assertEqual(test3, 12)

    def test_005_id(self):
        """Rev. ids"""
        self.assertTrue(self.base1, 1)
        self.assertTrue(self.base2, 2)
        self.assertTrue(self.base3, 22)
        self.assertTrue(self.base4, 2.2)
        self.assertTrue(self.base5, "two")

    def test_006_Jsstr(self):
        """Revisin the JSON string"""
        o2_1 = [{"ray": 1, "yo": "hol"}]
        r2_1 = Base.to_json_string(o2_1)
        o2_2 = [{"ray": 3}]
        r2_2 = Base.to_json_string(o2_2)
        o2_3 = None
        r2_3 = Base.to_json_string(o2_3)
        o2_4 = "raymundo"
        r2_4 = Base.to_json_string(o2_4)
        o2_5 = 123
        o2_6 = [[1, 2, 3]]
        r2_6 = Base.to_json_string(o2_6)
        o2_7 = []
        r2_7 = Base.to_json_string(o2_7)
        self.assertEqual(Base.from_json_string(r2_1), o2_1)
        self.assertEqual(Base.from_json_string(r2_2), o2_2)
        self.assertEqual(Base.from_json_string(r2_3), [])
        self.assertEqual(Base.from_json_string(r2_4), o2_4)
        self.assertEqual(Base.from_json_string(r2_6), o2_6)
        self.assertEqual(Base.from_json_string(r2_7), o2_7)
#        self.assertEqual(Base.from_json_string(o2_1), [])
        self.assertEqual(Base.from_json_string(o2_3), [])
        self.assertEqual(Base.from_json_string(o2_7), [])

    def test_007_create(self):
        """Revising file creation and writting"""
        o3_1 = {'id': 1, 'width': 1, 'height': 2, 'x': 2, 'y': 2}
        r3_1 = Rectangle.create(**o3_1)
        self.assertEqual(r3_1.__str__(), '[Rectangle] (1) 2/2 - 1/2')
        o3_2 = {'id': 2, 'size': 3, 'x': 4, 'y': 5}
        s3_1 = Square.create(**o3_2)
        self.assertEqual(s3_1.__str__(), '[Square] (2) 4/5 - 3')
        o3_2 = {'id': 1, 'width': "string", 'height': 2, 'x': 2, 'y': 2}
        o3_3 = {'id': 2, 'size': "string", 'x': 4, 'y': 5}
        with self.assertRaises(TypeError):
            r3_2 = Rectangle.create(**o3_2)
            s3_2 = Square.create(**o3_3)

    def test_008_JsonStringFormat(self):
        """Checking JSON string format"""
        list_input = [
            {'id': 100, 'width': 25, 'height': 5},
            {'id': 8, 'width': 11, 'height': 8}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(list_input), list)
        self.assertTrue(type(json_list_input), str)
        self.assertTrue(type(list_output), list)

    def test_009_save(self):
        """Savingtests"""
        o4_1 = Rectangle(10, 7, 2, 8)
        o4_2 = Rectangle(2, 4)
        o4_3 = Square(10, 7, 2)
        o4_4 = Square(8)
        rsave = Rectangle.save_to_file([o4_1, o4_2])
        ssave = Square.save_to_file([o4_3, o4_4])
        self.assertTrue(os.path.isfile('Rectangle.json'))
        self.assertTrue(os.path.isfile('Square.json'))


if __name__ == '__main__':
    unittest.main()
