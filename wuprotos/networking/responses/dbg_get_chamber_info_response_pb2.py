# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/dbg_get_chamber_info_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/dbg_get_chamber_info_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nAwuprotos/networking/responses/dbg_get_chamber_info_response.proto\x12\x1dwuprotos.networking.responses\"\x99\x01\n\x19\x44\x62gGetChamberInfoResponse\x12\x1b\n\x13\x63hamber_template_id\x18\x01 \x01(\t\x12\"\n\x1atotal_population_allotment\x18\x02 \x01(\r\x12!\n\x19used_population_allotment\x18\x03 \x01(\r\x12\x18\n\x10\x63hallenge_rating\x18\x04 \x01(\rb\x06proto3')
)




_DBGGETCHAMBERINFORESPONSE = _descriptor.Descriptor(
  name='DbgGetChamberInfoResponse',
  full_name='wuprotos.networking.responses.DbgGetChamberInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chamber_template_id', full_name='wuprotos.networking.responses.DbgGetChamberInfoResponse.chamber_template_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_population_allotment', full_name='wuprotos.networking.responses.DbgGetChamberInfoResponse.total_population_allotment', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='used_population_allotment', full_name='wuprotos.networking.responses.DbgGetChamberInfoResponse.used_population_allotment', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='challenge_rating', full_name='wuprotos.networking.responses.DbgGetChamberInfoResponse.challenge_rating', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=101,
  serialized_end=254,
)

DESCRIPTOR.message_types_by_name['DbgGetChamberInfoResponse'] = _DBGGETCHAMBERINFORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DbgGetChamberInfoResponse = _reflection.GeneratedProtocolMessageType('DbgGetChamberInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _DBGGETCHAMBERINFORESPONSE,
  __module__ = 'wuprotos.networking.responses.dbg_get_chamber_info_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.DbgGetChamberInfoResponse)
  ))
_sym_db.RegisterMessage(DbgGetChamberInfoResponse)


# @@protoc_insertion_point(module_scope)