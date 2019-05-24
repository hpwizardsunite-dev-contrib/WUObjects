# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/PortkeyBonusGameRewardTuple.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Loot import LootReward_pb2 as WUProtos_dot_Data_dot_Loot_dot_LootReward__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/PortkeyBonusGameRewardTuple.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n/WUProtos/Data/PortkeyBonusGameRewardTuple.proto\x12\rWUProtos.Data\x1a#WUProtos/Data/Loot/LootReward.proto\"|\n\x1bPortkeyBonusGameRewardTuple\x12.\n\x06reward\x18\x01 \x01(\x0b\x32\x1e.WUProtos.Data.Loot.LootReward\x12\x12\n\nmultiplier\x18\x02 \x01(\x02\x12\x19\n\x11\x63\x61tegory_proto_id\x18\x03 \x01(\tb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Loot_dot_LootReward__pb2.DESCRIPTOR,])




_PORTKEYBONUSGAMEREWARDTUPLE = _descriptor.Descriptor(
  name='PortkeyBonusGameRewardTuple',
  full_name='WUProtos.Data.PortkeyBonusGameRewardTuple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reward', full_name='WUProtos.Data.PortkeyBonusGameRewardTuple.reward', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multiplier', full_name='WUProtos.Data.PortkeyBonusGameRewardTuple.multiplier', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category_proto_id', full_name='WUProtos.Data.PortkeyBonusGameRewardTuple.category_proto_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=103,
  serialized_end=227,
)

_PORTKEYBONUSGAMEREWARDTUPLE.fields_by_name['reward'].message_type = WUProtos_dot_Data_dot_Loot_dot_LootReward__pb2._LOOTREWARD
DESCRIPTOR.message_types_by_name['PortkeyBonusGameRewardTuple'] = _PORTKEYBONUSGAMEREWARDTUPLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PortkeyBonusGameRewardTuple = _reflection.GeneratedProtocolMessageType('PortkeyBonusGameRewardTuple', (_message.Message,), dict(
  DESCRIPTOR = _PORTKEYBONUSGAMEREWARDTUPLE,
  __module__ = 'WUProtos.Data.PortkeyBonusGameRewardTuple_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.PortkeyBonusGameRewardTuple)
  ))
_sym_db.RegisterMessage(PortkeyBonusGameRewardTuple)


# @@protoc_insertion_point(module_scope)