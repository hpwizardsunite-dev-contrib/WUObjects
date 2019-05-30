<!-- define variables -->
[1.1]: http://i.imgur.com/M4fJ65n.png (ATTENTION)


![alt text][1.1] <strong><em>`The contents of this repo are a proof of concept and are for educational use only`</em></strong>![alt text][1.1]<br/>

# WUObjects [![Build Status](https://travis-ci.org/hpwizardsunite-dev-contrib/WUObjects.svg?branch=master)](https://travis-ci.org/hpwizardsunite-dev-contrib/WUObjects) [![Discord](https://img.shields.io/badge/Discord-Online-blue.svg)](https://discord.gg/mFH2D34)

Scripts to extract useful details from Harry Potter Wizards Unite such as spells, foundables, professions, potions, etc.


## Getting started

### Prerequisites

* [Python 3](https://www.python.org/)
* [Protoc](https://developers.google.com/protocol-buffers/) (Google Protocol Buffers)
* Android phone with the HPWU app (optional - for assets)

### Instructions
* After cloning this repo, run the following to load the WU Protos submodule.

```git submodule update --init --recursive```

* To download assets, you will need to install HPWU on an Android device, go to the settings screen, scroll all the way down and hit the button that says Download all Assets. Then connect your phone to your computer in file transfer mode.

* To get an updated version of the GameDataWrapper file, replace `/gamefiles/GameDataWrapper.bytes` with the following file from your phone:

```/sdcard/Android/data/com.nianticlabs.hpwu.prod/files/GameData/GameDataWrapper.bytes```

* To get all the other assets you just downloaded, copy the following directory from your phone into the `/assets` folder:

```/sdcard/Android/data/com.nianticlabs.hpwu.prod/files/UnityCache/Shared```

* You can then extract these assets with a tool like [AssetStudio](https://github.com/Perfare/AssetStudio)

* The GameDataClient should be in there as a TextAsset and Strings_en_US_loc should be a MonoBehavior in there.

* To compile the WU protos run the following. This will create a folder called `wuprotos`

```
cd ./WUProtos_Base
./compile.py python -o ../ --keep_proto_files
```

* To decode the GameDataWrapper, GameDataClient, and strings files, run `gamefiles_decode.py` (only needs to be done if they've updated)

---

Everything else in this repo is a work in progress and is mainly there to make it easier for me to parse data out of the game files. Here is a general overview of everything in this repo.

<pre>/assets - Files that are loaded as the game is played
/gamefiles
  - GameDataClient - client-side code for rendering objects in the game
  - GameDataWrapper - server generated properties
  - strings - US localization text
/various_scripts - junk I had sitting around from previous decoding
/wuprotos - compiled python protos, do not edit
/WUProtos_Base - submodule containing all the .proto files
gamefiles_decode.py - already has been run, just here if there are updates to GDC/GDW/Strings
extract_objects.py - main extraction script. WIP.</pre>