import json

class Strings:
    def __init__(self, strings_map):
        self.s = strings_map
    def find(self, key):
        if key in self.s:
            return self.s[key]
        else:
            return key

with open('gamefiles/GameDataClient.json') as f:
    gdc = json.loads(f.read())
with open('gamefiles/GameDataWrapper.json') as f:
    gdw = json.loads(f.read())
with open('gamefiles/strings.json') as f:
    s = Strings(json.loads(f.read()))

# Helper function for parse_task
def get_str_for_difficulty(dif):
    if dif == 0:
        return 'Zero'
    if dif == 1.0:
        return 'Low'
    if dif == 2.0:
        return 'Medium'
    if dif == 3.0:
        return 'High'
    if dif == 4.0:
        return 'Danger'
    if dif == 5.0:
        return 'Severe'
    if dif == 6.0:
        return 'Emergency'
    if dif > 6.0:
        return 'Emergency'

# Helper function for parse_task
def get_str_for_trace(dif):
    if dif == 0.5:
        return 'Good'
    elif dif > 0.68 and dif <= 0.7:
        return 'Great'
    else: # TODO: Add masterful range if it ever shows up
        return str(dif)

# Helper function for parse_rewards
def get_vault_item_name(id):
    if id.startswith('vault_item_xp') or id.startswith('proto_vaultitem_potion') or id.startswith('proto_vaultitem_currency'):
        for message in gdc['messages']:
            if 'vaultItem' in message and id == message['vaultItem']['id']:
                return(s.find(message['vaultItem']['name']))
    else:
        return(id)

# Helper function for parse_rewards
def get_collection_family_name(id):
    for message in gdc['messages']:
        if 'collectionFamily' in message and id == message['collectionFamily']['id']:
            return(s.find(message['collectionFamily']['name']))

# Helper function for parse_rewards and parse_task
def get_foundable_name(id):
    for message in gdc['messages']:
        if 'collectionItem' in message and id == message['collectionItem']['id']:
            return(s.find(message['collectionItem']['name']))


# Complex function to parse a task and return a string
def parse_task(task):
    assert 'hookTask' in task # TODO: will probably need to expand this at some point
    output = ''
    task = task['hookTask']
    if 'lootOutposts' in task:
        amt = task['lootOutposts']['requiredOutpostsCount']
        output += s.find('quests_hooks_loot_outposts_number_only').format(AMOUNT=amt)
    elif 'winTraces' in task:
        if 'difficulty' in task['winTraces']:
            amt = task['winTraces']['requiredTraceCount']
            dif = task['winTraces']['difficulty']
            dif = get_str_for_difficulty(dif)
            output += (s.find('quests_hooks_win_traces_difficulty_only').format(AMOUNT=amt, DIFFICULTY=dif))
        elif 'familyGmtId' in task['winTraces']:
            amt = task['winTraces']['requiredTraceCount']
            fam = get_collection_family_name(task['winTraces']['familyGmtId'])
            output += (s.find('quests_hooks_win_traces_family_id').format(AMOUNT=amt, ID=fam))
        elif 'requiredTraceCount' in task['winTraces']:
            amt = task['winTraces']['requiredTraceCount']
            output += (s.find('quests_hooks_win_traces_number_only').format(AMOUNT=amt))
        else:
            print('ERROR:')
            print(task)
            assert False
    elif 'placeStickers' in task:
        if 'stickerFamilyGmtId' in task['placeStickers']:
            amt = task['placeStickers']['requiredPlaceCount']
            fam = task['placeStickers']['stickerFamilyGmtId']
            output += (s.find('quests_hooks_place_stickers_family_id').format(AMOUNT=amt, ID=fam))
        else:  # TODO: do something to alert on missing stuff here
            amt = task['placeStickers']['requiredPlaceCount']
            output += (s.find('quests_hooks_place_stickers_number_only').format(AMOUNT=amt))
    elif 'castSpells' in task:
        if 'requiredMasteryLevel' in task['castSpells']:
            amt = task['castSpells']['requiredSpellCount']
            mas = get_str_for_trace(task['castSpells']['requiredMasteryLevel'])
            output += (s.find('quests_hooks_cast_spells_mastery').format(AMOUNT=amt, MASTERY=mas))
        else:
            amt = task['castSpells']['requiredSpellCount']
            output += (s.find('quests_hooks_cast_spells_number_only').format(AMOUNT=amt))

    elif 'unlockPortmanteau' in task:
        if 'minimumDistanceType' in task['unlockPortmanteau']:
            amt = task['unlockPortmanteau']['requiredUnlockCount']
            dis = task['unlockPortmanteau']['minimumDistanceType']
            output += (s.find('quests_hooks_unlock_portmanteau_distance_type').format(AMOUNT=amt, DISTANCE=str(
                dis) + 'km Portkey Portmanteaus'))
        else:
            amt = task['unlockPortmanteau']['requiredUnlockCount']
            output += (s.find('quests_hooks_unlock_portmanteau_number_only').format(AMOUNT=amt))
    elif 'defeatMobInChallenges' in task:
        if 'encounterGmtId' in task['defeatMobInChallenges']:
            amt = task['defeatMobInChallenges']['requiredDefeatCount']
            mob = task['defeatMobInChallenges']['encounterGmtId']
            output += (s.find('quests_hooks_defeat_mob_challenges_encounter_id').format(AMOUNT=amt, ID=mob))
        else:
            amt = task['defeatMobInChallenges']['requiredDefeatCount']
            output += (s.find('quests_hooks_defeat_mob_challenges_number_only').format(AMOUNT=amt))
    elif 'playFortressChallenges' in task:
        if 'requiredLeastPlayerCount' in task['playFortressChallenges']:
            amt = task['playFortressChallenges']['requiredChallengeCount']
            pla = task['playFortressChallenges']['requiredLeastPlayerCount']
            output += (s.find('quests_hooks_play_fortress_required_players').format(AMOUNT=amt, PLAYERS=pla))
        else:
            amt = task['playFortressChallenges']['requiredChallengeCount']
            output += (s.find('quests_hooks_play_fortress_number_only').format(AMOUNT=amt))
    elif 'brewPotions' in task:
        if 'potionGmtId' in task['brewPotions']:
            assert False
        else:
            amt = task['brewPotions']['requiredBrewCount']
            output += (s.find('quests_hooks_brew_potion_number_only').format(AMOUNT=amt))
    elif 'usePotions' in task:
        if 'requiredPotion' in task['usePotions']:
            amt = task['usePotions']['requiredUseCount']
            pot = task['usePotions']['requiredPotion']
            output += (s.find('quests_hooks_use_potions_potion_id').format(AMOUNT=amt, ID=pot))
        else:
            amt = task['usePotions']['requiredUseCount']
            output += s.find('quests_hooks_use_potions_number_only').format(AMOUNT=amt)
    elif 'walkDistance' in task:
        amt = task['walkDistance']['requiredMicrometersToWalk']
        output += (s.find('quests_hooks_walk_number_only').format(AMOUNT=amt))
    elif 'collectStickers' in task:
        if 'stickerGmtId' in task['collectStickers']:
            amt = task['collectStickers']['requiredCollectCount']
            id = get_foundable_name(task['collectStickers']['stickerGmtId'])
            output += s.find('quests_hooks_collect_stickers_encounter_id').format(AMOUNT=amt, ID=id)
        elif 'stickerPageGmtId' in task['collectStickers']:
            assert False
        elif 'stickerFamilyGmtId' in task['collectStickers']:
            assert False
        else:
            amt = task['collectStickers']['requiredCollectCount']
            output += (s.find('quests_hooks_collect_stickers_number_only').format(AMOUNT=amt))
    elif 'collectPotionIngredients' in task:
        if 'ingredientGmtId' in task['collectPotionIngredients']:
            assert False
        else:
            amt = task['collectPotionIngredients']['requiredPotionIngredientCount']
            output += s.find('quests_hooks_collect_ingredients_number_only').format(AMOUNT=amt)
    elif 'takeSelfies' in task: # TODO: update this with the correct string
        amt = task['takeSelfies']['requiredSelfieCount']
        output += 'Take {AMOUNT} selfies for your Ministry ID.*'.format(AMOUNT=amt)
    elif 'takeEncounterPictures' in task: # TODO: update this with the correct string
        amt = task['takeEncounterPictures']['requiredPicturesCount']
        output += 'Take {AMOUNT} pictures of Foundables.*'.format(AMOUNT=amt)
    elif 'addFriends' in task: # TODO: update this with the correct string
        amt = task['addFriends']['requiredFriendsCount']
        output += 'Make {AMOUNT} new friends.*'.format(AMOUNT=amt)
    else:
        print('ERROR:')
        print(task)
        assert False
    return output

