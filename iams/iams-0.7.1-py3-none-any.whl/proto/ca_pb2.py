# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ca.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08\x63\x61.proto\x12\riams.servicer\"%\n\x07Request\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04hard\x18\x02 \x01(\x08\"4\n\x08Response\x12\x13\n\x0bprivate_key\x18\x01 \x01(\t\x12\x13\n\x0b\x63\x65rtificate\x18\x02 \x01(\t2R\n\x14\x43\x65rtificateAuthority\x12:\n\x05renew\x12\x16.iams.servicer.Request\x1a\x17.iams.servicer.Response\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ca_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=27
  _REQUEST._serialized_end=64
  _RESPONSE._serialized_start=66
  _RESPONSE._serialized_end=118
  _CERTIFICATEAUTHORITY._serialized_start=120
  _CERTIFICATEAUTHORITY._serialized_end=202
# @@protoc_insertion_point(module_scope)
