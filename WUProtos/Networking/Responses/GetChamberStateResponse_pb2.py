# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Responses/GetChamberStateResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Enums import ChallengeRpcStatus_pb2 as WUProtos_dot_Enums_dot_ChallengeRpcStatus__pb2
from WUProtos.Data import ChamberState_pb2 as WUProtos_dot_Data_dot_ChamberState__pb2
from WUProtos.Data.Client import ClientPlayerSnapshot_pb2 as WUProtos_dot_Data_dot_Client_dot_ClientPlayerSnapshot__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Responses/GetChamberStateResponse.proto',
  package='WUProtos.Networking.Responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n;WUProtos/Networking/Responses/GetChamberStateResponse.proto\x12\x1dWUProtos.Networking.Responses\x1a\'WUProtos/Enums/ChallengeRpcStatus.proto\x1a WUProtos/Data/ChamberState.proto\x1a/WUProtos/Data/Client/ClientPlayerSnapshot.proto\"\xdb\x01\n\x17GetChamberStateResponse\x12\x32\n\x06status\x18\x01 \x01(\x0e\x32\".WUProtos.Enums.ChallengeRpcStatus\x12*\n\x05state\x18\x02 \x01(\x0b\x32\x1b.WUProtos.Data.ChamberState\x12\x43\n\x0fplayer_snapshot\x18\x03 \x01(\x0b\x32*.WUProtos.Data.Client.ClientPlayerSnapshot\x12\x1b\n\x13next_call_timestamp\x18\x04 \x01(\x03\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Enums_dot_ChallengeRpcStatus__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_ChamberState__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_Client_dot_ClientPlayerSnapshot__pb2.DESCRIPTOR,])




_GETCHAMBERSTATERESPONSE = _descriptor.Descriptor(
  name='GetChamberStateResponse',
  full_name='WUProtos.Networking.Responses.GetChamberStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='WUProtos.Networking.Responses.GetChamberStateResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='WUProtos.Networking.Responses.GetChamberStateResponse.state', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_snapshot', full_name='WUProtos.Networking.Responses.GetChamberStateResponse.player_snapshot', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_call_timestamp', full_name='WUProtos.Networking.Responses.GetChamberStateResponse.next_call_timestamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=438,
)

_GETCHAMBERSTATERESPONSE.fields_by_name['status'].enum_type = WUProtos_dot_Enums_dot_ChallengeRpcStatus__pb2._CHALLENGERPCSTATUS
_GETCHAMBERSTATERESPONSE.fields_by_name['state'].message_type = WUProtos_dot_Data_dot_ChamberState__pb2._CHAMBERSTATE
_GETCHAMBERSTATERESPONSE.fields_by_name['player_snapshot'].message_type = WUProtos_dot_Data_dot_Client_dot_ClientPlayerSnapshot__pb2._CLIENTPLAYERSNAPSHOT
DESCRIPTOR.message_types_by_name['GetChamberStateResponse'] = _GETCHAMBERSTATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetChamberStateResponse = _reflection.GeneratedProtocolMessageType('GetChamberStateResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETCHAMBERSTATERESPONSE,
  __module__ = 'WUProtos.Networking.Responses.GetChamberStateResponse_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Responses.GetChamberStateResponse)
  ))
_sym_db.RegisterMessage(GetChamberStateResponse)


# @@protoc_insertion_point(module_scope)