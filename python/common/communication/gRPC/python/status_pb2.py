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
# source: status.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='status.proto',
  package='status',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cstatus.proto\x12\x06status\"&\n\x06Status\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\t\"\x1e\n\rStatusRequest\x12\r\n\x05jobId\x18\x01 \x01(\x05\"\xf3\x01\n\x0eStatusResponse\x12\r\n\x05jobId\x18\x01 \x01(\x05\x12!\n\tjobStatus\x18\x02 \x01(\x0b\x32\x0e.status.Status\x12\'\n\x0fschedulerStatus\x18\x03 \x01(\x0b\x32\x0e.status.Status\x12@\n\rtrainerStatus\x18\x04 \x03(\x0b\x32).status.StatusResponse.TrainerStatusEntry\x1a\x44\n\x12TrainerStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.status.Status:\x02\x38\x01*m\n\nStatusEnum\x12\n\n\x06STATUS\x10\x00\x12\x08\n\x04IDLE\x10\x01\x12\x0c\n\x08TRAINING\x10\x02\x12\x0e\n\nSUCCESSFUL\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\x0f\n\x0bSTART_TRAIN\x10\x05\x12\x0e\n\nSTOP_TRAIN\x10\x06\x62\x06proto3'
)

_STATUSENUM = _descriptor.EnumDescriptor(
  name='StatusEnum',
  full_name='status.StatusEnum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IDLE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRAINING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCESSFUL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='START_TRAIN', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOP_TRAIN', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=342,
  serialized_end=451,
)
_sym_db.RegisterEnumDescriptor(_STATUSENUM)

StatusEnum = enum_type_wrapper.EnumTypeWrapper(_STATUSENUM)
STATUS = 0
IDLE = 1
TRAINING = 2
SUCCESSFUL = 3
FAILED = 4
START_TRAIN = 5
STOP_TRAIN = 6



_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='status.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='status.Status.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='status.Status.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=24,
  serialized_end=62,
)


_STATUSREQUEST = _descriptor.Descriptor(
  name='StatusRequest',
  full_name='status.StatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobId', full_name='status.StatusRequest.jobId', index=0,
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
  serialized_start=64,
  serialized_end=94,
)


_STATUSRESPONSE_TRAINERSTATUSENTRY = _descriptor.Descriptor(
  name='TrainerStatusEntry',
  full_name='status.StatusResponse.TrainerStatusEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='status.StatusResponse.TrainerStatusEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='status.StatusResponse.TrainerStatusEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=340,
)

_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='status.StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobId', full_name='status.StatusResponse.jobId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jobStatus', full_name='status.StatusResponse.jobStatus', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schedulerStatus', full_name='status.StatusResponse.schedulerStatus', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trainerStatus', full_name='status.StatusResponse.trainerStatus', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_STATUSRESPONSE_TRAINERSTATUSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=340,
)

_STATUSRESPONSE_TRAINERSTATUSENTRY.fields_by_name['value'].message_type = _STATUS
_STATUSRESPONSE_TRAINERSTATUSENTRY.containing_type = _STATUSRESPONSE
_STATUSRESPONSE.fields_by_name['jobStatus'].message_type = _STATUS
_STATUSRESPONSE.fields_by_name['schedulerStatus'].message_type = _STATUS
_STATUSRESPONSE.fields_by_name['trainerStatus'].message_type = _STATUSRESPONSE_TRAINERSTATUSENTRY
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['StatusRequest'] = _STATUSREQUEST
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
DESCRIPTOR.enum_types_by_name['StatusEnum'] = _STATUSENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'status_pb2'
  # @@protoc_insertion_point(class_scope:status.Status)
  })
_sym_db.RegisterMessage(Status)

StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATUSREQUEST,
  '__module__' : 'status_pb2'
  # @@protoc_insertion_point(class_scope:status.StatusRequest)
  })
_sym_db.RegisterMessage(StatusRequest)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), {

  'TrainerStatusEntry' : _reflection.GeneratedProtocolMessageType('TrainerStatusEntry', (_message.Message,), {
    'DESCRIPTOR' : _STATUSRESPONSE_TRAINERSTATUSENTRY,
    '__module__' : 'status_pb2'
    # @@protoc_insertion_point(class_scope:status.StatusResponse.TrainerStatusEntry)
    })
  ,
  'DESCRIPTOR' : _STATUSRESPONSE,
  '__module__' : 'status_pb2'
  # @@protoc_insertion_point(class_scope:status.StatusResponse)
  })
_sym_db.RegisterMessage(StatusResponse)
_sym_db.RegisterMessage(StatusResponse.TrainerStatusEntry)


_STATUSRESPONSE_TRAINERSTATUSENTRY._options = None
# @@protoc_insertion_point(module_scope)
