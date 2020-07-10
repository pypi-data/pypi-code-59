# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cognite/seismic/protos/types.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cognite/seismic/protos/types.proto',
  package='com.cognite.seismic',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"cognite/seismic/protos/types.proto\x12\x13\x63om.cognite.seismic\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto\"/\n\nCoordinate\x12\x0b\n\x03\x63rs\x18\x01 \x01(\t\x12\t\n\x01x\x18\x02 \x01(\x02\x12\t\n\x01y\x18\x03 \x01(\x02\"\xb9\x01\n\x05Trace\x12\x14\n\x0ctrace_header\x18\x01 \x01(\x0c\x12*\n\x05iline\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12*\n\x05xline\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\r\n\x05trace\x18\x04 \x03(\x02\x12\x33\n\ncoordinate\x18\x05 \x01(\x0b\x32\x1f.com.cognite.seismic.Coordinate\";\n\x0cSurfacePoint\x12\r\n\x05iline\x18\x01 \x01(\x05\x12\r\n\x05xline\x18\x02 \x01(\x05\x12\r\n\x05value\x18\x03 \x01(\x02\"\x90\x01\n\x06Survey\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12;\n\x08metadata\x18\x03 \x03(\x0b\x32).com.cognite.seismic.Survey.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8c\x01\n\x04\x46ile\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x39\n\x08metadata\x18\x03 \x03(\x0b\x32\'.com.cognite.seismic.File.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"$\n\x07Project\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x61lias\x18\x02 \x01(\t\"4\n\nIdentifier\x12\x0c\n\x02id\x18\x01 \x01(\tH\x00\x12\x0e\n\x04name\x18\x02 \x01(\tH\x00\x42\x08\n\x06\x66indby\"d\n\x0eLineDescriptor\x12(\n\x03min\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12(\n\x03max\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\";\n\nLineSelect\x12\x0f\n\x05iline\x18\x01 \x01(\x05H\x00\x12\x0f\n\x05xline\x18\x02 \x01(\x05H\x00\x42\x0b\n\tdirection\"i\n\tLineRange\x12.\n\tfrom_line\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12,\n\x07to_line\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\"\x12\n\x03\x43RS\x12\x0b\n\x03\x63rs\x18\x01 \x01(\t\"\x17\n\x03Wkt\x12\x10\n\x08geometry\x18\x01 \x01(\t\"0\n\x07GeoJson\x12%\n\x04json\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"\x91\x01\n\x08Geometry\x12%\n\x03\x63rs\x18\x01 \x01(\x0b\x32\x18.com.cognite.seismic.CRS\x12\'\n\x03wkt\x18\x02 \x01(\x0b\x32\x18.com.cognite.seismic.WktH\x00\x12+\n\x03geo\x18\x03 \x01(\x0b\x32\x1c.com.cognite.seismic.GeoJsonH\x00\x42\x08\n\x06\x66ormat*X\n\tJobStatus\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06QUEUED\x10\x01\x12\x0f\n\x0bIN_PROGRESS\x10\x02\x12\x0b\n\x07SUCCESS\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\x0b\n\x07TIMEOUT\x10\x05*\xa0\x01\n\x08\x46ileStep\x12\x0c\n\x08REGISTER\x10\x00\x12\x17\n\x13INSERT_FILE_HEADERS\x10\x01\x12\x18\n\x14INSERT_TRACE_HEADERS\x10\x02\x12\x0f\n\x0bINSERT_DATA\x10\x03\x12\x14\n\x10\x43OMPUTE_COVERAGE\x10\x04\x12\x10\n\x0c\x43OMPUTE_GRID\x10\x05\x12\r\n\x08\x44\x45LETING\x10\xfe\x01\x12\x0b\n\x06\x44\x45LETE\x10\xff\x01*H\n\x13InterpolationMethod\x12\x11\n\rNEAREST_TRACE\x10\x00\x12\x1e\n\x1aINVERSE_DISTANCE_WEIGHTING\x10\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])

_JOBSTATUS = _descriptor.EnumDescriptor(
  name='JobStatus',
  full_name='com.cognite.seismic.JobStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QUEUED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IN_PROGRESS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TIMEOUT', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1314,
  serialized_end=1402,
)
_sym_db.RegisterEnumDescriptor(_JOBSTATUS)

JobStatus = enum_type_wrapper.EnumTypeWrapper(_JOBSTATUS)
_FILESTEP = _descriptor.EnumDescriptor(
  name='FileStep',
  full_name='com.cognite.seismic.FileStep',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REGISTER', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INSERT_FILE_HEADERS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INSERT_TRACE_HEADERS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INSERT_DATA', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPUTE_COVERAGE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPUTE_GRID', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETING', index=6, number=254,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=7, number=255,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1405,
  serialized_end=1565,
)
_sym_db.RegisterEnumDescriptor(_FILESTEP)

FileStep = enum_type_wrapper.EnumTypeWrapper(_FILESTEP)
_INTERPOLATIONMETHOD = _descriptor.EnumDescriptor(
  name='InterpolationMethod',
  full_name='com.cognite.seismic.InterpolationMethod',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NEAREST_TRACE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVERSE_DISTANCE_WEIGHTING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1567,
  serialized_end=1639,
)
_sym_db.RegisterEnumDescriptor(_INTERPOLATIONMETHOD)

InterpolationMethod = enum_type_wrapper.EnumTypeWrapper(_INTERPOLATIONMETHOD)
NONE = 0
QUEUED = 1
IN_PROGRESS = 2
SUCCESS = 3
FAILED = 4
TIMEOUT = 5
REGISTER = 0
INSERT_FILE_HEADERS = 1
INSERT_TRACE_HEADERS = 2
INSERT_DATA = 3
COMPUTE_COVERAGE = 4
COMPUTE_GRID = 5
DELETING = 254
DELETE = 255
NEAREST_TRACE = 0
INVERSE_DISTANCE_WEIGHTING = 1



_COORDINATE = _descriptor.Descriptor(
  name='Coordinate',
  full_name='com.cognite.seismic.Coordinate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='crs', full_name='com.cognite.seismic.Coordinate.crs', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='com.cognite.seismic.Coordinate.x', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='com.cognite.seismic.Coordinate.y', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=121,
  serialized_end=168,
)


_TRACE = _descriptor.Descriptor(
  name='Trace',
  full_name='com.cognite.seismic.Trace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='trace_header', full_name='com.cognite.seismic.Trace.trace_header', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iline', full_name='com.cognite.seismic.Trace.iline', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='xline', full_name='com.cognite.seismic.Trace.xline', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace', full_name='com.cognite.seismic.Trace.trace', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coordinate', full_name='com.cognite.seismic.Trace.coordinate', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=171,
  serialized_end=356,
)


_SURFACEPOINT = _descriptor.Descriptor(
  name='SurfacePoint',
  full_name='com.cognite.seismic.SurfacePoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='iline', full_name='com.cognite.seismic.SurfacePoint.iline', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='xline', full_name='com.cognite.seismic.SurfacePoint.xline', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.cognite.seismic.SurfacePoint.value', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=358,
  serialized_end=417,
)


_SURVEY_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='com.cognite.seismic.Survey.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.cognite.seismic.Survey.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.cognite.seismic.Survey.MetadataEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=517,
  serialized_end=564,
)

_SURVEY = _descriptor.Descriptor(
  name='Survey',
  full_name='com.cognite.seismic.Survey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.cognite.seismic.Survey.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='com.cognite.seismic.Survey.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='com.cognite.seismic.Survey.metadata', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SURVEY_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=564,
)


_FILE_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='com.cognite.seismic.File.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.cognite.seismic.File.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.cognite.seismic.File.MetadataEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=517,
  serialized_end=564,
)

