# Copyright 2022 The XFL Authors. All rights reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: commu.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='commu.proto',
  package='commu',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x63ommu.proto\x12\x05\x63ommu\")\n\x0bPostRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"\x1c\n\x0cPostResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x62\x06proto3'
)




_POSTREQUEST = _descriptor.Descriptor(
  name='PostRequest',
  full_name='commu.PostRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='commu.PostRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='commu.PostRequest.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=22,
  serialized_end=63,
)


_POSTRESPONSE = _descriptor.Descriptor(
  name='PostResponse',
  full_name='commu.PostResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='commu.PostResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=65,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['PostRequest'] = _POSTREQUEST
DESCRIPTOR.message_types_by_name['PostResponse'] = _POSTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PostRequest = _reflection.GeneratedProtocolMessageType('PostRequest', (_message.Message,), {
  'DESCRIPTOR' : _POSTREQUEST,
  '__module__' : 'commu_pb2'
  # @@protoc_insertion_point(class_scope:commu.PostRequest)
  })
_sym_db.RegisterMessage(PostRequest)

PostResponse = _reflection.GeneratedProtocolMessageType('PostResponse', (_message.Message,), {
  'DESCRIPTOR' : _POSTRESPONSE,
  '__module__' : 'commu_pb2'
  # @@protoc_insertion_point(class_scope:commu.PostResponse)
  })
_sym_db.RegisterMessage(PostResponse)


# @@protoc_insertion_point(module_scope)
