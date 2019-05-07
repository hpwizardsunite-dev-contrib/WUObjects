# Example extraction script
import json

class Foundable:
    def __init__(self):
        self.id = ''
        self.family_id = ''
        self.page_id = ''
        self.rarity = ''
        self.name = ''
        self.desc = ''
        self.image = ''

    def __str__(self):
        # format can be anything you want
        return json.dumps(self.__dict__)

class Foundables:
    def __init__(self, gdc, gdw, s):
        self.gdc = gdc
        self.gdw = gdw
        self.s = s
        self.foundables = []

    def extract(self):
        for message in self.gdw['messages']:
            if 'collectionItem' in message:
                foundable = Foundable()
                foundable.id = message['collectionItem']['id']
                foundable.family_id = message['collectionItem']['familyId']
                foundable.page_id = message['collectionItem']['pageId']
                foundable.rarity = message['collectionItem']['rarity']
                self.foundables.append(foundable)

        for foundable in self.foundables:
            for message in self.gdc['messages']:
                if 'collectionItem' in message and message['collectionItem']['id'] == foundable.id:
                    foundable.name = self.s[message['collectionItem']['name']]
                    foundable.desc = self.s[message['collectionItem']['description']]
                    foundable.icon = message['collectionItem']['iconReturned'] # need better way to point to asset
            print(foundable) # write to file or something later?
