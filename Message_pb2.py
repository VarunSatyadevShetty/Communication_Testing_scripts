# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rMessage.proto\"\"\n\x07Request\x12\x17\n\x0fsendcommandflag\x18\x01 \x01(\t\"\x1e\n\x08Response\x12\x12\n\ndata_array\x18\x01 \x03(\x02\x32\x36\n\x14\x43ommunicationService\x12\x1e\n\x05Input\x12\x08.Request\x1a\t.Response\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=17
  _REQUEST._serialized_end=51
  _RESPONSE._serialized_start=53
  _RESPONSE._serialized_end=83
  _COMMUNICATIONSERVICE._serialized_start=85
  _COMMUNICATIONSERVICE._serialized_end=139
# @@protoc_insertion_point(module_scope)
