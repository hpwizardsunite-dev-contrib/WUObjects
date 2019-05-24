# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/CauldronReward.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/CauldronReward.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"WUProtos/Data/CauldronReward.proto\x12\rWUProtos.Data\"U\n\x0e\x43\x61uldronReward\x12\x13\n\x0btemplate_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63\x61uldron_id\x18\x02 \x01(\x03\x12\x19\n\x11\x61vailability_time\x18\x03 \x01(\x03\x62\x06proto3')
)




_CAULDRONREWARD = _descriptor.Descriptor(
  name='CauldronReward',
  full_name='WUProtos.Data.CauldronReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='WUProtos.Data.CauldronReward.template_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cauldron_id', full_name='WUProtos.Data.CauldronReward.cauldron_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='availability_time', full_name='WUProtos.Data.CauldronReward.availability_time', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=53,
  serialized_end=138,
)

DESCRIPTOR.message_types_by_name['CauldronReward'] = _CAULDRONREWARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CauldronReward = _reflection.GeneratedProtocolMessageType('CauldronReward', (_message.Message,), dict(
  DESCRIPTOR = _CAULDRONREWARD,
  __module__ = 'WUProtos.Data.CauldronReward_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.CauldronReward)
  ))
_sym_db.RegisterMessage(CauldronReward)


# @@protoc_insertion_point(module_scope)