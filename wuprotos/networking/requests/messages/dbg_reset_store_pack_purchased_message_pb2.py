# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/dbg_reset_store_pack_purchased_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/dbg_reset_store_pack_purchased_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nRwuprotos/networking/requests/messages/dbg_reset_store_pack_purchased_message.proto\x12%wuprotos.networking.requests.messages\"\xd4\x01\n!DbgResetStorePackPurchasedMessage\x12o\n\nstore_pack\x18\x01 \x03(\x0b\x32[.wuprotos.networking.requests.messages.DbgResetStorePackPurchasedMessage.StorePackPurchased\x1a>\n\x12StorePackPurchased\x12\x15\n\rstore_pack_id\x18\x01 \x01(\t\x12\x11\n\tnew_count\x18\x02 \x01(\x03\x62\x06proto3')
)




_DBGRESETSTOREPACKPURCHASEDMESSAGE_STOREPACKPURCHASED = _descriptor.Descriptor(
  name='StorePackPurchased',
  full_name='wuprotos.networking.requests.messages.DbgResetStorePackPurchasedMessage.StorePackPurchased',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='store_pack_id', full_name='wuprotos.networking.requests.messages.DbgResetStorePackPurchasedMessage.StorePackPurchased.store_pack_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_count', full_name='wuprotos.networking.requests.messages.DbgResetStorePackPurchasedMessage.StorePackPurchased.new_count', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=276,
  serialized_end=338,
)

_DBGRESETSTOREPACKPURCHASEDMESSAGE = _descriptor.Descriptor(
  name='DbgResetStorePackPurchasedMessage',
  full_name='wuprotos.networking.requests.messages.DbgResetStorePackPurchasedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='store_pack', full_name='wuprotos.networking.requests.messages.DbgResetStorePackPurchasedMessage.store_pack', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DBGRESETSTOREPACKPURCHASEDMESSAGE_STOREPACKPURCHASED, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=338,
)

_DBGRESETSTOREPACKPURCHASEDMESSAGE_STOREPACKPURCHASED.containing_type = _DBGRESETSTOREPACKPURCHASEDMESSAGE
_DBGRESETSTOREPACKPURCHASEDMESSAGE.fields_by_name['store_pack'].message_type = _DBGRESETSTOREPACKPURCHASEDMESSAGE_STOREPACKPURCHASED
DESCRIPTOR.message_types_by_name['DbgResetStorePackPurchasedMessage'] = _DBGRESETSTOREPACKPURCHASEDMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DbgResetStorePackPurchasedMessage = _reflection.GeneratedProtocolMessageType('DbgResetStorePackPurchasedMessage', (_message.Message,), dict(

  StorePackPurchased = _reflection.GeneratedProtocolMessageType('StorePackPurchased', (_message.Message,), dict(
    DESCRIPTOR = _DBGRESETSTOREPACKPURCHASEDMESSAGE_STOREPACKPURCHASED,
    __module__ = 'wuprotos.networking.requests.messages.dbg_reset_store_pack_purchased_message_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.DbgResetStorePackPurchasedMessage.StorePackPurchased)
    ))
  ,
  DESCRIPTOR = _DBGRESETSTOREPACKPURCHASEDMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.dbg_reset_store_pack_purchased_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.DbgResetStorePackPurchasedMessage)
  ))
_sym_db.RegisterMessage(DbgResetStorePackPurchasedMessage)
_sym_db.RegisterMessage(DbgResetStorePackPurchasedMessage.StorePackPurchased)


# @@protoc_insertion_point(module_scope)