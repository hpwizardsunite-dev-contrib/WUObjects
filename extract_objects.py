import json
from spells import Spells
from foundables import Foundables
from potions import Potions

# Simple class to look up a key in the strings file and return the key name if no value is found
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

spells = Spells(gdc, gdw, s)
spells.extract()

foundables = Foundables(gdc, gdw, s)
foundables.extract()

potions = Potions(gdc, gdw, s)
