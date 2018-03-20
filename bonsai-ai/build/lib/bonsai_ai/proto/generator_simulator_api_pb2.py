# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bonsai/proto/generator_simulator_api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bonsai/proto/generator_simulator_api.proto',
  package='bonsai.proto.generator_simulator_api',
  syntax='proto3',
  serialized_pb=_b('\n*bonsai/proto/generator_simulator_api.proto\x12$bonsai.proto.generator_simulator_api\x1a google/protobuf/descriptor.proto\"]\n\x14SimulationSourceData\x12\r\n\x05state\x18\x01 \x01(\x0c\x12\x0e\n\x06reward\x18\x02 \x01(\x02\x12\x10\n\x08terminal\x18\x03 \x01(\x08\x12\x14\n\x0c\x61\x63tion_taken\x18\x04 \x01(\x0c\"&\n\x0cRegisterData\x12\x16\n\x0esimulator_name\x18\x01 \x01(\t\"\xd9\x02\n\x11SimulatorToServer\x12Y\n\x0cmessage_type\x18\x01 \x01(\x0e\x32\x43.bonsai.proto.generator_simulator_api.SimulatorToServer.MessageType\x12I\n\rregister_data\x18\x02 \x01(\x0b\x32\x32.bonsai.proto.generator_simulator_api.RegisterData\x12N\n\nstate_data\x18\x03 \x03(\x0b\x32:.bonsai.proto.generator_simulator_api.SimulationSourceData\x12\x0e\n\x06sim_id\x18\x04 \x01(\x07\">\n\x0bMessageType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08REGISTER\x10\x01\x12\t\n\x05READY\x10\x02\x12\t\n\x05STATE\x10\x03\"\xdc\x01\n\x17\x41\x63knowledgeRegisterData\x12;\n\x11properties_schema\x18\x01 \x01(\x0b\x32 .google.protobuf.DescriptorProto\x12\x37\n\routput_schema\x18\x02 \x01(\x0b\x32 .google.protobuf.DescriptorProto\x12;\n\x11prediction_schema\x18\x03 \x01(\x0b\x32 .google.protobuf.DescriptorProto\x12\x0e\n\x06sim_id\x18\x04 \x01(\x07\"\x81\x01\n\x11SetPropertiesData\x12\x1a\n\x12\x64ynamic_properties\x18\x01 \x01(\x0c\x12\x13\n\x0breward_name\x18\x02 \x01(\t\x12;\n\x11prediction_schema\x18\x03 \x01(\x0b\x32 .google.protobuf.DescriptorProto\",\n\x0ePredictionData\x12\x1a\n\x12\x64ynamic_prediction\x18\x01 \x01(\x0c\"\x8e\x04\n\x11ServerToSimulator\x12Y\n\x0cmessage_type\x18\x01 \x01(\x0e\x32\x43.bonsai.proto.generator_simulator_api.ServerToSimulator.MessageType\x12`\n\x19\x61\x63knowledge_register_data\x18\x02 \x01(\x0b\x32=.bonsai.proto.generator_simulator_api.AcknowledgeRegisterData\x12T\n\x13set_properties_data\x18\x03 \x01(\x0b\x32\x37.bonsai.proto.generator_simulator_api.SetPropertiesData\x12M\n\x0fprediction_data\x18\x04 \x03(\x0b\x32\x34.bonsai.proto.generator_simulator_api.PredictionData\x12\x0e\n\x06sim_id\x18\x05 \x01(\x07\"\x86\x01\n\x0bMessageType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x18\n\x14\x41\x43KNOWLEDGE_REGISTER\x10\x01\x12\x12\n\x0eSET_PROPERTIES\x10\x02\x12\t\n\x05START\x10\x03\x12\x08\n\x04STOP\x10\x04\x12\x0e\n\nPREDICTION\x10\x05\x12\t\n\x05RESET\x10\x06\x12\x0c\n\x08\x46INISHED\x10\x07\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])



_SIMULATORTOSERVER_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='bonsai.proto.generator_simulator_api.SimulatorToServer.MessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=537,
  serialized_end=599,
)
_sym_db.RegisterEnumDescriptor(_SIMULATORTOSERVER_MESSAGETYPE)

_SERVERTOSIMULATOR_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='bonsai.proto.generator_simulator_api.ServerToSimulator.MessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACKNOWLEDGE_REGISTER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_PROPERTIES', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREDICTION', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESET', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINISHED', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1395,
  serialized_end=1529,
)
_sym_db.RegisterEnumDescriptor(_SERVERTOSIMULATOR_MESSAGETYPE)


