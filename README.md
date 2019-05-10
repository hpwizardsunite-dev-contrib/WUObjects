[![Discord](https://img.shields.io/badge/Discord-Online-blue.svg)](https://discord.gg/mFH2D34)

# WUObjects
Scripts to extract useful details from Harry Potter Wizards Unite such as spells, foundables, professions, potions, etc.

<pre>/assets - Files that are loaded as the game is played. Sourced from /gamefiles/manifest
/gamefiles
  - GameDataClient - client-side code for rendering GameObjects?
  - GameDataWrapper - server generated properties
  - strings - US localization text
  - manifest - File that is used to determine which assets to load
/various_scripts - junk I had sitting around from previous decoding
/WUProtos - compiled python protos, do not edit
gamefiles_decode.py - already has been run, just here for there are updates to GDC/GDW/Strings
extract_objects.py - main extraction script. WIP.</pre>

Run extract_objects.py to get started
