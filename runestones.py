#!/usr/bin/env python

import json

class Runestone:
    id = ''
    name = ''
    desc = '' # All the same
    icon = ''
    family = ''
    limit = 0 # All the same
    level = 0
    deletable = False
    show_in_menu = False

    def __str__(self):
        return json.dumps(self.__dict__, sort_keys=True)

class Runestones:
    def __init__(self, gdc, gdw, s):
        self.gdc = gdc
        self.gdw = gdw
        self.s = s
        self.objects = []

        for message in self.gdw['messages']:
            if 'vaultItem' in message and message['vaultItem']['vaultCategoryGmtId'] == 'proto_vaultcategory_runestones':
                obj = message['vaultItem']
                runestone = Runestone()
                runestone.id = obj['id']
                runestone.limit = int(obj['cap'])
                runestone.level = int(obj['runestoneItem']['quality'])
                runestone.family = obj['runestoneItem']['collectionFamilyGmtId']
                self.objects.append(runestone)

        for runestone in self.objects:
            for message in self.gdc['messages']:
                # First replace the family ID with the family name
                if 'collectionFamily' in message and message['collectionFamily']['id'] == runestone.family:
                    obj = message['collectionFamily']
                    runestone.family = self.s.find(obj['name'])
                    # TODO: Could get family icon here as well

                # Then get the rest
                if 'vaultItem' in message and message['vaultItem']['id'] == runestone.id:
                    obj = message['vaultItem']
                    runestone.icon = obj['icon']
                    if 'deletable' in obj:
                        runestone.deletable = obj['deletable']
                    if 'showInVaultItemMenu' in obj:
                        runestone.show_in_menu = obj['showInVaultItemMenu']

                    runestone.name = self.s.find(obj['name'])
                    runestone.desc = self.s.find(obj['description'])

            print(runestone)