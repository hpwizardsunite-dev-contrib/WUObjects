# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/data/default_profile.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/data/default_profile.proto',
  package='wuprotos.data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n#wuprotos/data/default_profile.proto\x12\rwuprotos.data\"\x1c\n\x0e\x44\x65\x66\x61ultProfile\x12\n\n\x02id\x18\x01 \x01(\tb\x06proto3')
)




_DEFAULTPROFILE = _descriptor.Descriptor(
  name='DefaultProfile',
  full_name='wuprotos.data.DefaultProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='wuprotos.data.DefaultProfile.id', index=0,
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
  serialized_start=54,
  serialized_end=82,
)

DESCRIPTOR.message_types_by_name['DefaultProfile'] = _DEFAULTPROFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DefaultProfile = _reflection.GeneratedProtocolMessageType('DefaultProfile', (_message.Message,), dict(
  DESCRIPTOR = _DEFAULTPROFILE,
  __module__ = 'wuprotos.data.default_profile_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.data.DefaultProfile)
  ))
_sym_db.RegisterMessage(DefaultProfile)


# @@protoc_insertion_point(module_scope)