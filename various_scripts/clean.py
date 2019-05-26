#!/usr/bin/env python

from wuprotos.data.client import client_game_data_wrapper_pb2
from google.protobuf.json_format import MessageToJson

f = open('../gamefiles/GameDataClient.bytes', 'rb')
s = f.read()
f.close()

wrapper = client_game_data_wrapper_pb2.ClientGameDataWrapper()
wrapper.ParseFromString(s)
print(MessageToJson(wrapper))
