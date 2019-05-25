# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/get_currency_balance_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wuprotos.data import currency_quantity_pb2 as wuprotos_dot_data_dot_currency__quantity__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/get_currency_balance_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nAwuprotos/networking/responses/get_currency_balance_response.proto\x12\x1dwuprotos.networking.responses\x1a%wuprotos/data/currency_quantity.proto\"\xcf\x01\n\x1aGetCurrencyBalanceResponse\x12P\n\x06status\x18\x01 \x01(\x0e\x32@.wuprotos.networking.responses.GetCurrencyBalanceResponse.Status\x12\x30\n\x07\x62\x61lance\x18\x03 \x03(\x0b\x32\x1f.wuprotos.data.CurrencyQuantity\"-\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x62\x06proto3')
  ,
  dependencies=[wuprotos_dot_data_dot_currency__quantity__pb2.DESCRIPTOR,])



_GETCURRENCYBALANCERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='wuprotos.networking.responses.GetCurrencyBalanceResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=302,
  serialized_end=347,
)
_sym_db.RegisterEnumDescriptor(_GETCURRENCYBALANCERESPONSE_STATUS)


_GETCURRENCYBALANCERESPONSE = _descriptor.Descriptor(
  name='GetCurrencyBalanceResponse',
  full_name='wuprotos.networking.responses.GetCurrencyBalanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wuprotos.networking.responses.GetCurrencyBalanceResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='balance', full_name='wuprotos.networking.responses.GetCurrencyBalanceResponse.balance', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETCURRENCYBALANCERESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=140,
  serialized_end=347,
)

_GETCURRENCYBALANCERESPONSE.fields_by_name['status'].enum_type = _GETCURRENCYBALANCERESPONSE_STATUS
_GETCURRENCYBALANCERESPONSE.fields_by_name['balance'].message_type = wuprotos_dot_data_dot_currency__quantity__pb2._CURRENCYQUANTITY
_GETCURRENCYBALANCERESPONSE_STATUS.containing_type = _GETCURRENCYBALANCERESPONSE
DESCRIPTOR.message_types_by_name['GetCurrencyBalanceResponse'] = _GETCURRENCYBALANCERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCurrencyBalanceResponse = _reflection.GeneratedProtocolMessageType('GetCurrencyBalanceResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETCURRENCYBALANCERESPONSE,
  __module__ = 'wuprotos.networking.responses.get_currency_balance_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.GetCurrencyBalanceResponse)
  ))
_sym_db.RegisterMessage(GetCurrencyBalanceResponse)


# @@protoc_insertion_point(module_scope)