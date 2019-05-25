# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/admin_grant_in_app_purchase_item_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/admin_grant_in_app_purchase_item_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nTwuprotos/networking/requests/messages/admin_grant_in_app_purchase_item_message.proto\x12%wuprotos.networking.requests.messages\"i\n\"AdminGrantInAppPurchaseItemMessage\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x0e\n\x06sku_id\x18\x02 \x01(\t\x12\x0e\n\x06reason\x18\x03 \x01(\t\x12\x10\n\x08quantity\x18\x04 \x01(\x05\x62\x06proto3')
)




_ADMINGRANTINAPPPURCHASEITEMMESSAGE = _descriptor.Descriptor(
  name='AdminGrantInAppPurchaseItemMessage',
  full_name='wuprotos.networking.requests.messages.AdminGrantInAppPurchaseItemMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='wuprotos.networking.requests.messages.AdminGrantInAppPurchaseItemMessage.player_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sku_id', full_name='wuprotos.networking.requests.messages.AdminGrantInAppPurchaseItemMessage.sku_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='wuprotos.networking.requests.messages.AdminGrantInAppPurchaseItemMessage.reason', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='wuprotos.networking.requests.messages.AdminGrantInAppPurchaseItemMessage.quantity', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=127,
  serialized_end=232,
)

DESCRIPTOR.message_types_by_name['AdminGrantInAppPurchaseItemMessage'] = _ADMINGRANTINAPPPURCHASEITEMMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdminGrantInAppPurchaseItemMessage = _reflection.GeneratedProtocolMessageType('AdminGrantInAppPurchaseItemMessage', (_message.Message,), dict(
  DESCRIPTOR = _ADMINGRANTINAPPPURCHASEITEMMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.admin_grant_in_app_purchase_item_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.AdminGrantInAppPurchaseItemMessage)
  ))
_sym_db.RegisterMessage(AdminGrantInAppPurchaseItemMessage)


# @@protoc_insertion_point(module_scope)