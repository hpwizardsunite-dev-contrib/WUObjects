# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/FeatureFlagRequirement.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/FeatureFlagRequirement.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n*WUProtos/Data/FeatureFlagRequirement.proto\x12\rWUProtos.Data\"1\n\x16\x46\x65\x61tureFlagRequirement\x12\x17\n\x0f\x66\x65\x61ture_flag_id\x18\x01 \x01(\tb\x06proto3')
)




_FEATUREFLAGREQUIREMENT = _descriptor.Descriptor(
  name='FeatureFlagRequirement',
  full_name='WUProtos.Data.FeatureFlagRequirement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_flag_id', full_name='WUProtos.Data.FeatureFlagRequirement.feature_flag_id', index=0,
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
  serialized_start=61,
  serialized_end=110,
)

DESCRIPTOR.message_types_by_name['FeatureFlagRequirement'] = _FEATUREFLAGREQUIREMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeatureFlagRequirement = _reflection.GeneratedProtocolMessageType('FeatureFlagRequirement', (_message.Message,), dict(
  DESCRIPTOR = _FEATUREFLAGREQUIREMENT,
  __module__ = 'WUProtos.Data.FeatureFlagRequirement_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.FeatureFlagRequirement)
  ))
_sym_db.RegisterMessage(FeatureFlagRequirement)


# @@protoc_insertion_point(module_scope)