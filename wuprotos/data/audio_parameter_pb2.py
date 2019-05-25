# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/data/audio_parameter.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/data/audio_parameter.proto',
  package='wuprotos.data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n#wuprotos/data/audio_parameter.proto\x12\rwuprotos.data\"9\n\x0e\x41udioParameter\x12\x12\n\nparam_name\x18\x01 \x01(\t\x12\x13\n\x0bparam_value\x18\x02 \x01(\x02\x62\x06proto3')
)




_AUDIOPARAMETER = _descriptor.Descriptor(
  name='AudioParameter',
  full_name='wuprotos.data.AudioParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='param_name', full_name='wuprotos.data.AudioParameter.param_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='param_value', full_name='wuprotos.data.AudioParameter.param_value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['AudioParameter'] = _AUDIOPARAMETER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AudioParameter = _reflection.GeneratedProtocolMessageType('AudioParameter', (_message.Message,), dict(
  DESCRIPTOR = _AUDIOPARAMETER,
  __module__ = 'wuprotos.data.audio_parameter_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.data.AudioParameter)
  ))
_sym_db.RegisterMessage(AudioParameter)


# @@protoc_insertion_point(module_scope)