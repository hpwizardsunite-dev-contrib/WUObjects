# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/FlooNetworkRegionScores.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/FlooNetworkRegionScores.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n+WUProtos/Data/FlooNetworkRegionScores.proto\x12\rWUProtos.Data\"\xc9\x01\n\x17\x46looNetworkRegionScores\x12\x11\n\tseason_id\x18\x01 \x01(\t\x12\x11\n\tregion_id\x18\x02 \x01(\t\x12R\n\x0fpoints_per_team\x18\x03 \x03(\x0b\x32\x39.WUProtos.Data.FlooNetworkRegionScores.PointsPerTeamEntry\x1a\x34\n\x12PointsPerTeamEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x62\x06proto3')
)




_FLOONETWORKREGIONSCORES_POINTSPERTEAMENTRY = _descriptor.Descriptor(
  name='PointsPerTeamEntry',
  full_name='WUProtos.Data.FlooNetworkRegionScores.PointsPerTeamEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='WUProtos.Data.FlooNetworkRegionScores.PointsPerTeamEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='WUProtos.Data.FlooNetworkRegionScores.PointsPerTeamEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=264,
)

_FLOONETWORKREGIONSCORES = _descriptor.Descriptor(
  name='FlooNetworkRegionScores',
  full_name='WUProtos.Data.FlooNetworkRegionScores',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='season_id', full_name='WUProtos.Data.FlooNetworkRegionScores.season_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='region_id', full_name='WUProtos.Data.FlooNetworkRegionScores.region_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='points_per_team', full_name='WUProtos.Data.FlooNetworkRegionScores.points_per_team', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FLOONETWORKREGIONSCORES_POINTSPERTEAMENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=264,
)

_FLOONETWORKREGIONSCORES_POINTSPERTEAMENTRY.containing_type = _FLOONETWORKREGIONSCORES
_FLOONETWORKREGIONSCORES.fields_by_name['points_per_team'].message_type = _FLOONETWORKREGIONSCORES_POINTSPERTEAMENTRY
DESCRIPTOR.message_types_by_name['FlooNetworkRegionScores'] = _FLOONETWORKREGIONSCORES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FlooNetworkRegionScores = _reflection.GeneratedProtocolMessageType('FlooNetworkRegionScores', (_message.Message,), dict(

  PointsPerTeamEntry = _reflection.GeneratedProtocolMessageType('PointsPerTeamEntry', (_message.Message,), dict(
    DESCRIPTOR = _FLOONETWORKREGIONSCORES_POINTSPERTEAMENTRY,
    __module__ = 'WUProtos.Data.FlooNetworkRegionScores_pb2'
    # @@protoc_insertion_point(class_scope:WUProtos.Data.FlooNetworkRegionScores.PointsPerTeamEntry)
    ))
  ,
  DESCRIPTOR = _FLOONETWORKREGIONSCORES,
  __module__ = 'WUProtos.Data.FlooNetworkRegionScores_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.FlooNetworkRegionScores)
  ))
_sym_db.RegisterMessage(FlooNetworkRegionScores)
_sym_db.RegisterMessage(FlooNetworkRegionScores.PointsPerTeamEntry)


_FLOONETWORKREGIONSCORES_POINTSPERTEAMENTRY._options = None
# @@protoc_insertion_point(module_scope)