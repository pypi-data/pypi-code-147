# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arg_services/mining_explanation/v1/adu.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,arg_services/mining_explanation/v1/adu.proto\x12\"arg_services.mining_explanation.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\"\x80\x01\n\x15\x43lassificationRequest\x12\x1a\n\x08language\x18\x01 \x01(\tR\x08language\x12\x1a\n\x08segments\x18\x02 \x03(\tR\x08segments\x12/\n\x06\x65xtras\x18\x0f \x01(\x0b\x32\x17.google.protobuf.StructR\x06\x65xtras\"\x92\x01\n\x16\x43lassificationResponse\x12G\n\x08segments\x18\x01 \x03(\x0b\x32+.arg_services.mining_explanation.v1.SegmentR\x08segments\x12/\n\x06\x65xtras\x18\x0f \x01(\x0b\x32\x17.google.protobuf.StructR\x06\x65xtras\"L\n\x07Segment\x12\'\n\x0fkeyword_markers\x18\x01 \x03(\x08R\x0ekeywordMarkers\x12\x18\n\x07\x63lauses\x18\x02 \x03(\tR\x07\x63lauses2\xd7\x01\n\x15\x41\x64uExplanationService\x12\xbd\x01\n\x0e\x43lassification\x12\x39.arg_services.mining_explanation.v1.ClassificationRequest\x1a:.arg_services.mining_explanation.v1.ClassificationResponse\"4\x82\xd3\xe4\x93\x02.:\x01*\")/mining_explanation/v1/adu/classificationB\xd4\x01\n&com.arg_services.mining_explanation.v1B\x08\x41\x64uProtoP\x01\xa2\x02\x03\x41MX\xaa\x02 ArgServices.MiningExplanation.V1\xca\x02 ArgServices\\MiningExplanation\\V1\xe2\x02,ArgServices\\MiningExplanation\\V1\\GPBMetadata\xea\x02\"ArgServices::MiningExplanation::V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'arg_services.mining_explanation.v1.adu_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&com.arg_services.mining_explanation.v1B\010AduProtoP\001\242\002\003AMX\252\002 ArgServices.MiningExplanation.V1\312\002 ArgServices\\MiningExplanation\\V1\342\002,ArgServices\\MiningExplanation\\V1\\GPBMetadata\352\002\"ArgServices::MiningExplanation::V1'
  _ADUEXPLANATIONSERVICE.methods_by_name['Classification']._options = None
  _ADUEXPLANATIONSERVICE.methods_by_name['Classification']._serialized_options = b'\202\323\344\223\002.:\001*\")/mining_explanation/v1/adu/classification'
  _CLASSIFICATIONREQUEST._serialized_start=145
  _CLASSIFICATIONREQUEST._serialized_end=273
  _CLASSIFICATIONRESPONSE._serialized_start=276
  _CLASSIFICATIONRESPONSE._serialized_end=422
  _SEGMENT._serialized_start=424
  _SEGMENT._serialized_end=500
  _ADUEXPLANATIONSERVICE._serialized_start=503
  _ADUEXPLANATIONSERVICE._serialized_end=718
# @@protoc_insertion_point(module_scope)