_SIMULATIONSOURCEDATA = _descriptor.Descriptor(
  name='SimulationSourceData',
  full_name='bonsai.proto.generator_simulator_api.SimulationSourceData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='bonsai.proto.generator_simulator_api.SimulationSourceData.state', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reward', full_name='bonsai.proto.generator_simulator_api.SimulationSourceData.reward', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='terminal', full_name='bonsai.proto.generator_simulator_api.SimulationSourceData.terminal', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action_taken', full_name='bonsai.proto.generator_simulator_api.SimulationSourceData.action_taken', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=211,
)


_REGISTERDATA = _descriptor.Descriptor(
  name='RegisterData',
  full_name='bonsai.proto.generator_simulator_api.RegisterData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='simulator_name', full_name='bonsai.proto.generator_simulator_api.RegisterData.simulator_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=213,
  serialized_end=251,
)


_SIMULATORTOSERVER = _descriptor.Descriptor(
  name='SimulatorToServer',
  full_name='bonsai.proto.generator_simulator_api.SimulatorToServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_type', full_name='bonsai.proto.generator_simulator_api.SimulatorToServer.message_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='register_data', full_name='bonsai.proto.generator_simulator_api.SimulatorToServer.register_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state_data', full_name='bonsai.proto.generator_simulator_api.SimulatorToServer.state_data', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sim_id', full_name='bonsai.proto.generator_simulator_api.SimulatorToServer.sim_id', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SIMULATORTOSERVER_MESSAGETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=254,
  serialized_end=599,
)


_ACKNOWLEDGEREGISTERDATA = _descriptor.Descriptor(
  name='AcknowledgeRegisterData',
  full_name='bonsai.proto.generator_simulator_api.AcknowledgeRegisterData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='properties_schema', full_name='bonsai.proto.generator_simulator_api.AcknowledgeRegisterData.properties_schema', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_schema', full_name='bonsai.proto.generator_simulator_api.AcknowledgeRegisterData.output_schema', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prediction_schema', full_name='bonsai.proto.generator_simulator_api.AcknowledgeRegisterData.prediction_schema', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sim_id', full_name='bonsai.proto.generator_simulator_api.AcknowledgeRegisterData.sim_id', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=602,
  serialized_end=822,
)


_SETPROPERTIESDATA = _descriptor.Descriptor(
  name='SetPropertiesData',
  full_name='bonsai.proto.generator_simulator_api.SetPropertiesData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dynamic_properties', full_name='bonsai.proto.generator_simulator_api.SetPropertiesData.dynamic_properties', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reward_name', full_name='bonsai.proto.generator_simulator_api.SetPropertiesData.reward_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prediction_schema', full_name='bonsai.proto.generator_simulator_api.SetPropertiesData.prediction_schema', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=825,
  serialized_end=954,
)


_PREDICTIONDATA = _descriptor.Descriptor(
  name='PredictionData',
  full_name='bonsai.proto.generator_simulator_api.PredictionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dynamic_prediction', full_name='bonsai.proto.generator_simulator_api.PredictionData.dynamic_prediction', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=956,
  serialized_end=1000,
)


_SERVERTOSIMULATOR = _descriptor.Descriptor(
  name='ServerToSimulator',
  full_name='bonsai.proto.generator_simulator_api.ServerToSimulator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_type', full_name='bonsai.proto.generator_simulator_api.ServerToSimulator.message_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acknowledge_register_data', full_name='bonsai.proto.generator_simulator_api.ServerToSimulator.acknowledge_register_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='set_properties_data', full_name='bonsai.proto.generator_simulator_api.ServerToSimulator.set_properties_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prediction_data', full_name='bonsai.proto.generator_simulator_api.ServerToSimulator.prediction_data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sim_id', full_name='bonsai.proto.generator_simulator_api.ServerToSimulator.sim_id', index=4,
      number=5, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVERTOSIMULATOR_MESSAGETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1003,
  serialized_end=1529,
)

