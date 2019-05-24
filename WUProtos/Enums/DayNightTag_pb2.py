# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Enums/DayNightTag.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Enums/DayNightTag.proto',
  package='WUProtos.Enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n WUProtos/Enums/DayNightTag.proto\x12\x0eWUProtos.Enums*^\n\x0b\x44\x61yNightTag\x12\x17\n\x13\x45NV_DAY_NIGHT_UNSET\x10\x00\x12\x0b\n\x07\x45NV_DAY\x10\x01\x12\r\n\tENV_NIGHT\x10\x02\x12\x0c\n\x08\x45NV_DAWN\x10\x03\x12\x0c\n\x08\x45NV_DUSK\x10\x04\x62\x06proto3')
)

_DAYNIGHTTAG = _descriptor.EnumDescriptor(
  name='DayNightTag',
  full_name='WUProtos.Enums.DayNightTag',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENV_DAY_NIGHT_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENV_DAY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENV_NIGHT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENV_DAWN', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENV_DUSK', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=52,
  serialized_end=146,
)
_sym_db.RegisterEnumDescriptor(_DAYNIGHTTAG)

DayNightTag = enum_type_wrapper.EnumTypeWrapper(_DAYNIGHTTAG)
ENV_DAY_NIGHT_UNSET = 0
ENV_DAY = 1
ENV_NIGHT = 2
ENV_DAWN = 3
ENV_DUSK = 4


DESCRIPTOR.enum_types_by_name['DayNightTag'] = _DAYNIGHTTAG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)