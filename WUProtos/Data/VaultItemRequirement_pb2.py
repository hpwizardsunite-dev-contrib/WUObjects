# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/VaultItemRequirement.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Enums import ComparisonOperator_pb2 as WUProtos_dot_Enums_dot_ComparisonOperator__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/VaultItemRequirement.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(WUProtos/Data/VaultItemRequirement.proto\x12\rWUProtos.Data\x1a\'WUProtos/Enums/ComparisonOperator.proto\"u\n\x14VaultItemRequirement\x12\x0f\n\x07item_id\x18\x01 \x01(\t\x12?\n\x13\x63omparison_operator\x18\x02 \x01(\x0e\x32\".WUProtos.Enums.ComparisonOperator\x12\x0b\n\x03qty\x18\x03 \x01(\x03\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Enums_dot_ComparisonOperator__pb2.DESCRIPTOR,])




_VAULTITEMREQUIREMENT = _descriptor.Descriptor(
  name='VaultItemRequirement',
  full_name='WUProtos.Data.VaultItemRequirement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='WUProtos.Data.VaultItemRequirement.item_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comparison_operator', full_name='WUProtos.Data.VaultItemRequirement.comparison_operator', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qty', full_name='WUProtos.Data.VaultItemRequirement.qty', index=2,
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
  serialized_start=100,
  serialized_end=217,
)

_VAULTITEMREQUIREMENT.fields_by_name['comparison_operator'].enum_type = WUProtos_dot_Enums_dot_ComparisonOperator__pb2._COMPARISONOPERATOR
DESCRIPTOR.message_types_by_name['VaultItemRequirement'] = _VAULTITEMREQUIREMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VaultItemRequirement = _reflection.GeneratedProtocolMessageType('VaultItemRequirement', (_message.Message,), dict(
  DESCRIPTOR = _VAULTITEMREQUIREMENT,
  __module__ = 'WUProtos.Data.VaultItemRequirement_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.VaultItemRequirement)
  ))
_sym_db.RegisterMessage(VaultItemRequirement)


# @@protoc_insertion_point(module_scope)