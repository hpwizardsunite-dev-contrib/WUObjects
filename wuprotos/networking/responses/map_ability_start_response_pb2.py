# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/map_ability_start_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/map_ability_start_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n>wuprotos/networking/responses/map_ability_start_response.proto\x12\x1dwuprotos.networking.responses\"\xf8\x02\n\x17MapAbilityStartResponse\x12M\n\x06status\x18\x01 \x01(\x0e\x32=.wuprotos.networking.responses.MapAbilityStartResponse.Status\"\x8d\x02\n\x06Status\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12 \n\x1cPLAYER_DOES_NOT_HAVE_ABILITY\x10\x02\x12\x17\n\x13\x41\x42ILITY_UNAVAILABLE\x10\x03\x12\x16\n\x12TARGET_UNAVAILABLE\x10\x04\x12\x12\n\x0e\x43HALLENGE_OVER\x10\x05\x12\t\n\x05\x45RROR\x10\x06\x12\x1b\n\x17\x43HAMBER_NOT_IN_PROGRESS\x10\x07\x12\x19\n\x15PLAYER_NOT_IN_CHAMBER\x10\x08\x12\x14\n\x10NOT_ENOUGH_FOCUS\x10\t\x12\x12\n\x0eTARGET_INVALID\x10\n\x12\x18\n\x14STRONGER_BUFF_EXISTS\x10\x0b\x62\x06proto3')
)



_MAPABILITYSTARTRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='wuprotos.networking.responses.MapAbilityStartResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_DOES_NOT_HAVE_ABILITY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABILITY_UNAVAILABLE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TARGET_UNAVAILABLE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_OVER', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAMBER_NOT_IN_PROGRESS', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_NOT_IN_CHAMBER', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_ENOUGH_FOCUS', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TARGET_INVALID', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRONGER_BUFF_EXISTS', index=11, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=205,
  serialized_end=474,
)
_sym_db.RegisterEnumDescriptor(_MAPABILITYSTARTRESPONSE_STATUS)


_MAPABILITYSTARTRESPONSE = _descriptor.Descriptor(
  name='MapAbilityStartResponse',
  full_name='wuprotos.networking.responses.MapAbilityStartResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wuprotos.networking.responses.MapAbilityStartResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MAPABILITYSTARTRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=474,
)

_MAPABILITYSTARTRESPONSE.fields_by_name['status'].enum_type = _MAPABILITYSTARTRESPONSE_STATUS
_MAPABILITYSTARTRESPONSE_STATUS.containing_type = _MAPABILITYSTARTRESPONSE
DESCRIPTOR.message_types_by_name['MapAbilityStartResponse'] = _MAPABILITYSTARTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MapAbilityStartResponse = _reflection.GeneratedProtocolMessageType('MapAbilityStartResponse', (_message.Message,), dict(
  DESCRIPTOR = _MAPABILITYSTARTRESPONSE,
  __module__ = 'wuprotos.networking.responses.map_ability_start_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.MapAbilityStartResponse)
  ))
_sym_db.RegisterMessage(MapAbilityStartResponse)


# @@protoc_insertion_point(module_scope)