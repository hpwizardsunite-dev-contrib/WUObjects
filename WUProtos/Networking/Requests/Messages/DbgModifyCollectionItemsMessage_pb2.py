# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Requests/Messages/DbgModifyCollectionItemsMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Debug import DebugModifyCollectionItem_pb2 as WUProtos_dot_Data_dot_Debug_dot_DebugModifyCollectionItem__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Requests/Messages/DbgModifyCollectionItemsMessage.proto',
  package='WUProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nKWUProtos/Networking/Requests/Messages/DbgModifyCollectionItemsMessage.proto\x12%WUProtos.Networking.Requests.Messages\x1a\x33WUProtos/Data/Debug/DebugModifyCollectionItem.proto\"k\n\x1f\x44\x62gModifyCollectionItemsMessage\x12H\n\x10\x63ollection_items\x18\x01 \x03(\x0b\x32..WUProtos.Data.Debug.DebugModifyCollectionItemb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Debug_dot_DebugModifyCollectionItem__pb2.DESCRIPTOR,])




_DBGMODIFYCOLLECTIONITEMSMESSAGE = _descriptor.Descriptor(
  name='DbgModifyCollectionItemsMessage',
  full_name='WUProtos.Networking.Requests.Messages.DbgModifyCollectionItemsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collection_items', full_name='WUProtos.Networking.Requests.Messages.DbgModifyCollectionItemsMessage.collection_items', index=0,
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
  serialized_start=171,
  serialized_end=278,
)

_DBGMODIFYCOLLECTIONITEMSMESSAGE.fields_by_name['collection_items'].message_type = WUProtos_dot_Data_dot_Debug_dot_DebugModifyCollectionItem__pb2._DEBUGMODIFYCOLLECTIONITEM
DESCRIPTOR.message_types_by_name['DbgModifyCollectionItemsMessage'] = _DBGMODIFYCOLLECTIONITEMSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DbgModifyCollectionItemsMessage = _reflection.GeneratedProtocolMessageType('DbgModifyCollectionItemsMessage', (_message.Message,), dict(
  DESCRIPTOR = _DBGMODIFYCOLLECTIONITEMSMESSAGE,
  __module__ = 'WUProtos.Networking.Requests.Messages.DbgModifyCollectionItemsMessage_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Requests.Messages.DbgModifyCollectionItemsMessage)
  ))
_sym_db.RegisterMessage(DbgModifyCollectionItemsMessage)


# @@protoc_insertion_point(module_scope)