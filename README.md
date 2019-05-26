<!-- define variables -->
[1.1]: http://i.imgur.com/M4fJ65n.png (ATTENTION)


![alt text][1.1] <strong><em>`The contents of this repo are a proof of concept and are for educational use only`</em></strong>![alt text][1.1]<br/>

# WUObjects [![Build Status](https://travis-ci.org/hpwizardsunite-dev-contrib/WUObjects.svg?branch=master)](https://travis-ci.org/hpwizardsunite-dev-contrib/WUObjects) [![Discord](https://img.shields.io/badge/Discord-Online-blue.svg)](https://discord.gg/mFH2D34)

Scripts to extract useful details from Harry Potter Wizards Unite such as spells, foundables, professions, potions, etc.

<pre>/assets - Files that are loaded as the game is played. Sourced from /gamefiles/manifest
/gamefiles
  - GameDataClient - client-side code for rendering GameObjects?
  - GameDataWrapper - server generated properties
  - strings - US localization text
  - manifest - File that is used to determine which assets to load
/various_scripts - junk I had sitting around from previous decoding
Compile *.proto files
cd ./WUProtos_Base
  - ./compile.py python -o ../ --keep_proto_files
/wuprotos - compiled python protos, do not edit
gamefiles_decode.py - already has been run, just here for there are updates to GDC/GDW/Strings
extract_objects.py - main extraction script. WIP.</pre>

Run extract_objects.py to get started
