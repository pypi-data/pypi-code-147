# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arg_services/mining/v1/entailment.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from arg_services.mining.v1 import adu_pb2 as arg__services_dot_mining_dot_v1_dot_adu__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'arg_services/mining/v1/entailment.proto\x12\x16\x61rg_services.mining.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a arg_services/mining/v1/adu.proto\x1a\x1cgoogle/api/annotations.proto\"\x90\x01\n\x11\x45ntailmentRequest\x12\x1a\n\x08language\x18\x01 \x01(\tR\x08language\x12\x18\n\x07premise\x18\x02 \x01(\tR\x07premise\x12\x14\n\x05\x63laim\x18\x03 \x01(\tR\x05\x63laim\x12/\n\x06\x65xtras\x18\x0f \x01(\x0b\x32\x17.google.protobuf.StructR\x06\x65xtras\"\xe6\x01\n\x12\x45ntailmentResponse\x12O\n\x0f\x65ntailment_type\x18\x01 \x01(\x0e\x32&.arg_services.mining.v1.EntailmentTypeR\x0e\x65ntailmentType\x12N\n\x0bpredictions\x18\x02 \x03(\x0b\x32,.arg_services.mining.v1.EntailmentPredictionR\x0bpredictions\x12/\n\x06\x65xtras\x18\x0f \x01(\x0b\x32\x17.google.protobuf.StructR\x06\x65xtras\"\x95\x02\n\x12\x45ntailmentsRequest\x12\x1a\n\x08language\x18\x01 \x01(\tR\x08language\x12T\n\x08segments\x18\x02 \x03(\x0b\x32\x38.arg_services.mining.v1.EntailmentsRequest.SegmentsEntryR\x08segments\x12/\n\x06\x65xtras\x18\x0f \x01(\x0b\x32\x17.google.protobuf.StructR\x06\x65xtras\x1a\\\n\rSegmentsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32\x1f.arg_services.mining.v1.SegmentR\x05value:\x02\x38\x01\"\x8a\x01\n\x13\x45ntailmentsResponse\x12\x42\n\x07results\x18\x01 \x03(\x0b\x32(.arg_services.mining.v1.EntailmentResultR\x07results\x12/\n\x06\x65xtras\x18\x0f \x01(\x0b\x32\x17.google.protobuf.StructR\x06\x65xtras\"\xa6\x01\n\x10\x45ntailmentResult\x12\x42\n\nentailment\x18\x01 \x01(\x0b\x32\".arg_services.mining.v1.EntailmentR\nentailment\x12N\n\x0bpredictions\x18\x02 \x03(\x0b\x32,.arg_services.mining.v1.EntailmentPredictionR\x0bpredictions\"\x82\x01\n\nEntailment\x12\x1d\n\npremise_id\x18\x01 \x01(\tR\tpremiseId\x12\x19\n\x08\x63laim_id\x18\x02 \x01(\tR\x07\x63laimId\x12:\n\x04type\x18\x03 \x01(\x0e\x32&.arg_services.mining.v1.EntailmentTypeR\x04type\"t\n\x14\x45ntailmentPrediction\x12 \n\x0bprobability\x18\x01 \x01(\x01R\x0bprobability\x12:\n\x04type\x18\x02 \x01(\x0e\x32&.arg_services.mining.v1.EntailmentTypeR\x04type*\x91\x01\n\x0e\x45ntailmentType\x12\x1f\n\x1b\x45NTAILMENT_TYPE_UNSPECIFIED\x10\x00\x12\x1e\n\x1a\x45NTAILMENT_TYPE_ENTAILMENT\x10\x01\x12!\n\x1d\x45NTAILMENT_TYPE_CONTRADICTION\x10\x02\x12\x1b\n\x17\x45NTAILMENT_TYPE_NEUTRAL\x10\x03\x32\xa7\x02\n\x11\x45ntailmentService\x12\x85\x01\n\nEntailment\x12).arg_services.mining.v1.EntailmentRequest\x1a*.arg_services.mining.v1.EntailmentResponse\" \x82\xd3\xe4\x93\x02\x1a:\x01*\"\x15/mining/v1/entailment\x12\x89\x01\n\x0b\x45ntailments\x12*.arg_services.mining.v1.EntailmentsRequest\x1a+.arg_services.mining.v1.EntailmentsResponse\"!\x82\xd3\xe4\x93\x02\x1b:\x01*\"\x16/mining/v1/entailmentsB\xa3\x01\n\x1a\x63om.arg_services.mining.v1B\x0f\x45ntailmentProtoP\x01\xa2\x02\x03\x41MX\xaa\x02\x15\x41rgServices.Mining.V1\xca\x02\x15\x41rgServices\\Mining\\V1\xe2\x02!ArgServices\\Mining\\V1\\GPBMetadata\xea\x02\x17\x41rgServices::Mining::V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'arg_services.mining.v1.entailment_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.arg_services.mining.v1B\017EntailmentProtoP\001\242\002\003AMX\252\002\025ArgServices.Mining.V1\312\002\025ArgServices\\Mining\\V1\342\002!ArgServices\\Mining\\V1\\GPBMetadata\352\002\027ArgServices::Mining::V1'
  _ENTAILMENTSREQUEST_SEGMENTSENTRY._options = None
  _ENTAILMENTSREQUEST_SEGMENTSENTRY._serialized_options = b'8\001'
  _ENTAILMENTSERVICE.methods_by_name['Entailment']._options = None
  _ENTAILMENTSERVICE.methods_by_name['Entailment']._serialized_options = b'\202\323\344\223\002\032:\001*\"\025/mining/v1/entailment'
  _ENTAILMENTSERVICE.methods_by_name['Entailments']._options = None
  _ENTAILMENTSERVICE.methods_by_name['Entailments']._serialized_options = b'\202\323\344\223\002\033:\001*\"\026/mining/v1/entailments'
  _ENTAILMENTTYPE._serialized_start=1383
  _ENTAILMENTTYPE._serialized_end=1528
  _ENTAILMENTREQUEST._serialized_start=162
  _ENTAILMENTREQUEST._serialized_end=306
  _ENTAILMENTRESPONSE._serialized_start=309
  _ENTAILMENTRESPONSE._serialized_end=539
  _ENTAILMENTSREQUEST._serialized_start=542
  _ENTAILMENTSREQUEST._serialized_end=819
  _ENTAILMENTSREQUEST_SEGMENTSENTRY._serialized_start=727
  _ENTAILMENTSREQUEST_SEGMENTSENTRY._serialized_end=819
  _ENTAILMENTSRESPONSE._serialized_start=822
  _ENTAILMENTSRESPONSE._serialized_end=960
  _ENTAILMENTRESULT._serialized_start=963
  _ENTAILMENTRESULT._serialized_end=1129
  _ENTAILMENT._serialized_start=1132
  _ENTAILMENT._serialized_end=1262
  _ENTAILMENTPREDICTION._serialized_start=1264
  _ENTAILMENTPREDICTION._serialized_end=1380
  _ENTAILMENTSERVICE._serialized_start=1531
  _ENTAILMENTSERVICE._serialized_end=1826
# @@protoc_insertion_point(module_scope)
