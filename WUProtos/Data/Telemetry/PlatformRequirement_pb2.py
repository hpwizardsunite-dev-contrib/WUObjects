# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Telemetry/PlatformRequirement.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Enums import DevicePlatform_pb2 as WUProtos_dot_Enums_dot_DevicePlatform__pb2
from WUProtos.Enums import EqualityOperator_pb2 as WUProtos_dot_Enums_dot_EqualityOperator__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Telemetry/PlatformRequirement.proto',
  package='WUProtos.Data.Telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n1WUProtos/Data/Telemetry/PlatformRequirement.proto\x12\x17WUProtos.Data.Telemetry\x1a#WUProtos/Enums/DevicePlatform.proto\x1a%WUProtos/Enums/EqualityOperator.proto\"{\n\x13PlatformRequirement\x12\x30\n\x08platform\x18\x01 \x01(\x0e\x32\x1e.WUProtos.Enums.DevicePlatform\x12\x32\n\x08operator\x18\x02 \x01(\x0e\x32 .WUProtos.Enums.EqualityOperatorb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Enums_dot_DevicePlatform__pb2.DESCRIPTOR,WUProtos_dot_Enums_dot_EqualityOperator__pb2.DESCRIPTOR,])




_PLATFORMREQUIREMENT = _descriptor.Descriptor(
  name='PlatformRequirement',
  full_name='WUProtos.Data.Telemetry.PlatformRequirement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='platform', full_name='WUProtos.Data.Telemetry.PlatformRequirement.platform', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operator', full_name='WUProtos.Data.Telemetry.PlatformRequirement.operator', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=154,
  serialized_end=277,
)

_PLATFORMREQUIREMENT.fields_by_name['platform'].enum_type = WUProtos_dot_Enums_dot_DevicePlatform__pb2._DEVICEPLATFORM
_PLATFORMREQUIREMENT.fields_by_name['operator'].enum_type = WUProtos_dot_Enums_dot_EqualityOperator__pb2._EQUALITYOPERATOR
DESCRIPTOR.message_types_by_name['PlatformRequirement'] = _PLATFORMREQUIREMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlatformRequirement = _reflection.GeneratedProtocolMessageType('PlatformRequirement', (_message.Message,), dict(
  DESCRIPTOR = _PLATFORMREQUIREMENT,
  __module__ = 'WUProtos.Data.Telemetry.PlatformRequirement_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Telemetry.PlatformRequirement)
  ))
_sym_db.RegisterMessage(PlatformRequirement)


# @@protoc_insertion_point(module_scope)