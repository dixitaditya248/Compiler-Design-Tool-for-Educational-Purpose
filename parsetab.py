
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = 'A32683D747C8A057F51B59CFB48B6FC8'
    
_lr_action_items = {'BODY':([0,1,3,4,5,6,7,],[1,-5,1,-3,-4,1,1,]),'ID':([0,1,3,4,5,6,7,],[4,-5,4,-3,-4,4,4,]),'RULE':([0,1,3,4,5,6,7,],[5,-5,5,-3,-4,5,5,]),'$end':([1,2,4,5,7,8,],[-5,0,-3,-4,-1,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[2,]),'E':([0,3,6,7,],[3,6,7,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> E E E','S',3,'p_s','grammar1.py',50),
  ('S -> E E E E','S',4,'p_s67','grammar1.py',141),
  ('E -> ID','E',1,'p_e','grammar1.py',244),
  ('E -> RULE','E',1,'p_e1','grammar1.py',278),
  ('E -> BODY','E',1,'p_s2','grammar1.py',312),
]
