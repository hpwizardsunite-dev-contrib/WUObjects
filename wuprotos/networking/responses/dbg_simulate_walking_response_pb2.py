# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/dbg_simulate_walking_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/dbg_simulate_walking_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nAwuprotos/networking/responses/dbg_simulate_walking_response.proto\x12\x1dwuprotos.networking.responses\"\x9d\x01\n\x1a\x44\x62gSimulateWalkingResponse\x12P\n\x06status\x18\x01 \x01(\x0e\x32@.wuprotos.networking.responses.DbgSimulateWalkingResponse.Status\"-\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x62\x06proto3')
)



_DBGSIMULATEWALKINGRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='wuprotos.networking.responses.DbgSimulateWalkingResponse.Status',
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
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=213,
  serialized_end=258,
)
_sym_db.RegisterEnumDescriptor(_DBGSIMULATEWALKINGRESPONSE_STATUS)


_DBGSIMULATEWALKINGRESPONSE = _descriptor.Descriptor(
  name='DbgSimulateWalkingResponse',
  full_name='wuprotos.networking.responses.DbgSimulateWalkingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wuprotos.networking.responses.DbgSimulateWalkingResponse.status', index=0,
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
    _DBGSIMULATEWALKINGRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=258,
)

_DBGSIMULATEWALKINGRESPONSE.fields_by_name['status'].enum_type = _DBGSIMULATEWALKINGRESPONSE_STATUS
_DBGSIMULATEWALKINGRESPONSE_STATUS.containing_type = _DBGSIMULATEWALKINGRESPONSE
DESCRIPTOR.message_types_by_name['DbgSimulateWalkingResponse'] = _DBGSIMULATEWALKINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DbgSimulateWalkingResponse = _reflection.GeneratedProtocolMessageType('DbgSimulateWalkingResponse', (_message.Message,), dict(
  DESCRIPTOR = _DBGSIMULATEWALKINGRESPONSE,
  __module__ = 'wuprotos.networking.responses.dbg_simulate_walking_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.DbgSimulateWalkingResponse)
  ))
_sym_db.RegisterMessage(DbgSimulateWalkingResponse)


# @@protoc_insertion_point(module_scope)