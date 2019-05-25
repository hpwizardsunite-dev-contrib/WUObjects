# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/apply_key_to_walkbox_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/apply_key_to_walkbox_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nAwuprotos/networking/responses/apply_key_to_walkbox_response.proto\x12\x1dwuprotos.networking.responses\"\xdc\x01\n\x19\x41pplyKeyToWalkboxResponse\x12O\n\x06status\x18\x01 \x01(\x0e\x32?.wuprotos.networking.responses.ApplyKeyToWalkboxResponse.Status\"n\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x13\n\x0fINVALID_WALKBOX\x10\x03\x12\x13\n\x0fKEY_UNAVAILABLE\x10\x04\x12\x15\n\x11\x41LREADY_UNLOCKING\x10\x05\x62\x06proto3')
)



_APPLYKEYTOWALKBOXRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='wuprotos.networking.responses.ApplyKeyToWalkboxResponse.Status',
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
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_WALKBOX', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEY_UNAVAILABLE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALREADY_UNLOCKING', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=211,
  serialized_end=321,
)
_sym_db.RegisterEnumDescriptor(_APPLYKEYTOWALKBOXRESPONSE_STATUS)


_APPLYKEYTOWALKBOXRESPONSE = _descriptor.Descriptor(
  name='ApplyKeyToWalkboxResponse',
  full_name='wuprotos.networking.responses.ApplyKeyToWalkboxResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wuprotos.networking.responses.ApplyKeyToWalkboxResponse.status', index=0,
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
    _APPLYKEYTOWALKBOXRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=321,
)

_APPLYKEYTOWALKBOXRESPONSE.fields_by_name['status'].enum_type = _APPLYKEYTOWALKBOXRESPONSE_STATUS
_APPLYKEYTOWALKBOXRESPONSE_STATUS.containing_type = _APPLYKEYTOWALKBOXRESPONSE
DESCRIPTOR.message_types_by_name['ApplyKeyToWalkboxResponse'] = _APPLYKEYTOWALKBOXRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ApplyKeyToWalkboxResponse = _reflection.GeneratedProtocolMessageType('ApplyKeyToWalkboxResponse', (_message.Message,), dict(
  DESCRIPTOR = _APPLYKEYTOWALKBOXRESPONSE,
  __module__ = 'wuprotos.networking.responses.apply_key_to_walkbox_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.ApplyKeyToWalkboxResponse)
  ))
_sym_db.RegisterMessage(ApplyKeyToWalkboxResponse)


# @@protoc_insertion_point(module_scope)