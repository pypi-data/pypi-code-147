# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: framework.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x66ramework.proto\x12\riams.servicer\x1a\x1bgoogle/protobuf/empty.proto\"\x1e\n\x0c\x41gentRequest\x12\x0e\n\x06\x66ilter\x18\x01 \x03(\t\"*\n\x0cRenewRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04hard\x18\x02 \x01(\x08\"9\n\rRenewResponse\x12\x13\n\x0bprivate_key\x18\x01 \x01(\t\x12\x13\n\x0b\x63\x65rtificate\x18\x02 \x01(\t\"\xa5\x01\n\tAgentData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\r\x12\r\n\x05image\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x06 \x01(\x0c\x12\x11\n\tautostart\x18\x07 \x01(\x08\x12\x13\n\x0b\x63onstraints\x18\x08 \x03(\t\x12\x13\n\x0bpreferences\x18\t \x03(\t\"\\\n\x04\x45\x64ge\x12\x11\n\tnode_from\x18\x01 \x01(\t\x12\x0f\n\x07node_to\x18\x02 \x01(\t\x12\r\n\x05\x61gent\x18\x03 \x01(\t\x12\x0e\n\x06weight\x18\x04 \x01(\x01\x12\x11\n\tsymmetric\x18\x05 \x01(\x08\"]\n\x04Node\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x01 \x01(\t\x12\r\n\x05pools\x18\x02 \x03(\t\x12\"\n\x05\x65\x64ges\x18\x03 \x03(\x0b\x32\x13.iams.servicer.Edge\x12\x11\n\tabilities\x18\x04 \x03(\t2\x81\x05\n\tFramework\x12\x43\n\x06\x61gents\x12\x1b.iams.servicer.AgentRequest\x1a\x18.iams.servicer.AgentData\"\x00\x30\x01\x12:\n\x06\x62ooted\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12\x44\n\x05renew\x12\x1b.iams.servicer.RenewRequest\x1a\x1c.iams.servicer.RenewResponse\"\x00\x12>\n\x06\x63reate\x12\x18.iams.servicer.AgentData\x1a\x18.iams.servicer.AgentData\"\x00\x12>\n\x06update\x12\x18.iams.servicer.AgentData\x1a\x18.iams.servicer.AgentData\"\x00\x12=\n\x07\x64\x65stroy\x12\x18.iams.servicer.AgentData\x1a\x16.google.protobuf.Empty\"\x00\x12;\n\x05sleep\x12\x18.iams.servicer.AgentData\x1a\x16.google.protobuf.Empty\"\x00\x12=\n\x07upgrade\x12\x18.iams.servicer.AgentData\x1a\x16.google.protobuf.Empty\"\x00\x12\x36\n\x08topology\x12\x13.iams.servicer.Node\x1a\x13.iams.servicer.Node\"\x00\x12:\n\x04wake\x12\x18.iams.servicer.AgentData\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'framework_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AGENTREQUEST._serialized_start=63
  _AGENTREQUEST._serialized_end=93
  _RENEWREQUEST._serialized_start=95
  _RENEWREQUEST._serialized_end=137
  _RENEWRESPONSE._serialized_start=139
  _RENEWRESPONSE._serialized_end=196
  _AGENTDATA._serialized_start=199
  _AGENTDATA._serialized_end=364
  _EDGE._serialized_start=366
  _EDGE._serialized_end=458
  _NODE._serialized_start=460
  _NODE._serialized_end=553
  _FRAMEWORK._serialized_start=556
  _FRAMEWORK._serialized_end=1197
# @@protoc_insertion_point(module_scope)
