#!/usr/bin/env python

import json

class Achievement:
    id = ''
    name = ''
    desc = ''
    amount = 0
    has_badge = False
    badge_icon = '' # Only filled out if has_badge is True

    def __str__(self):
        return json.dumps(self.__dict__, sort_keys=True)

class Achievements:
    def __init__(self, gdc, gdw, s):
        self.gdc = gdc
        self.gdw = gdw
        self.s = s
        self.objects = []

        for message in self.gdw['messages']:
            if 'quest' in message and message['quest']['type'] == 'QUEST_TYPE_ACHIEVEMENT':
                obj = message['quest']
                achievement = Achievement()
                achievement.id = obj['id']

                requirements = obj['tasks'][0]['reqTask']['reqs']['reqs'][0]
                if 'lifetimeMetricReq' in requirements:
                    achievement.amount = requirements['lifetimeMetricReq']['requiredCount']
                else:
                    achievement.amount = requirements['levelReq']['level']

                rewards = obj['rewards']['rewards']
                for reward in rewards:
                    if 'itemReward' in reward and reward['itemReward']['itemId'].startswith('proto_vaultitem_badge'):
                        achievement.has_badge = True
                        achievement.badge_icon = reward['itemReward']['itemId']
                self.objects.append(achievement)

        for achievement in self.objects:
            for message in self.gdc['messages']:
                if 'quest' in message and message['quest']['id'] == achievement.id:
                    obj = message['quest']
                    achievement.name = self.s.find(obj['questNameLocKey'])
                    achievement.desc = self.s.find(obj['questDescLocKey'])
                if achievement.has_badge and 'vaultItem' in message and message['vaultItem']['id'] == achievement.badge_icon:
                    obj = message['vaultItem']
                    achievement.badge_icon = obj['icon']

            #print(achievement.desc.format(AMOUNT=achievement.amount))

            #if achievement.has_badge:
            #    print(achievement.name + ': ' + achievement.badge_icon + '.png')