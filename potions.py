#!/usr/bin/env python

import json

class Potion:
    id = ''
    name = ''
    desc = ''
    icon = ''
    buff = ''
    consumable_scenarios = []
    deletable = False
    ordering = 0

    def __str__(self):
        return json.dumps(self.__dict__, sort_keys=True)

class Potions:
    def __init__(self, gdc, gdw, s):
        self.gdc = gdc
        self.gdw = gdw
        self.s = s
        self.objects = []

        for message in self.gdw['messages']:
            if 'vaultItem' in message and message['vaultItem']['vaultCategoryGmtId'] == 'proto_vaultcategory_potions':
                obj = message['vaultItem']
                potion = Potion()
                potion.id = obj['id']
                potion.buff = obj['potionItem']['appliedBuffGmtId'][0]
                potion.consumable_scenarios = obj['potionItem']['consumableScenario']
                self.objects.append(potion)

        for potion in self.objects:
            for message in self.gdc['messages']:
                if 'vaultItem' in message and message['vaultItem']['id'] == potion.id:
                    obj = message['vaultItem']
                    potion.icon = obj['icon']
                    if 'deletable' in obj and obj['deletable'] == 'true':
                        potion.deletable = True
                    potion.name = self.s.find(obj['name'])
                    potion.desc = self.s.find(obj['description'])
                    potion.ordering = obj['ordering']
            print(potion)