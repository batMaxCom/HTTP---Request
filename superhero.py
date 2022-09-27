import requests
from pprint import pprint


class S_Hero:
    host = 'https://akabab.github.io/superhero-api/api'

    def all_hero(self):
        url = f'{self.host}/all.json'
        response = requests.get(url)
        return response.json()

    def intelligence(self, heroes: list):
        hero_list = self.all_hero()
        hero_max_intelligence = {}
        for hero in hero_list:
            s_hero = {hero['name']: int(hero['powerstats']['intelligence'])}
            for h in heroes:
                if h in s_hero:
                    hero_max_intelligence.update(s_hero)
        return max(hero_max_intelligence.items(), key=lambda x: x[1])

