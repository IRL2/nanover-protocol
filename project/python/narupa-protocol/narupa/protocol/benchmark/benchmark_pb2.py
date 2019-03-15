# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: narupa/protocol/benchmark/benchmark.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from narupa.protocol.instance import get_frame_pb2 as narupa_dot_protocol_dot_instance_dot_get__frame__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='narupa/protocol/benchmark/benchmark.proto',
  package='narupa.protocol.benchmark',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n)narupa/protocol/benchmark/benchmark.proto\x12\x19narupa.protocol.benchmark\x1a(narupa/protocol/instance/get_frame.proto\" \n\rSimpleMessage\x12\x0f\n\x07payload\x18\x01 \x01(\x05\"4\n\x0fGetFrameRequest\x12\x0f\n\x07n_atoms\x18\x01 \x01(\x05\x12\x10\n\x08n_frames\x18\x02 \x01(\x05\"\x19\n\x08RawFrame\x12\r\n\x05\x66rame\x18\x01 \x03(\x02\"\x19\n\x08RawBytes\x12\r\n\x05\x62ytes\x18\x01 \x01(\x0c\x32\xb2\x03\n\x0eStreamProvider\x12\x66\n\x10GetSimpleMessage\x12(.narupa.protocol.benchmark.SimpleMessage\x1a(.narupa.protocol.benchmark.SimpleMessage\x12\x65\n\tGetFrames\x12*.narupa.protocol.benchmark.GetFrameRequest\x1a*.narupa.protocol.instance.GetFrameResponse0\x01\x12\x61\n\x0cGetFramesRaw\x12*.narupa.protocol.benchmark.GetFrameRequest\x1a#.narupa.protocol.benchmark.RawFrame0\x01\x12n\n\x12GetFramesThrottled\x12*.narupa.protocol.benchmark.GetFrameRequest\x1a*.narupa.protocol.instance.GetFrameResponse0\x01\x62\x06proto3')
  ,
  dependencies=[narupa_dot_protocol_dot_instance_dot_get__frame__pb2.DESCRIPTOR,])




_SIMPLEMESSAGE = _descriptor.Descriptor(
  name='SimpleMessage',
  full_name='narupa.protocol.benchmark.SimpleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='narupa.protocol.benchmark.SimpleMessage.payload', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=114,
  serialized_end=146,
)


_GETFRAMEREQUEST = _descriptor.Descriptor(
  name='GetFrameRequest',
  full_name='narupa.protocol.benchmark.GetFrameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n_atoms', full_name='narupa.protocol.benchmark.GetFrameRequest.n_atoms', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n_frames', full_name='narupa.protocol.benchmark.GetFrameRequest.n_frames', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=148,
  serialized_end=200,
)


_RAWFRAME = _descriptor.Descriptor(
  name='RawFrame',
  full_name='narupa.protocol.benchmark.RawFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame', full_name='narupa.protocol.benchmark.RawFrame.frame', index=0,
      number=1, type=2, cpp_type=6, label=3,
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
  serialized_start=202,
  serialized_end=227,
)


_RAWBYTES = _descriptor.Descriptor(
  name='RawBytes',
  full_name='narupa.protocol.benchmark.RawBytes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bytes', full_name='narupa.protocol.benchmark.RawBytes.bytes', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=229,
  serialized_end=254,
)

DESCRIPTOR.message_types_by_name['SimpleMessage'] = _SIMPLEMESSAGE
DESCRIPTOR.message_types_by_name['GetFrameRequest'] = _GETFRAMEREQUEST
DESCRIPTOR.message_types_by_name['RawFrame'] = _RAWFRAME
DESCRIPTOR.message_types_by_name['RawBytes'] = _RAWBYTES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimpleMessage = _reflection.GeneratedProtocolMessageType('SimpleMessage', (_message.Message,), dict(
  DESCRIPTOR = _SIMPLEMESSAGE,
  __module__ = 'narupa.protocol.benchmark.benchmark_pb2'
  # @@protoc_insertion_point(class_scope:narupa.protocol.benchmark.SimpleMessage)
  ))
_sym_db.RegisterMessage(SimpleMessage)

GetFrameRequest = _reflection.GeneratedProtocolMessageType('GetFrameRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFRAMEREQUEST,
  __module__ = 'narupa.protocol.benchmark.benchmark_pb2'
  # @@protoc_insertion_point(class_scope:narupa.protocol.benchmark.GetFrameRequest)
  ))
_sym_db.RegisterMessage(GetFrameRequest)

RawFrame = _reflection.GeneratedProtocolMessageType('RawFrame', (_message.Message,), dict(
  DESCRIPTOR = _RAWFRAME,
  __module__ = 'narupa.protocol.benchmark.benchmark_pb2'
  # @@protoc_insertion_point(class_scope:narupa.protocol.benchmark.RawFrame)
  ))
_sym_db.RegisterMessage(RawFrame)

RawBytes = _reflection.GeneratedProtocolMessageType('RawBytes', (_message.Message,), dict(
  DESCRIPTOR = _RAWBYTES,
  __module__ = 'narupa.protocol.benchmark.benchmark_pb2'
  # @@protoc_insertion_point(class_scope:narupa.protocol.benchmark.RawBytes)
  ))
_sym_db.RegisterMessage(RawBytes)



_STREAMPROVIDER = _descriptor.ServiceDescriptor(
  name='StreamProvider',
  full_name='narupa.protocol.benchmark.StreamProvider',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=257,
  serialized_end=691,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSimpleMessage',
    full_name='narupa.protocol.benchmark.StreamProvider.GetSimpleMessage',
    index=0,
    containing_service=None,
    input_type=_SIMPLEMESSAGE,
    output_type=_SIMPLEMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetFrames',
    full_name='narupa.protocol.benchmark.StreamProvider.GetFrames',
    index=1,
    containing_service=None,
    input_type=_GETFRAMEREQUEST,
    output_type=narupa_dot_protocol_dot_instance_dot_get__frame__pb2._GETFRAMERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetFramesRaw',
    full_name='narupa.protocol.benchmark.StreamProvider.GetFramesRaw',
    index=2,
    containing_service=None,
    input_type=_GETFRAMEREQUEST,
    output_type=_RAWFRAME,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetFramesThrottled',
    full_name='narupa.protocol.benchmark.StreamProvider.GetFramesThrottled',
    index=3,
    containing_service=None,
    input_type=_GETFRAMEREQUEST,
    output_type=narupa_dot_protocol_dot_instance_dot_get__frame__pb2._GETFRAMERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAMPROVIDER)

DESCRIPTOR.services_by_name['StreamProvider'] = _STREAMPROVIDER

# @@protoc_insertion_point(module_scope)
