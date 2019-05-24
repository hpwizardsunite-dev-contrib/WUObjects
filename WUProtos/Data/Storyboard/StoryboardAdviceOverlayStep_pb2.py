# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Storyboard/StoryboardAdviceOverlayStep.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import SpeechBubble_pb2 as WUProtos_dot_Data_dot_SpeechBubble__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Storyboard/StoryboardAdviceOverlayStep.proto',
  package='WUProtos.Data.Storyboard',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n:WUProtos/Data/Storyboard/StoryboardAdviceOverlayStep.proto\x12\x18WUProtos.Data.Storyboard\x1a WUProtos/Data/SpeechBubble.proto\"\x9c\x02\n\x1bStoryboardAdviceOverlayStep\x12\x32\n\rspeech_bubble\x18\x01 \x01(\x0b\x32\x1b.WUProtos.Data.SpeechBubble\x12\x16\n\x0erequires_scrim\x18\x02 \x01(\x08\x12_\n\talignment\x18\x03 \x01(\x0e\x32L.WUProtos.Data.Storyboard.StoryboardAdviceOverlayStep.AdviceOverlayAlignment\x12!\n\x19show_continue_action_text\x18\x04 \x01(\x08\"-\n\x16\x41\x64viceOverlayAlignment\x12\n\n\x06\x62ottom\x10\x00\x12\x07\n\x03top\x10\x01\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_SpeechBubble__pb2.DESCRIPTOR,])



_STORYBOARDADVICEOVERLAYSTEP_ADVICEOVERLAYALIGNMENT = _descriptor.EnumDescriptor(
  name='AdviceOverlayAlignment',
  full_name='WUProtos.Data.Storyboard.StoryboardAdviceOverlayStep.AdviceOverlayAlignment',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='bottom', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='top', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=362,
  serialized_end=407,
)
_sym_db.RegisterEnumDescriptor(_STORYBOARDADVICEOVERLAYSTEP_ADVICEOVERLAYALIGNMENT)


_STORYBOARDADVICEOVERLAYSTEP = _descriptor.Descriptor(
  name='StoryboardAdviceOverlayStep',
  full_name='WUProtos.Data.Storyboard.StoryboardAdviceOverlayStep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='speech_bubble', full_name='WUProtos.Data.Storyboard.StoryboardAdviceOverlayStep.speech_bubble', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requires_scrim', full_name='WUProtos.Data.Storyboard.StoryboardAdviceOverlayStep.requires_scrim', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alignment', full_name='WUProtos.Data.Storyboard.StoryboardAdviceOverlayStep.alignment', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_continue_action_text', full_name='WUProtos.Data.Storyboard.StoryboardAdviceOverlayStep.show_continue_action_text', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STORYBOARDADVICEOVERLAYSTEP_ADVICEOVERLAYALIGNMENT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=407,
)

_STORYBOARDADVICEOVERLAYSTEP.fields_by_name['speech_bubble'].message_type = WUProtos_dot_Data_dot_SpeechBubble__pb2._SPEECHBUBBLE
_STORYBOARDADVICEOVERLAYSTEP.fields_by_name['alignment'].enum_type = _STORYBOARDADVICEOVERLAYSTEP_ADVICEOVERLAYALIGNMENT
_STORYBOARDADVICEOVERLAYSTEP_ADVICEOVERLAYALIGNMENT.containing_type = _STORYBOARDADVICEOVERLAYSTEP
DESCRIPTOR.message_types_by_name['StoryboardAdviceOverlayStep'] = _STORYBOARDADVICEOVERLAYSTEP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StoryboardAdviceOverlayStep = _reflection.GeneratedProtocolMessageType('StoryboardAdviceOverlayStep', (_message.Message,), dict(
  DESCRIPTOR = _STORYBOARDADVICEOVERLAYSTEP,
  __module__ = 'WUProtos.Data.Storyboard.StoryboardAdviceOverlayStep_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Storyboard.StoryboardAdviceOverlayStep)
  ))
_sym_db.RegisterMessage(StoryboardAdviceOverlayStep)


# @@protoc_insertion_point(module_scope)