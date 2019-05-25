#!/usr/bin/env python

import json

from google.protobuf.json_format import MessageToJson

from wuprotos.data import game_data_wrapper_pb2
from wuprotos.data.client import client_game_data_wrapper_pb2

folder_name = './gamefiles/'


# Game Data Client file
def parse_gdc():
    with open(folder_name + 'GameDataClient.bytes', 'rb') as f:
        s = f.read()
    wrapper = client_game_data_wrapper_pb2.ClientGameDataWrapper()
    wrapper.ParseFromString(s)
    with open(folder_name + 'GameDataClient.json', 'w') as f:
        f.write(MessageToJson(wrapper))
    print('Parsed GDC')


# Game Data Wrapper file
def parse_gdw():
    with open(folder_name + 'GameDataWrapper.bytes', 'rb') as f:
        s = f.read()
    wrapper = game_data_wrapper_pb2.GameDataWrapper()
    wrapper.ParseFromString(s)
    with open(folder_name + 'GameDataWrapper.json', 'w') as f:
        f.write(MessageToJson(wrapper))
    print('Parsed GDW')


# Strings/localization file
def parse_str():
    with open(folder_name + 'strings.txt', 'rb') as f:
        s = f.read()
    sections = s.split(b'string LocKey = "')
    parseable_strings = {}
    first = True
    for k in sections:
        key_idx = k.index(b'"')
        key = k[:key_idx].decode('utf-8')

        val_idx = key_idx + 2 + k[key_idx + 1:].index(b'"')
        val_end_idx = val_idx + k[val_idx:].rfind(b'"')
        val = k[val_idx:val_end_idx].decode('utf-8')
        if first:
            first = False
            continue
        parseable_strings[key] = val
    with open(folder_name + 'strings.json', 'w') as f:
        f.write(json.dumps(parseable_strings, indent=0, sort_keys=True))
    print('Parsed strings')


parse_gdc()
parse_gdw()
parse_str()
