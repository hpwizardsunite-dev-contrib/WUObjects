# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/claim_potion_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wuprotos.data.loot import loot_reward_pb2 as wuprotos_dot_data_dot_loot_dot_loot__reward__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/claim_potion_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n9wuprotos/networking/responses/claim_potion_response.proto\x12\x1dwuprotos.networking.responses\x1a$wuprotos/data/loot/loot_reward.proto\"\xbf\x03\n\x13\x43laimPotionResponse\x12T\n\x06result\x18\x01 \x01(\x0e\x32\x44.wuprotos.networking.responses.ClaimPotionResponse.ClaimPotionResult\x12G\n\x10received_rewards\x18\x02 \x01(\x0b\x32-.wuprotos.data.loot.LootReward.LootCollection\x12H\n\x11remaining_rewards\x18\x03 \x01(\x0b\x32-.wuprotos.data.loot.LootReward.LootCollection\"\xbe\x01\n\x11\x43laimPotionResult\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x17\n\x13\x45MPTY_SLOT_SELECTED\x10\x02\x12\x18\n\x14\x42REWING_NOT_COMPLETE\x10\x03\x12+\n\'INSUFFICIENT_INVENTORY_SPACE_FOR_POTION\x10\x04\x12/\n+CAULDRON_DOES_NOT_CONTAIN_REQUESTED_REWARDS\x10\x05\x62\x06proto3')
  ,
  dependencies=[wuprotos_dot_data_dot_loot_dot_loot__reward__pb2.DESCRIPTOR,])



_CLAIMPOTIONRESPONSE_CLAIMPOTIONRESULT = _descriptor.EnumDescriptor(
  name='ClaimPotionResult',
  full_name='wuprotos.networking.responses.ClaimPotionResponse.ClaimPotionResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMPTY_SLOT_SELECTED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BREWING_NOT_COMPLETE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSUFFICIENT_INVENTORY_SPACE_FOR_POTION', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAULDRON_DOES_NOT_CONTAIN_REQUESTED_REWARDS', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=388,
  serialized_end=578,
)
_sym_db.RegisterEnumDescriptor(_CLAIMPOTIONRESPONSE_CLAIMPOTIONRESULT)


_CLAIMPOTIONRESPONSE = _descriptor.Descriptor(
  name='ClaimPotionResponse',
  full_name='wuprotos.networking.responses.ClaimPotionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='wuprotos.networking.responses.ClaimPotionResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='received_rewards', full_name='wuprotos.networking.responses.ClaimPotionResponse.received_rewards', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remaining_rewards', full_name='wuprotos.networking.responses.ClaimPotionResponse.remaining_rewards', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLAIMPOTIONRESPONSE_CLAIMPOTIONRESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=578,
)

_CLAIMPOTIONRESPONSE.fields_by_name['result'].enum_type = _CLAIMPOTIONRESPONSE_CLAIMPOTIONRESULT
_CLAIMPOTIONRESPONSE.fields_by_name['received_rewards'].message_type = wuprotos_dot_data_dot_loot_dot_loot__reward__pb2._LOOTREWARD_LOOTCOLLECTION
_CLAIMPOTIONRESPONSE.fields_by_name['remaining_rewards'].message_type = wuprotos_dot_data_dot_loot_dot_loot__reward__pb2._LOOTREWARD_LOOTCOLLECTION
_CLAIMPOTIONRESPONSE_CLAIMPOTIONRESULT.containing_type = _CLAIMPOTIONRESPONSE
DESCRIPTOR.message_types_by_name['ClaimPotionResponse'] = _CLAIMPOTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClaimPotionResponse = _reflection.GeneratedProtocolMessageType('ClaimPotionResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLAIMPOTIONRESPONSE,
  __module__ = 'wuprotos.networking.responses.claim_potion_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.ClaimPotionResponse)
  ))
_sym_db.RegisterMessage(ClaimPotionResponse)


# @@protoc_insertion_point(module_scope)