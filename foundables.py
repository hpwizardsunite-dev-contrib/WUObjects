#!/usr/bin/env python

# Example extraction script
import json

class Foundable:
    id = ''
    name = ''
    desc = ''
    icon = ''
    family_id = ''
    page_id = ''
    rarity = ''
    counts = []

    def __str__(self):
        # format can be anything you want
        return json.dumps(self.__dict__, sort_keys=True)

class Foundables:
    def __init__(self, gdc, gdw, s):
        self.gdc = gdc
        self.gdw = gdw
        self.s = s
        self.objects = []

        for message in self.gdw['messages']:
            if 'collectionItem' in message:
                foundable = Foundable()
                foundable.id = message['collectionItem']['id']
                foundable.family_id = message['collectionItem']['familyId']
                foundable.page_id = message['collectionItem']['pageId']
                foundable.rarity = message['collectionItem']['rarity']
                foundable.counts = message['collectionItem']['shardCounts']
                self.objects.append(foundable)

        for foundable in self.objects:
            for message in self.gdc['messages']:
                if 'collectionItem' in message and message['collectionItem']['id'] == foundable.id:
                    foundable.name = self.s.find(message['collectionItem']['name'])
                    foundable.desc = self.s.find(message['collectionItem']['description'])
                    foundable.icon = message['collectionItem']['iconReturned']
            #if len(foundable.counts) == 4 and foundable.counts[0] == 1 and foundable.counts[1] == 2 and foundable.counts[2] == 3 and foundable.counts[3] == 4:
            #    print(foundable.id)
            print(foundable)