_FILE = _descriptor.Descriptor(
  name='File',
  full_name='com.cognite.seismic.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.cognite.seismic.File.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='com.cognite.seismic.File.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='com.cognite.seismic.File.metadata', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_FILE_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=567,
  serialized_end=707,
)


_PROJECT = _descriptor.Descriptor(
  name='Project',
  full_name='com.cognite.seismic.Project',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.cognite.seismic.Project.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alias', full_name='com.cognite.seismic.Project.alias', index=1,
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
  serialized_start=709,
  serialized_end=745,
)


_IDENTIFIER = _descriptor.Descriptor(
  name='Identifier',
  full_name='com.cognite.seismic.Identifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.cognite.seismic.Identifier.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='com.cognite.seismic.Identifier.name', index=1,
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
    _descriptor.OneofDescriptor(
      name='findby', full_name='com.cognite.seismic.Identifier.findby',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=747,
  serialized_end=799,
)


_LINEDESCRIPTOR = _descriptor.Descriptor(
  name='LineDescriptor',
  full_name='com.cognite.seismic.LineDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='com.cognite.seismic.LineDescriptor.min', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max', full_name='com.cognite.seismic.LineDescriptor.max', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=801,
  serialized_end=901,
)


_LINESELECT = _descriptor.Descriptor(
  name='LineSelect',
  full_name='com.cognite.seismic.LineSelect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='iline', full_name='com.cognite.seismic.LineSelect.iline', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='xline', full_name='com.cognite.seismic.LineSelect.xline', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
    _descriptor.OneofDescriptor(
      name='direction', full_name='com.cognite.seismic.LineSelect.direction',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=903,
  serialized_end=962,
)


_LINERANGE = _descriptor.Descriptor(
  name='LineRange',
  full_name='com.cognite.seismic.LineRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_line', full_name='com.cognite.seismic.LineRange.from_line', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_line', full_name='com.cognite.seismic.LineRange.to_line', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=964,
  serialized_end=1069,
)


_CRS = _descriptor.Descriptor(
  name='CRS',
  full_name='com.cognite.seismic.CRS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='crs', full_name='com.cognite.seismic.CRS.crs', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1071,
  serialized_end=1089,
)


_WKT = _descriptor.Descriptor(
  name='Wkt',
  full_name='com.cognite.seismic.Wkt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='geometry', full_name='com.cognite.seismic.Wkt.geometry', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1091,
  serialized_end=1114,
)


_GEOJSON = _descriptor.Descriptor(
  name='GeoJson',
  full_name='com.cognite.seismic.GeoJson',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='json', full_name='com.cognite.seismic.GeoJson.json', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1116,
  serialized_end=1164,
)


_GEOMETRY = _descriptor.Descriptor(
  name='Geometry',
  full_name='com.cognite.seismic.Geometry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='crs', full_name='com.cognite.seismic.Geometry.crs', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wkt', full_name='com.cognite.seismic.Geometry.wkt', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geo', full_name='com.cognite.seismic.Geometry.geo', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='format', full_name='com.cognite.seismic.Geometry.format',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1167,
  serialized_end=1312,
)

_TRACE.fields_by_name['iline'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_TRACE.fields_by_name['xline'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_TRACE.fields_by_name['coordinate'].message_type = _COORDINATE
_SURVEY_METADATAENTRY.containing_type = _SURVEY
_SURVEY.fields_by_name['metadata'].message_type = _SURVEY_METADATAENTRY
_FILE_METADATAENTRY.containing_type = _FILE
_FILE.fields_by_name['metadata'].message_type = _FILE_METADATAENTRY
_IDENTIFIER.oneofs_by_name['findby'].fields.append(
  _IDENTIFIER.fields_by_name['id'])
_IDENTIFIER.fields_by_name['id'].containing_oneof = _IDENTIFIER.oneofs_by_name['findby']
_IDENTIFIER.oneofs_by_name['findby'].fields.append(
  _IDENTIFIER.fields_by_name['name'])
_IDENTIFIER.fields_by_name['name'].containing_oneof = _IDENTIFIER.oneofs_by_name['findby']
_LINEDESCRIPTOR.fields_by_name['min'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_LINEDESCRIPTOR.fields_by_name['max'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_LINESELECT.oneofs_by_name['direction'].fields.append(
  _LINESELECT.fields_by_name['iline'])
_LINESELECT.fields_by_name['iline'].containing_oneof = _LINESELECT.oneofs_by_name['direction']
_LINESELECT.oneofs_by_name['direction'].fields.append(
  _LINESELECT.fields_by_name['xline'])
_LINESELECT.fields_by_name['xline'].containing_oneof = _LINESELECT.oneofs_by_name['direction']
_LINERANGE.fields_by_name['from_line'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_LINERANGE.fields_by_name['to_line'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_GEOJSON.fields_by_name['json'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_GEOMETRY.fields_by_name['crs'].message_type = _CRS
_GEOMETRY.fields_by_name['wkt'].message_type = _WKT
_GEOMETRY.fields_by_name['geo'].message_type = _GEOJSON
_GEOMETRY.oneofs_by_name['format'].fields.append(
  _GEOMETRY.fields_by_name['wkt'])
_GEOMETRY.fields_by_name['wkt'].containing_oneof = _GEOMETRY.oneofs_by_name['format']
_GEOMETRY.oneofs_by_name['format'].fields.append(
  _GEOMETRY.fields_by_name['geo'])
_GEOMETRY.fields_by_name['geo'].containing_oneof = _GEOMETRY.oneofs_by_name['format']
DESCRIPTOR.message_types_by_name['Coordinate'] = _COORDINATE
DESCRIPTOR.message_types_by_name['Trace'] = _TRACE
DESCRIPTOR.message_types_by_name['SurfacePoint'] = _SURFACEPOINT
DESCRIPTOR.message_types_by_name['Survey'] = _SURVEY
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['Project'] = _PROJECT
DESCRIPTOR.message_types_by_name['Identifier'] = _IDENTIFIER
DESCRIPTOR.message_types_by_name['LineDescriptor'] = _LINEDESCRIPTOR
DESCRIPTOR.message_types_by_name['LineSelect'] = _LINESELECT
DESCRIPTOR.message_types_by_name['LineRange'] = _LINERANGE
DESCRIPTOR.message_types_by_name['CRS'] = _CRS
DESCRIPTOR.message_types_by_name['Wkt'] = _WKT
DESCRIPTOR.message_types_by_name['GeoJson'] = _GEOJSON
DESCRIPTOR.message_types_by_name['Geometry'] = _GEOMETRY
DESCRIPTOR.enum_types_by_name['JobStatus'] = _JOBSTATUS
DESCRIPTOR.enum_types_by_name['FileStep'] = _FILESTEP
DESCRIPTOR.enum_types_by_name['InterpolationMethod'] = _INTERPOLATIONMETHOD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Coordinate = _reflection.GeneratedProtocolMessageType('Coordinate', (_message.Message,), {
  'DESCRIPTOR' : _COORDINATE,
  '__module__' : 'cognite.seismic.protos.types_pb2'
  # @@protoc_insertion_point(class_scope:com.cognite.seismic.Coordinate)
  })
_sym_db.RegisterMessage(Coordinate)

Trace = _reflection.GeneratedProtocolMessageType('Trace', (_message.Message,), {
  'DESCRIPTOR' : _TRACE,
  '__module__' : 'cognite.seismic.protos.types_pb2'
  # @@protoc_insertion_point(class_scope:com.cognite.seismic.Trace)
  })
_sym_db.RegisterMessage(Trace)

SurfacePoint = _reflection.GeneratedProtocolMessageType('SurfacePoint', (_message.Message,), {
  'DESCRIPTOR' : _SURFACEPOINT,
  '__module__' : 'cognite.seismic.protos.types_pb2'
  # @@protoc_insertion_point(class_scope:com.cognite.seismic.SurfacePoint)
  })
_sym_db.RegisterMessage(SurfacePoint)

Survey = _reflection.GeneratedProtocolMessageType('Survey', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _SURVEY_METADATAENTRY,
    '__module__' : 'cognite.seismic.protos.types_pb2'
    # @@protoc_insertion_point(class_scope:com.cognite.seismic.Survey.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _SURVEY,
  '__module__' : 'cognite.seismic.protos.types_pb2'
  # @@protoc_insertion_point(class_scope:com.cognite.seismic.Survey)
  })
_sym_db.RegisterMessage(Survey)
_sym_db.RegisterMessage(Survey.MetadataEntry)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _FILE_METADATAENTRY,
    '__module__' : 'cognite.seismic.protos.types_pb2'
    # @@protoc_insertion_point(class_scope:com.cognite.seismic.File.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _FILE,
  '__module__' : 'cognite.seismic.protos.types_pb2'
  # @@protoc_insertion_point(class_scope:com.cognite.seismic.File)
  })
_sym_db.RegisterMessage(File)
_sym_db.RegisterMessage(File.MetadataEntry)

Project = _reflection.GeneratedProtocolMessageType('Project', (_message.Message,), {
  'DESCRIPTOR' : _PROJECT,
  '__module__' : 'cognite.seismic.protos.types_pb2'
  # @@protoc_insertion_point(class_scope:com.cognite.seismic.Project)
  })
_sym_db.RegisterMessage(Project)

Identifier = _reflection.GeneratedProtocolMessageType('Identifier', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFIER,
  '__module__' : 'cognite.seismic.protos.types_pb2'
  # @@protoc_insertion_point(class_scope:com.cognite.seismic.Identifier)
  })
_sym_db.RegisterMessage(Identifier)

LineDescriptor = _reflection.GeneratedProtocolMessageType('LineDescriptor', (_message.Message,), {
  'DESCRIPTOR' : _LINEDESCRIPTOR,
  '__module__' : 'cognite.seismic.protos.types_pb2'
  # @@protoc_insertion_point(class_scope:com.cognite.seismic.LineDescriptor)
  })
_sym_db.RegisterMessage(LineDescriptor)

LineSelect = _reflection.GeneratedProtocolMessageType('LineSelect', (_message.Message,), {
  'DESCRIPTOR' : _LINESELECT,
  '__module__' : 'cognite.seismic.protos.types_pb2'
  # @@protoc_insertion_point(class_scope:com.cognite.seismic.LineSelect)
  })
_sym_db.RegisterMessage(LineSelect)

LineRange = _reflection.GeneratedProtocolMessageType('LineRange', (_message.Message,), {
  'DESCRIPTOR' : _LINERANGE,
  '__module__' : 'cognite.seismic.protos.types_pb2'
  # @@protoc_insertion_point(class_scope:com.cognite.seismic.LineRange)
  })
_sym_db.RegisterMessage(LineRange)

CRS = _reflection.GeneratedProtocolMessageType('CRS', (_message.Message,), {
  'DESCRIPTOR' : _CRS,
  '__module__' : 'cognite.seismic.protos.types_pb2'
  # @@protoc_insertion_point(class_scope:com.cognite.seismic.CRS)
  })
_sym_db.RegisterMessage(CRS)

Wkt = _reflection.GeneratedProtocolMessageType('Wkt', (_message.Message,), {
  'DESCRIPTOR' : _WKT,
  '__module__' : 'cognite.seismic.protos.types_pb2'
  # @@protoc_insertion_point(class_scope:com.cognite.seismic.Wkt)
  })
_sym_db.RegisterMessage(Wkt)

GeoJson = _reflection.GeneratedProtocolMessageType('GeoJson', (_message.Message,), {
  'DESCRIPTOR' : _GEOJSON,
  '__module__' : 'cognite.seismic.protos.types_pb2'
  # @@protoc_insertion_point(class_scope:com.cognite.seismic.GeoJson)
  })
_sym_db.RegisterMessage(GeoJson)

Geometry = _reflection.GeneratedProtocolMessageType('Geometry', (_message.Message,), {
  'DESCRIPTOR' : _GEOMETRY,
  '__module__' : 'cognite.seismic.protos.types_pb2'
  # @@protoc_insertion_point(class_scope:com.cognite.seismic.Geometry)
  })
_sym_db.RegisterMessage(Geometry)


_SURVEY_METADATAENTRY._options = None
_FILE_METADATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
