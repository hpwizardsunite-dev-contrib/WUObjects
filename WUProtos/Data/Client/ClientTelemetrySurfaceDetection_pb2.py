# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientTelemetrySurfaceDetection.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientTelemetrySurfaceDetection.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n:WUProtos/Data/Client/ClientTelemetrySurfaceDetection.proto\x12\x14WUProtos.Data.Client\"R\n\x1f\x43lientTelemetrySurfaceDetection\x12\x18\n\x10\x65ncounter_gmt_id\x18\x01 \x01(\t\x12\x15\n\rfound_surface\x18\x02 \x01(\x08\x62\x06proto3')
)




_CLIENTTELEMETRYSURFACEDETECTION = _descriptor.Descriptor(
  name='ClientTelemetrySurfaceDetection',
  full_name='WUProtos.Data.Client.ClientTelemetrySurfaceDetection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='encounter_gmt_id', full_name='WUProtos.Data.Client.ClientTelemetrySurfaceDetection.encounter_gmt_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='found_surface', full_name='WUProtos.Data.Client.ClientTelemetrySurfaceDetection.found_surface', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=84,
  serialized_end=166,
)

DESCRIPTOR.message_types_by_name['ClientTelemetrySurfaceDetection'] = _CLIENTTELEMETRYSURFACEDETECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientTelemetrySurfaceDetection = _reflection.GeneratedProtocolMessageType('ClientTelemetrySurfaceDetection', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTTELEMETRYSURFACEDETECTION,
  __module__ = 'WUProtos.Data.Client.ClientTelemetrySurfaceDetection_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientTelemetrySurfaceDetection)
  ))
_sym_db.RegisterMessage(ClientTelemetrySurfaceDetection)


# @@protoc_insertion_point(module_scope)