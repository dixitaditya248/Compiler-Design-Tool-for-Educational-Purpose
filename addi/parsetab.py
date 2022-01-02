
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUM PLUS E : E PLUS E  E : NUM  '
    
_lr_action_items = {'NUM':([0,3,],[2,2,]),'$end':([1,2,4,],[0,-2,-1,]),'PLUS':([1,2,4,],[3,-2,3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'E':([0,3,],[1,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> E","S'",1,None,None,None),
  ('E -> E PLUS E','E',3,'p_g2','addifinal.py',30),
  ('E -> NUM','E',1,'p_g1','addifinal.py',36),
]