_SIMULATORTOSERVER.fields_by_name['message_type'].enum_type = _SIMULATORTOSERVER_MESSAGETYPE
_SIMULATORTOSERVER.fields_by_name['register_data'].message_type = _REGISTERDATA
_SIMULATORTOSERVER.fields_by_name['state_data'].message_type = _SIMULATIONSOURCEDATA
_SIMULATORTOSERVER_MESSAGETYPE.containing_type = _SIMULATORTOSERVER
_ACKNOWLEDGEREGISTERDATA.fields_by_name['properties_schema'].message_type = google_dot_protobuf_dot_descriptor__pb2._DESCRIPTORPROTO
_ACKNOWLEDGEREGISTERDATA.fields_by_name['output_schema'].message_type = google_dot_protobuf_dot_descriptor__pb2._DESCRIPTORPROTO
_ACKNOWLEDGEREGISTERDATA.fields_by_name['prediction_schema'].message_type = google_dot_protobuf_dot_descriptor__pb2._DESCRIPTORPROTO
_SETPROPERTIESDATA.fields_by_name['prediction_schema'].message_type = google_dot_protobuf_dot_descriptor__pb2._DESCRIPTORPROTO
_SERVERTOSIMULATOR.fields_by_name['message_type'].enum_type = _SERVERTOSIMULATOR_MESSAGETYPE
_SERVERTOSIMULATOR.fields_by_name['acknowledge_register_data'].message_type = _ACKNOWLEDGEREGISTERDATA
_SERVERTOSIMULATOR.fields_by_name['set_properties_data'].message_type = _SETPROPERTIESDATA
_SERVERTOSIMULATOR.fields_by_name['prediction_data'].message_type = _PREDICTIONDATA
_SERVERTOSIMULATOR_MESSAGETYPE.containing_type = _SERVERTOSIMULATOR
DESCRIPTOR.message_types_by_name['SimulationSourceData'] = _SIMULATIONSOURCEDATA
DESCRIPTOR.message_types_by_name['RegisterData'] = _REGISTERDATA
DESCRIPTOR.message_types_by_name['SimulatorToServer'] = _SIMULATORTOSERVER
DESCRIPTOR.message_types_by_name['AcknowledgeRegisterData'] = _ACKNOWLEDGEREGISTERDATA
DESCRIPTOR.message_types_by_name['SetPropertiesData'] = _SETPROPERTIESDATA
DESCRIPTOR.message_types_by_name['PredictionData'] = _PREDICTIONDATA
DESCRIPTOR.message_types_by_name['ServerToSimulator'] = _SERVERTOSIMULATOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimulationSourceData = _reflection.GeneratedProtocolMessageType('SimulationSourceData', (_message.Message,), dict(
  DESCRIPTOR = _SIMULATIONSOURCEDATA,
  __module__ = 'bonsai.proto.generator_simulator_api_pb2'
  # @@protoc_insertion_point(class_scope:bonsai.proto.generator_simulator_api.SimulationSourceData)
  ))
_sym_db.RegisterMessage(SimulationSourceData)

RegisterData = _reflection.GeneratedProtocolMessageType('RegisterData', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERDATA,
  __module__ = 'bonsai.proto.generator_simulator_api_pb2'
  # @@protoc_insertion_point(class_scope:bonsai.proto.generator_simulator_api.RegisterData)
  ))
_sym_db.RegisterMessage(RegisterData)

SimulatorToServer = _reflection.GeneratedProtocolMessageType('SimulatorToServer', (_message.Message,), dict(
  DESCRIPTOR = _SIMULATORTOSERVER,
  __module__ = 'bonsai.proto.generator_simulator_api_pb2'
  # @@protoc_insertion_point(class_scope:bonsai.proto.generator_simulator_api.SimulatorToServer)
  ))
_sym_db.RegisterMessage(SimulatorToServer)

AcknowledgeRegisterData = _reflection.GeneratedProtocolMessageType('AcknowledgeRegisterData', (_message.Message,), dict(
  DESCRIPTOR = _ACKNOWLEDGEREGISTERDATA,
  __module__ = 'bonsai.proto.generator_simulator_api_pb2'
  # @@protoc_insertion_point(class_scope:bonsai.proto.generator_simulator_api.AcknowledgeRegisterData)
  ))
_sym_db.RegisterMessage(AcknowledgeRegisterData)

SetPropertiesData = _reflection.GeneratedProtocolMessageType('SetPropertiesData', (_message.Message,), dict(
  DESCRIPTOR = _SETPROPERTIESDATA,
  __module__ = 'bonsai.proto.generator_simulator_api_pb2'
  # @@protoc_insertion_point(class_scope:bonsai.proto.generator_simulator_api.SetPropertiesData)
  ))
_sym_db.RegisterMessage(SetPropertiesData)

PredictionData = _reflection.GeneratedProtocolMessageType('PredictionData', (_message.Message,), dict(
  DESCRIPTOR = _PREDICTIONDATA,
  __module__ = 'bonsai.proto.generator_simulator_api_pb2'
  # @@protoc_insertion_point(class_scope:bonsai.proto.generator_simulator_api.PredictionData)
  ))
_sym_db.RegisterMessage(PredictionData)

ServerToSimulator = _reflection.GeneratedProtocolMessageType('ServerToSimulator', (_message.Message,), dict(
  DESCRIPTOR = _SERVERTOSIMULATOR,
  __module__ = 'bonsai.proto.generator_simulator_api_pb2'
  # @@protoc_insertion_point(class_scope:bonsai.proto.generator_simulator_api.ServerToSimulator)
  ))
_sym_db.RegisterMessage(ServerToSimulator)


# @@protoc_insertion_point(module_scope)
