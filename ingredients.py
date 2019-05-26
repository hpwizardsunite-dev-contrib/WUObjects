#!/usr/bin/env python

import json

class Ingredient:
    id = ''
    name = ''
    desc = ''
    icon = ''
    limit = 0
    cost = 0
    deletable = False
    show_in_menu = False

    def __str__(self):
        return json.dumps(self.__dict__, sort_keys=True)

class Ingredients:
    def __init__(self, gdc, gdw, s):
        self.gdc = gdc
        self.gdw = gdw
        self.s = s
        self.objects = []

        for message in self.gdw['messages']:
            if 'vaultItem' in message and message['vaultItem']['vaultCategoryGmtId'] == 'proto_vaultcategory_ingredients':
                obj = message['vaultItem']
                ingredient = Ingredient()
                ingredient.id = obj['id']
                ingredient.limit = int(obj['cap'])
                ingredient.cost = int(obj['potionIngredient']['cost']['rewards'][0]['currencyReward']['amount'])
                self.objects.append(ingredient)

        for ingredient in self.objects:
            for message in self.gdc['messages']:
                if 'vaultItem' in message and message['vaultItem']['id'] == ingredient.id:
                    obj = message['vaultItem']
                    ingredient.icon = obj['icon']
                    if 'deletable' in obj:
                        ingredient.deletable = obj['deletable']
                    if 'showInVaultItemMenu' in obj:
                        ingredient.show_in_menu = obj['showInVaultItemMenu']

                    ingredient.name = self.s.find(obj['name'])
                    ingredient.desc = self.s.find(obj['description'])

            print(ingredient)
