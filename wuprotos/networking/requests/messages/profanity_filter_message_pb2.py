# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/profanity_filter_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/profanity_filter_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nDwuprotos/networking/requests/messages/profanity_filter_message.proto\x12%wuprotos.networking.requests.messages\"&\n\x16ProfanityFilterMessage\x12\x0c\n\x04text\x18\x01 \x03(\tb\x06proto3')
)




_PROFANITYFILTERMESSAGE = _descriptor.Descriptor(
  name='ProfanityFilterMessage',
  full_name='wuprotos.networking.requests.messages.ProfanityFilterMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='wuprotos.networking.requests.messages.ProfanityFilterMessage.text', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=111,
  serialized_end=149,
)

DESCRIPTOR.message_types_by_name['ProfanityFilterMessage'] = _PROFANITYFILTERMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProfanityFilterMessage = _reflection.GeneratedProtocolMessageType('ProfanityFilterMessage', (_message.Message,), dict(
  DESCRIPTOR = _PROFANITYFILTERMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.profanity_filter_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.ProfanityFilterMessage)
  ))
_sym_db.RegisterMessage(ProfanityFilterMessage)


# @@protoc_insertion_point(module_scope)