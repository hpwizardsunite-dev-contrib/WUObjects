# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/SkuContent.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/SkuContent.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1eWUProtos/Data/SkuContent.proto\x12\rWUProtos.Data\"1\n\nSkuContent\x12\x11\n\titem_type\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x62\x06proto3')
)




_SKUCONTENT = _descriptor.Descriptor(
  name='SkuContent',
  full_name='WUProtos.Data.SkuContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_type', full_name='WUProtos.Data.SkuContent.item_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='WUProtos.Data.SkuContent.quantity', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=49,
  serialized_end=98,
)

DESCRIPTOR.message_types_by_name['SkuContent'] = _SKUCONTENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SkuContent = _reflection.GeneratedProtocolMessageType('SkuContent', (_message.Message,), dict(
  DESCRIPTOR = _SKUCONTENT,
  __module__ = 'WUProtos.Data.SkuContent_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.SkuContent)
  ))
_sym_db.RegisterMessage(SkuContent)


# @@protoc_insertion_point(module_scope)