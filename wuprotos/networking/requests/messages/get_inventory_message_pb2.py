# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/get_inventory_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/get_inventory_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nAwuprotos/networking/requests/messages/get_inventory_message.proto\x12%wuprotos.networking.requests.messages\"/\n\x13GetInventoryMessage\x12\x18\n\x10timestamp_millis\x18\x01 \x01(\x03\x62\x06proto3')
)




_GETINVENTORYMESSAGE = _descriptor.Descriptor(
  name='GetInventoryMessage',
  full_name='wuprotos.networking.requests.messages.GetInventoryMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp_millis', full_name='wuprotos.networking.requests.messages.GetInventoryMessage.timestamp_millis', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=108,
  serialized_end=155,
)

DESCRIPTOR.message_types_by_name['GetInventoryMessage'] = _GETINVENTORYMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetInventoryMessage = _reflection.GeneratedProtocolMessageType('GetInventoryMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETINVENTORYMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.get_inventory_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.GetInventoryMessage)
  ))
_sym_db.RegisterMessage(GetInventoryMessage)


# @@protoc_insertion_point(module_scope)