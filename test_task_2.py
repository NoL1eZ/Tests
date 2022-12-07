import unittest
from yaDisk import new_folder

file_path = 'asdaфывsaf'

class Test_func (unittest.TestCase):
    def test_func_stats(self):
        result = new_folder(file_path)
        if result == '<Response [409]>':
            print('Ресурс "{path}" уже существует')
        etalon = '<Response [201]>'
        self.assertEqual(result, etalon)