# Helper function to parse a list of rewards
def parse_rewards(rewards):
    output = ''
    for reward in rewards:
        if 'questReward' in reward:
            continue

        if len(rewards) > 1:
            output += '* '
        if 'itemReward' in reward:
            obj = reward['itemReward']
            output += obj['amount'] + ' ' + get_vault_item_name(obj['itemId'])
        elif 'collectionFamilyReward' in reward:
            obj = reward['collectionFamilyReward']
            output += str(obj['amount']) + ' ' + get_collection_family_name(obj['familyId']) + ' Family XP'
        elif 'currencyReward' in reward:
            obj = reward['currencyReward']
            assert obj['currencyId'] == 'vault_item_coins'
            output += str(obj['amount']) + ' Coins'
        elif 'collectionReward' in reward:
            obj = reward['collectionReward']
            output += str(obj['shardCount']) + ' ' + get_foundable_name(obj['itemId']) + ' Fragment'
        else:
            output += str(reward)

        if len(rewards) > 1:
            output += '\n'
        #output += str(reward)

    return output

section_num = 1 # Don't ask questions
# Takes a quest object, returns a string containing the tasks and rewards for it
def parse_quest(quest):
    global section_num
    assert(len(quest['tasks']) == 1)
    task = quest['tasks'][0]
    rewards = quest['rewards']['rewards']

    # Get task type, either header or normal
    if 'reqTask' in task:
        task_type = 'header'
    elif 'hookTask' in task:
        task_str = parse_task(task)
        task_type = 'normal'
    else:
        assert False

    rewards_str = parse_rewards(rewards)

    # Formatting of output
    if task_type == 'header':
        output = '\n# Section %d overall rewards:\n\n' % section_num
        section_num += 1
        output += rewards_str + '\n\n'
        output += 'Task|Reward\n---|---'
        return output
    else:
        output = task_str + ' | ' + rewards_str
        return output

for message in gdw['messages']:
    if 'quest' in message:
        obj = message['quest']
        if 'proto_quest_event_indy_2019_link' in obj['id']:
            print(parse_quest(obj))