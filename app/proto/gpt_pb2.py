# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gpt.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tgpt.proto\x12\x0bgpt_starter\"A\n\x0bGPTResponse\x12\r\n\x05reply\x18\x01 \x01(\t\x12\x0e\n\x06prompt\x18\x02 \x01(\t\x12\x13\n\x0btoken_count\x18\x03 \x01(\x04\"\x1b\n\nGPTRequest\x12\r\n\x05query\x18\x01 \x01(\t')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gpt_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_GPTRESPONSE']._serialized_start=26
  _globals['_GPTRESPONSE']._serialized_end=91
  _globals['_GPTREQUEST']._serialized_start=93
  _globals['_GPTREQUEST']._serialized_end=120
# @@protoc_insertion_point(module_scope)
