import unittest
from main import stats, func_stats, ids, func_ids, geo_logs, func_geo_logs

class Test_func (unittest.TestCase):
    def test_func_stats(self):
        result = func_stats(stats)
        etalon = 'yandex'
        self.assertEqual(result, etalon)

    def test_func_ids(self):
        result = func_ids(ids)
        etalon = {98, 35, 15, 213, 54, 119}
        self.assertEqual(result, etalon)

    def test_func_geo_logs(self):
        result = func_geo_logs(geo_logs)
        etalon = [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]
        self.assertEqual(result, etalon)