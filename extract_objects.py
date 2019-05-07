import json
from spells import Spells
from foundables import Foundables

with open('gamefiles/GameDataClient.json') as f:
    gdc = json.loads(f.read())
with open('gamefiles/GameDataWrapper.json') as f:
    gdw = json.loads(f.read())
with open('gamefiles/strings.json') as f:
    s = json.loads(f.read())

spells = Spells(gdc, gdw, s)
spells.extract()

foundables = Foundables(gdc, gdw, s)
foundables.extract()
