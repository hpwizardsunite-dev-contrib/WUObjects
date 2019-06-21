#!/usr/bin/env python
# TODO: clean this up
import json

class MapIngredient:
    id = ''
    name = ''
    amount = 0

    def __str__(self):
        return json.dumps(self.__dict__, sort_keys=True)

class MapIngredients:
    def __init__(self, gdc, gdw, s):
        self.gdc = gdc
        self.gdw = gdw
        self.s = s
        self.objects = []

        for message in self.gdw['messages']:
            if 'mapIngredient' in message:
                obj = message['mapIngredient']
                ingredient = MapIngredient()
                ingredient.id = obj['id']
                if 'itemReward' in obj['loot']['rewards'][0]:
                    ingredient.amount = obj['loot']['rewards'][0]['itemReward']['amount']

                self.objects.append(ingredient)

        for ingredient in self.objects:
            for message in self.gdc['messages']:
                id_name = ingredient.id.split('_')[-1]
                if 'vaultItem' in message and message['vaultItem']['id'] == 'proto_vaultitem_ingredients_' + id_name:
                    obj = message['vaultItem']
                    ingredient.name = self.s.find(obj['name'])


        for ingredient in self.objects:
            if ingredient.name == '':
                ingredient.name = ingredient.id
            print(str(ingredient.amount) + ' - ' + ingredient.id)