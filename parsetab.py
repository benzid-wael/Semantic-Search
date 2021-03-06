
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '-\xf2V\x8em1\xfe\xf7L\xd7/\xb8@BV;'
    
_lr_action_items = {'AND':([1,5,6,9,10,11,12,],[7,-5,-4,-6,-7,-3,7,]),'OR':([1,2,5,6,9,10,11,12,],[-2,8,-5,-4,-6,-7,-3,-1,]),'REL':([0,7,8,],[3,3,3,]),'NOT':([0,7,8,],[4,4,4,]),'ANNOTATION':([0,3,4,7,8,],[5,9,10,5,5,]),'$end':([1,2,5,6,9,10,11,12,],[-2,0,-5,-4,-6,-7,-3,-1,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'andquery':([0,8,],[1,12,]),'orquery':([0,],[2,]),'unitquery':([0,7,8,],[6,11,6,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> orquery","S'",1,None,None,None),
  ('orquery -> orquery OR andquery','orquery',3,'p_orquery_or','lex_parser.py',68),
  ('orquery -> andquery','orquery',1,'p_orquery_and','lex_parser.py',72),
  ('andquery -> andquery AND unitquery','andquery',3,'p_andquery_and','lex_parser.py',76),
  ('andquery -> unitquery','andquery',1,'p_andquery_unit','lex_parser.py',80),
  ('unitquery -> ANNOTATION','unitquery',1,'p_unitquery_annot','lex_parser.py',84),
  ('unitquery -> REL ANNOTATION','unitquery',2,'p_unitquery_rel','lex_parser.py',88),
  ('unitquery -> NOT ANNOTATION','unitquery',2,'p_unitquery_not','lex_parser.py',92),
]
