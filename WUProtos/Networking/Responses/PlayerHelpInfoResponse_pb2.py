# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Responses/PlayerHelpInfoResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Responses/PlayerHelpInfoResponse.proto',
  package='WUProtos.Networking.Responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n:WUProtos/Networking/Responses/PlayerHelpInfoResponse.proto\x12\x1dWUProtos.Networking.Responses\"+\n\x16PlayerHelpInfoResponse\x12\x11\n\tplayer_id\x18\x01 \x01(\tb\x06proto3')
)




_PLAYERHELPINFORESPONSE = _descriptor.Descriptor(
  name='PlayerHelpInfoResponse',
  full_name='WUProtos.Networking.Responses.PlayerHelpInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='WUProtos.Networking.Responses.PlayerHelpInfoResponse.player_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=93,
  serialized_end=136,
)

DESCRIPTOR.message_types_by_name['PlayerHelpInfoResponse'] = _PLAYERHELPINFORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerHelpInfoResponse = _reflection.GeneratedProtocolMessageType('PlayerHelpInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERHELPINFORESPONSE,
  __module__ = 'WUProtos.Networking.Responses.PlayerHelpInfoResponse_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Responses.PlayerHelpInfoResponse)
  ))
_sym_db.RegisterMessage(PlayerHelpInfoResponse)


# @@protoc_insertion_point(module_scope)