import requests
from pprint import pprint


def search_hero(list_name_hero: list):
    api_ = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    j_api = api_.json()
    list_hero = sorted([[_['powerstats']['intelligence'], _['name']] for _ in j_api if list_name_hero.count(_['name'])])
    list_hero_2 = []
    for i in j_api:
        if list_name_hero.count(i['name']):
            list_hero_2.append([i['powerstats']['intelligence'], i['name']])

    return pprint(f'самый умный супергерой {list_hero[-1][1]}')


search_hero(['Hulk', 'Capitan America', 'Thanos'])
