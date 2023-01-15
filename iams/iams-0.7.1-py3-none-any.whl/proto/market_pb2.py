# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: market.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cmarket.proto\x12\nims.market\x1a\x19google/protobuf/any.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x17\n\x06\x43\x61ncel\x12\r\n\x05order\x18\x01 \x01(\t\"^\n\x08Material\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0e\n\x06\x63onfig\x18\x03 \x01(\x0c\x12\x10\n\x08quantity\x18\x04 \x01(\x05\"K\n\x07\x41\x62ility\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0e\n\x06\x63onfig\x18\x03 \x01(\x0c\"\xeb\x01\n\x04Step\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05group\x18\x02 \x01(\t\x12\x0f\n\x07primary\x18\x03 \x01(\x08\x12\r\n\x05\x65\x64ges\x18\x04 \x03(\t\x12&\n\tabilities\x18\x05 \x03(\x0b\x32\x13.ims.market.Ability\x12\'\n\tmaterials\x18\x06 \x03(\x0b\x32\x14.ims.market.Material\x12)\n\x05start\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x06\x66inish\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa0\x01\n\tScheduler\x12\x0c\n\x04\x63ost\x18\x01 \x01(\x01\x12/\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x12\x12\n\x08relative\x18\x03 \x01(\x01H\x00\x12\x12\n\x08skip_eta\x18\x04 \x01(\x08H\x00\x12\x12\n\ntime_queue\x18\x05 \x01(\x01\x12\x11\n\ttime_work\x18\x06 \x01(\x01\x42\x05\n\x03\x65ta\"<\n\nProduction\x12\r\n\x05order\x18\x01 \x01(\t\x12\x1f\n\x05steps\x18\x03 \x03(\x0b\x32\x10.ims.market.Step\"\x84\x01\n\tTransport\x12\r\n\x05order\x18\x01 \x01(\t\x12\x11\n\tinterface\x18\x02 \x01(\t\x12\x14\n\x0ctarget_agent\x18\x03 \x01(\t\x12\x18\n\x10target_interface\x18\x04 \x01(\t\x12%\n\x07payload\x18\x05 \x01(\x0b\x32\x14.google.protobuf.Any\"\x8b\x02\n\x04Task\x12\r\n\x05\x61gent\x18\x01 \x01(\t\x12\x11\n\tinterface\x18\x02 \x01(\t\x12(\n\tscheduler\x18\x03 \x01(\x0b\x32\x15.ims.market.Scheduler\x12*\n\ttransport\x18\x04 \x01(\x0b\x32\x15.ims.market.TransportH\x00\x12,\n\nproduction\x18\x05 \x01(\x0b\x32\x16.ims.market.ProductionH\x00\x12)\n\x05start\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x06\x66inish\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x06\n\x04\x64\x61ta\"]\n\x05Order\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12\x1f\n\x05steps\x18\x02 \x03(\x0b\x32\x10.ims.market.Step\x12\x1f\n\x05tasks\x18\x03 \x03(\x0b\x32\x10.ims.market.Task2\r\n\x0bOrderMaster2\xa6\x03\n\x0bOrderMinion\x12\x45\n\x11production_assign\x12\x16.ims.market.Production\x1a\x16.ims.market.Production\"\x00\x12\x41\n\x11production_cancel\x12\x12.ims.market.Cancel\x1a\x16.google.protobuf.Empty\"\x00\x12\x44\n\x10production_offer\x12\x16.ims.market.Production\x1a\x16.ims.market.Production\"\x00\x12\x42\n\x10transport_assign\x12\x15.ims.market.Transport\x1a\x15.ims.market.Transport\"\x00\x12@\n\x10transport_cancel\x12\x12.ims.market.Cancel\x1a\x16.google.protobuf.Empty\"\x00\x12\x41\n\x0ftransport_offer\x12\x15.ims.market.Transport\x1a\x15.ims.market.Transport\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'market_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CANCEL._serialized_start=117
  _CANCEL._serialized_end=140
  _MATERIAL._serialized_start=142
  _MATERIAL._serialized_end=236
  _ABILITY._serialized_start=238
  _ABILITY._serialized_end=313
  _STEP._serialized_start=316
  _STEP._serialized_end=551
  _SCHEDULER._serialized_start=554
  _SCHEDULER._serialized_end=714
  _PRODUCTION._serialized_start=716
  _PRODUCTION._serialized_end=776
  _TRANSPORT._serialized_start=779
  _TRANSPORT._serialized_end=911
  _TASK._serialized_start=914
  _TASK._serialized_end=1181
  _ORDER._serialized_start=1183
  _ORDER._serialized_end=1276
  _ORDERMASTER._serialized_start=1278
  _ORDERMASTER._serialized_end=1291
  _ORDERMINION._serialized_start=1294
  _ORDERMINION._serialized_end=1716
# @@protoc_insertion_point(module_scope)
