# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: narupa/protocol/imd/imd.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from narupa.protocol.instance import get_topology_pb2 as narupa_dot_protocol_dot_instance_dot_get__topology__pb2
from narupa.protocol.instance import get_frame_pb2 as narupa_dot_protocol_dot_instance_dot_get__frame__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='narupa/protocol/imd/imd.proto',
  package='narupa.protocol.imd',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dnarupa/protocol/imd/imd.proto\x12\x13narupa.protocol.imd\x1a+narupa/protocol/instance/get_topology.proto\x1a(narupa/protocol/instance/get_frame.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x12\n\x10InteractionReply\"[\n\x0bInteraction\x12\x10\n\x08position\x18\x01 \x03(\x02\x12\r\n\x05\x61toms\x18\x02 \x03(\x05\x12+\n\nproperties\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct2\xdf\x02\n\x1cInteractiveMolecularDynamics\x12r\n\x11SubscribeTopology\x12,.narupa.protocol.instance.GetTopologyRequest\x1a-.narupa.protocol.instance.GetTopologyResponse0\x01\x12i\n\x0eSubscribeFrame\x12).narupa.protocol.instance.GetFrameRequest\x1a*.narupa.protocol.instance.GetFrameResponse0\x01\x12`\n\x13PublishInteractions\x12 .narupa.protocol.imd.Interaction\x1a%.narupa.protocol.imd.InteractionReply(\x01\x62\x06proto3')
  ,
  dependencies=[narupa_dot_protocol_dot_instance_dot_get__topology__pb2.DESCRIPTOR,narupa_dot_protocol_dot_instance_dot_get__frame__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_INTERACTIONREPLY = _descriptor.Descriptor(
  name='InteractionReply',
  full_name='narupa.protocol.imd.InteractionReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_end=189,
)


_INTERACTION = _descriptor.Descriptor(
  name='Interaction',
  full_name='narupa.protocol.imd.Interaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='narupa.protocol.imd.Interaction.position', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='atoms', full_name='narupa.protocol.imd.Interaction.atoms', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='narupa.protocol.imd.Interaction.properties', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=282,
)

_INTERACTION.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['InteractionReply'] = _INTERACTIONREPLY
DESCRIPTOR.message_types_by_name['Interaction'] = _INTERACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InteractionReply = _reflection.GeneratedProtocolMessageType('InteractionReply', (_message.Message,), dict(
  DESCRIPTOR = _INTERACTIONREPLY,
  __module__ = 'narupa.protocol.imd.imd_pb2'
  # @@protoc_insertion_point(class_scope:narupa.protocol.imd.InteractionReply)
  ))
_sym_db.RegisterMessage(InteractionReply)

Interaction = _reflection.GeneratedProtocolMessageType('Interaction', (_message.Message,), dict(
  DESCRIPTOR = _INTERACTION,
  __module__ = 'narupa.protocol.imd.imd_pb2'
  # @@protoc_insertion_point(class_scope:narupa.protocol.imd.Interaction)
  ))
_sym_db.RegisterMessage(Interaction)



_INTERACTIVEMOLECULARDYNAMICS = _descriptor.ServiceDescriptor(
  name='InteractiveMolecularDynamics',
  full_name='narupa.protocol.imd.InteractiveMolecularDynamics',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=285,
  serialized_end=636,
  methods=[
  _descriptor.MethodDescriptor(
    name='SubscribeTopology',
    full_name='narupa.protocol.imd.InteractiveMolecularDynamics.SubscribeTopology',
    index=0,
    containing_service=None,
    input_type=narupa_dot_protocol_dot_instance_dot_get__topology__pb2._GETTOPOLOGYREQUEST,
    output_type=narupa_dot_protocol_dot_instance_dot_get__topology__pb2._GETTOPOLOGYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeFrame',
    full_name='narupa.protocol.imd.InteractiveMolecularDynamics.SubscribeFrame',
    index=1,
    containing_service=None,
    input_type=narupa_dot_protocol_dot_instance_dot_get__frame__pb2._GETFRAMEREQUEST,
    output_type=narupa_dot_protocol_dot_instance_dot_get__frame__pb2._GETFRAMERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PublishInteractions',
    full_name='narupa.protocol.imd.InteractiveMolecularDynamics.PublishInteractions',
    index=2,
    containing_service=None,
    input_type=_INTERACTION,
    output_type=_INTERACTIONREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_INTERACTIVEMOLECULARDYNAMICS)

DESCRIPTOR.services_by_name['InteractiveMolecularDynamics'] = _INTERACTIVEMOLECULARDYNAMICS

# @@protoc_insertion_point(module_scope)
