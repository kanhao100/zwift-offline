# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_storage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12user_storage.proto\".\n\x0bUserStorage\x12\x1f\n\nattributes\x18\x02 \x03(\x0b\x32\x0b.Attributes\"\x98\x01\n\nAttributes\x12$\n\rgame_settings\x18\x16 \x01(\x0b\x32\r.GameSettings\x12\x35\n\x14garage_last_selected\x18\x17 \x01(\x0b\x32\x17.GarageItemLastSelected\x12-\n\x12special_event_seen\x18\x19 \x01(\x0b\x32\x11.SpecialEventSeen\"\x9c\x01\n\x0cGameSettings\x12\n\n\x02\x66\x32\x18\x02 \x01(\x02\x12\x14\n\x0cleaderboards\x18\x03 \x01(\x05\x12\x19\n\x11power_meter_slot0\x18\x04 \x01(\x05\x12\x19\n\x11power_meter_slot1\x18\x05 \x01(\x05\x12\x19\n\x11power_meter_slot2\x18\x06 \x01(\x05\x12\x19\n\x11power_meter_slot3\x18\x07 \x01(\x05\"9\n\x16GarageItemLastSelected\x12\x11\n\tsignature\x18\x01 \x01(\t\x12\x0c\n\x04time\x18\x02 \x01(\x04\"3\n\x10SpecialEventSeen\x12\x11\n\tsignature\x18\x01 \x01(\t\x12\x0c\n\x04time\x18\x02 \x01(\x04')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_storage_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USERSTORAGE._serialized_start=22
  _USERSTORAGE._serialized_end=68
  _ATTRIBUTES._serialized_start=71
  _ATTRIBUTES._serialized_end=223
  _GAMESETTINGS._serialized_start=226
  _GAMESETTINGS._serialized_end=382
  _GARAGEITEMLASTSELECTED._serialized_start=384
  _GARAGEITEMLASTSELECTED._serialized_end=441
  _SPECIALEVENTSEEN._serialized_start=443
  _SPECIALEVENTSEEN._serialized_end=494
# @@protoc_insertion_point(module_scope)
