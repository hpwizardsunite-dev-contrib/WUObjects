# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Event/AnalyticsEvents.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Event import AnalyticsEvent_pb2 as WUProtos_dot_Data_dot_Event_dot_AnalyticsEvent__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Event/AnalyticsEvents.proto',
  package='WUProtos.Data.Event',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n)WUProtos/Data/Event/AnalyticsEvents.proto\x12\x13WUProtos.Data.Event\x1a(WUProtos/Data/Event/AnalyticsEvent.proto\"E\n\x0f\x41nalyticsEvents\x12\x32\n\x05\x65vent\x18\x01 \x03(\x0b\x32#.WUProtos.Data.Event.AnalyticsEventb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Event_dot_AnalyticsEvent__pb2.DESCRIPTOR,])




_ANALYTICSEVENTS = _descriptor.Descriptor(
  name='AnalyticsEvents',
  full_name='WUProtos.Data.Event.AnalyticsEvents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='WUProtos.Data.Event.AnalyticsEvents.event', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=108,
  serialized_end=177,
)

_ANALYTICSEVENTS.fields_by_name['event'].message_type = WUProtos_dot_Data_dot_Event_dot_AnalyticsEvent__pb2._ANALYTICSEVENT
DESCRIPTOR.message_types_by_name['AnalyticsEvents'] = _ANALYTICSEVENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnalyticsEvents = _reflection.GeneratedProtocolMessageType('AnalyticsEvents', (_message.Message,), dict(
  DESCRIPTOR = _ANALYTICSEVENTS,
  __module__ = 'WUProtos.Data.Event.AnalyticsEvents_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Event.AnalyticsEvents)
  ))
_sym_db.RegisterMessage(AnalyticsEvents)


# @@protoc_insertion_point(module_scope)