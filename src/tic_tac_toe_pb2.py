# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tic_tac_toe.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11tic_tac_toe.proto\x12\x0btic_tac_toe\"5\n\x04Move\x12\x1f\n\x04mark\x18\x01 \x01(\x0e\x32\x11.tic_tac_toe.Mark\x12\x0c\n\x04\x63\x65ll\x18\x02 \x01(\x05\"\x9d\x01\n\x04Game\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0bis_finished\x18\x02 \x01(\x08\x12&\n\x06winner\x18\x03 \x01(\x0e\x32\x11.tic_tac_toe.MarkH\x00\x88\x01\x01\x12\x1f\n\x04turn\x18\x04 \x01(\x0e\x32\x11.tic_tac_toe.Mark\x12 \n\x05moves\x18\x05 \x03(\x0b\x32\x11.tic_tac_toe.MoveB\t\n\x07_winner\"\x13\n\x11\x43reateGameRequest\"!\n\x0eGetGameRequest\x12\x0f\n\x07game_id\x18\x01 \x01(\x05\"C\n\x0fMakeMoveRequest\x12\x0f\n\x07game_id\x18\x01 \x01(\x05\x12\x1f\n\x04move\x18\x02 \x01(\x0b\x32\x11.tic_tac_toe.Move*\'\n\x04Mark\x12\x0f\n\x0bMARK_NOUGHT\x10\x00\x12\x0e\n\nMARK_CROSS\x10\x01\x32\xca\x01\n\tTicTacToe\x12\x41\n\nCreateGame\x12\x1e.tic_tac_toe.CreateGameRequest\x1a\x11.tic_tac_toe.Game\"\x00\x12;\n\x07GetGame\x12\x1b.tic_tac_toe.GetGameRequest\x1a\x11.tic_tac_toe.Game\"\x00\x12=\n\x08MakeMove\x12\x1c.tic_tac_toe.MakeMoveRequest\x1a\x11.tic_tac_toe.Game\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tic_tac_toe_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MARK']._serialized_start=374
  _globals['_MARK']._serialized_end=413
  _globals['_MOVE']._serialized_start=34
  _globals['_MOVE']._serialized_end=87
  _globals['_GAME']._serialized_start=90
  _globals['_GAME']._serialized_end=247
  _globals['_CREATEGAMEREQUEST']._serialized_start=249
  _globals['_CREATEGAMEREQUEST']._serialized_end=268
  _globals['_GETGAMEREQUEST']._serialized_start=270
  _globals['_GETGAMEREQUEST']._serialized_end=303
  _globals['_MAKEMOVEREQUEST']._serialized_start=305
  _globals['_MAKEMOVEREQUEST']._serialized_end=372
  _globals['_TICTACTOE']._serialized_start=416
  _globals['_TICTACTOE']._serialized_end=618
# @@protoc_insertion_point(module_scope)
