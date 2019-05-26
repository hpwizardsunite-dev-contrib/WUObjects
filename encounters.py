#!/usr/bin/env python

import json

class Encounter:
    id = ''
    name = ''
    spell = ''
    encounter_type = '' # oneof 'swish', 'combat', 'portkey', 'picture'
    base_win_rate = 0 # swish only

    reward_amount = 0 # not in portkey or picture
    reward_type = '' # not in portkey and combat is always the same

    enemy_ranks = [] # combat only

    enemy_stats_power = '' # combat only
    enemy_stats_resist = ''  # combat only
    enemy_stats_attack = ''  # combat only
    enemy_stats_dodge = ''  # combat only
    enemy_stats_hp = ''  # combat only
    enemy_stats_mitigation = ''  # combat only
    enemy_stats_precision = ''  # combat only
    enemy_stats_sunder = ''  # combat only

    enemy_stat_growth_power = 0 # combat only
    enemy_stat_growth_resist = 0  # combat only
    enemy_stat_growth_attack = 0  # combat only
    enemy_stat_growth_dodge = 0  # combat only
    enemy_stat_growth_hp = 0  # combat only
    enemy_stat_growth_mitigation = 0  # combat only
    enemy_stat_growth_precision = 0  # combat only
    enemy_stat_growth_sunder = 0  # combat only

    def __str__(self):
        return json.dumps(vars(self), sort_keys=True)


# Helper method
def get_growth_adjustment(obj):
    if 'growthAdjustment' in obj:
        return obj['growthAdjustment']
    else:
        return 0


class Encounters:
    def __init__(self, gdc, gdw, s):
        self.gdc = gdc
        self.gdw = gdw
        self.s = s
        self.objects = []

        for message in self.gdw['messages']:
            if 'encounter' in message:
                obj = message['encounter']
                encounter = Encounter()
                encounter.id = obj['id']

                stage = obj['stages'][0]
                encounter.spell = stage['spellGmtId']

                if 'swish' in stage:
                    encounter.encounter_type = 'swish'
                    encounter.base_win_rate = stage['swish']['baseWinRate']
                elif 'combat' in stage:
                    encounter.encounter_type = 'combat'
                    encounter.enemy_ranks = stage['combat']['enemyRanks']
                    stat = stage['combat']['enemyStats']['stat']
                    encounter.enemy_stats_power = stat['proto_rpgstat_stat_combat_affinity_power']
                    encounter.enemy_stats_resist = stat['proto_rpgstat_stat_combat_affinity_resist']
                    encounter.enemy_stats_attack = stat['proto_rpgstat_stat_combat_attack']
                    encounter.enemy_stats_dodge = stat['proto_rpgstat_stat_combat_dodge']
                    encounter.enemy_stats_hp = stat['proto_rpgstat_stat_combat_hp']
                    encounter.enemy_stats_mitigation = stat['proto_rpgstat_stat_combat_mitigation']
                    encounter.enemy_stats_precision = stat['proto_rpgstat_stat_combat_precision']
                    encounter.enemy_stats_sunder = stat['proto_rpgstat_stat_combat_sunder']

                    growth = stage['combat']['enemyStats']['statGrowth']
                    encounter.enemy_stat_growth_power = get_growth_adjustment(growth['proto_rpgstat_stat_combat_affinity_power'])
                    encounter.enemy_stat_growth_resist = get_growth_adjustment(growth['proto_rpgstat_stat_combat_affinity_resist'])
                    encounter.enemy_stat_growth_attack = get_growth_adjustment(growth['proto_rpgstat_stat_combat_attack'])
                    encounter.enemy_stat_growth_dodge = get_growth_adjustment(growth['proto_rpgstat_stat_combat_dodge'])
                    encounter.enemy_stat_growth_hp = get_growth_adjustment(growth['proto_rpgstat_stat_combat_hp'])
                    encounter.enemy_stat_growth_mitigation = get_growth_adjustment(growth['proto_rpgstat_stat_combat_mitigation'])
                    encounter.enemy_stat_growth_precision = get_growth_adjustment(growth['proto_rpgstat_stat_combat_precision'])
                    encounter.enemy_stat_growth_sunder = get_growth_adjustment(growth['proto_rpgstat_stat_combat_sunder'])
                elif 'portkey' in stage:
                    encounter.encounter_type = 'portkey'
                elif 'picture' in stage:
                    encounter.encounter_type = 'picture'

                if 'collectionItemRewardShards' in obj:
                    encounter.reward_amount = obj['collectionItemRewardShards']
                if 'collectionItemRewardGmtId' in obj:
                    encounter.reward_type = obj['collectionItemRewardGmtId']

                self.objects.append(encounter)

        for encounter in self.objects:
            for message in self.gdc['messages']:
                if 'encounter' in message and message['encounter']['id'] == encounter.id:
                    obj = message['encounter']
                    encounter.name = self.s.find(obj['name'])
                if 'collectionItem' in message and message['collectionItem']['id'] == encounter.reward_type:
                    obj = message['collectionItem']
                    encounter.reward_type = self.s.find(obj['name'])
            print(encounter)