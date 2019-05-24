# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Profession/ProfessionRank.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import Requirements_pb2 as WUProtos_dot_Data_dot_Requirements__pb2
from WUProtos.Data.Profession import ProfessionNode_pb2 as WUProtos_dot_Data_dot_Profession_dot_ProfessionNode__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Profession/ProfessionRank.proto',
  package='WUProtos.Data.Profession',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n-WUProtos/Data/Profession/ProfessionRank.proto\x12\x18WUProtos.Data.Profession\x1a WUProtos/Data/Requirements.proto\x1a-WUProtos/Data/Profession/ProfessionNode.proto\"\xc7\x02\n\x0eProfessionRank\x12\x1d\n\x15potential_rank_points\x18\x01 \x01(\r\x12\x31\n\x0crequirements\x18\x02 \x03(\x0b\x32\x1b.WUProtos.Data.Requirements\x12^\n\x14profession_nodes_map\x18\x03 \x03(\x0b\x32@.WUProtos.Data.Profession.ProfessionRank.ProfessionNodesMapEntry\x12\x12\n\nshow_in_ui\x18\x04 \x01(\x08\x12\n\n\x02id\x18\x05 \x01(\t\x1a\x63\n\x17ProfessionNodesMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32(.WUProtos.Data.Profession.ProfessionNode:\x02\x38\x01\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Requirements__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_Profession_dot_ProfessionNode__pb2.DESCRIPTOR,])




_PROFESSIONRANK_PROFESSIONNODESMAPENTRY = _descriptor.Descriptor(
  name='ProfessionNodesMapEntry',
  full_name='WUProtos.Data.Profession.ProfessionRank.ProfessionNodesMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='WUProtos.Data.Profession.ProfessionRank.ProfessionNodesMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='WUProtos.Data.Profession.ProfessionRank.ProfessionNodesMapEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=385,
  serialized_end=484,
)

_PROFESSIONRANK = _descriptor.Descriptor(
  name='ProfessionRank',
  full_name='WUProtos.Data.Profession.ProfessionRank',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='potential_rank_points', full_name='WUProtos.Data.Profession.ProfessionRank.potential_rank_points', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requirements', full_name='WUProtos.Data.Profession.ProfessionRank.requirements', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profession_nodes_map', full_name='WUProtos.Data.Profession.ProfessionRank.profession_nodes_map', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_in_ui', full_name='WUProtos.Data.Profession.ProfessionRank.show_in_ui', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.Profession.ProfessionRank.id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PROFESSIONRANK_PROFESSIONNODESMAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=484,
)

_PROFESSIONRANK_PROFESSIONNODESMAPENTRY.fields_by_name['value'].message_type = WUProtos_dot_Data_dot_Profession_dot_ProfessionNode__pb2._PROFESSIONNODE
_PROFESSIONRANK_PROFESSIONNODESMAPENTRY.containing_type = _PROFESSIONRANK
_PROFESSIONRANK.fields_by_name['requirements'].message_type = WUProtos_dot_Data_dot_Requirements__pb2._REQUIREMENTS
_PROFESSIONRANK.fields_by_name['profession_nodes_map'].message_type = _PROFESSIONRANK_PROFESSIONNODESMAPENTRY
DESCRIPTOR.message_types_by_name['ProfessionRank'] = _PROFESSIONRANK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProfessionRank = _reflection.GeneratedProtocolMessageType('ProfessionRank', (_message.Message,), dict(

  ProfessionNodesMapEntry = _reflection.GeneratedProtocolMessageType('ProfessionNodesMapEntry', (_message.Message,), dict(
    DESCRIPTOR = _PROFESSIONRANK_PROFESSIONNODESMAPENTRY,
    __module__ = 'WUProtos.Data.Profession.ProfessionRank_pb2'
    # @@protoc_insertion_point(class_scope:WUProtos.Data.Profession.ProfessionRank.ProfessionNodesMapEntry)
    ))
  ,
  DESCRIPTOR = _PROFESSIONRANK,
  __module__ = 'WUProtos.Data.Profession.ProfessionRank_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Profession.ProfessionRank)
  ))
_sym_db.RegisterMessage(ProfessionRank)
_sym_db.RegisterMessage(ProfessionRank.ProfessionNodesMapEntry)


_PROFESSIONRANK_PROFESSIONNODESMAPENTRY._options = None
# @@protoc_insertion_point(module_scope)