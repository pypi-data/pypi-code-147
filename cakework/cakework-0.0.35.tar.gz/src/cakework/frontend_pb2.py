# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/frontend.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14proto/frontend.proto\x12\x08\x66rontend\"P\n\x0f\x43\x61llTaskRequest\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x0b\n\x03\x61pp\x18\x02 \x01(\t\x12\x0c\n\x04task\x18\x03 \x01(\t\x12\x12\n\nparameters\x18\x04 \x01(\t\"1\n\rCallTaskReply\x12\x11\n\trequestId\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\t2L\n\x08\x46rontend\x12@\n\x08\x43\x61llTask\x12\x19.frontend.CallTaskRequest\x1a\x17.frontend.CallTaskReply\"\x00\x42\x0cZ\n.;frontendb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.frontend_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\n.;frontend'
  _CALLTASKREQUEST._serialized_start=34
  _CALLTASKREQUEST._serialized_end=114
  _CALLTASKREPLY._serialized_start=116
  _CALLTASKREPLY._serialized_end=165
  _FRONTEND._serialized_start=167
  _FRONTEND._serialized_end=243
# @@protoc_insertion_point(module_scope)
