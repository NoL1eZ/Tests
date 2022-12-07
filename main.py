import requests


stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
def func_stats(stats):
    max_sales = 0
    big_channel = None
    for channel, sale in stats.items():
      if sale > max_sales:
         big_channel = channel
         max_sales = sale
    return big_channel

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def func_ids(ids):
    result = set()
    for i in ids.values():
      result.update(i)
    return result

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
def func_geo_logs(geo_logs):
    result_list = []
    for visit in geo_logs:
        if 'Россия' in list(visit.values())[0]:
          result_list.append(visit)
    return result_list


