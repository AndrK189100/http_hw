import requests
import pprint


def get_heroes(url, hero_names):
    heroes = []
    for hero in hero_names:
        result = requests.get(url + hero).json()
        result = result['results']
        for res in result:
            if res['name'] in res.values():
                heroes.append(res)
                break
    return heroes


def get_smartest_hero(heroes):
    heroes.sort(key=lambda val: int(val['powerstats']['intelligence']), reverse=True)
    return heroes[0]['name']

if __name__ == '__main__':
    heroes = get_heroes('https://superheroapi.com/api/2619421814940190/search/', ['Hulk', 'Captain America', 'Thanos'])
    name = get_smartest_hero(heroes)
    pprint.pprint(name)
