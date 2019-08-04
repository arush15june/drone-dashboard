# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drone.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='drone.proto',
  package='drone',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0b\x64rone.proto\x12\x05\x64rone\"f\n\nDroneState\x12\x0c\n\x04uuid\x18\x01 \x02(\t\x12\x10\n\x08latitude\x18\x02 \x02(\x01\x12\x11\n\tlongitude\x18\x03 \x02(\x01\x12\x12\n\ncurr_speed\x18\x04 \x02(\x01\x12\x11\n\ttimestamp\x18\x05 \x02(\x03')
)




_DRONESTATE = _descriptor.Descriptor(
  name='DroneState',
  full_name='drone.DroneState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='drone.DroneState.uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='drone.DroneState.latitude', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='drone.DroneState.longitude', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='curr_speed', full_name='drone.DroneState.curr_speed', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='drone.DroneState.timestamp', index=4,
      number=5, type=3, cpp_type=2, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=124,
)

DESCRIPTOR.message_types_by_name['DroneState'] = _DRONESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DroneState = _reflection.GeneratedProtocolMessageType('DroneState', (_message.Message,), {
  'DESCRIPTOR' : _DRONESTATE,
  '__module__' : 'drone_pb2'
  # @@protoc_insertion_point(class_scope:drone.DroneState)
  })
_sym_db.RegisterMessage(DroneState)


# @@protoc_insertion_point(module_scope)