from WUProtos.Data.Client import ClientGameDataWrapper_pb2
from google.protobuf.json_format import MessageToJson

f = open('../GameDataClient.bytes', 'rb')
s = f.read()
f.close()

wrapper = ClientGameDataWrapper_pb2.ClientGameDataWrapper()
wrapper.ParseFromString(s)
print(MessageToJson(wrapper))
