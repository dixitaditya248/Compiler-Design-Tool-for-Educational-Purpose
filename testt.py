 #!/usr/bin/python3
import sys
import ply.lex as lex
import ply.yacc as yacc




t_ignore = " \t\n"
t_num=r'[a-z]'
t_plus=r'[\+]'
t_mult=r'[\*]'
def t_id(t):
	 r'[0-9]+'
	  v=int(t.value)
	  if v < 1769 :
	     t.value=100
	    print(str(t.value))
	
def t_id1(t):
	 r'[0-9]+'
	  v=int(t.value)
	  if v < 1769 :
	     t.value=100
	    print(str(t.value))
	

tokens = ( 
 'num','plus','mult','id','id1'
)

def t_error(t):
	print("Illegal character %s" % t.value[0])
	t.lexer.skip(1)

def process(data):
	lex.lex()
	yacc.yacc()
	yacc.parse(data)

if __name__ == "__main__" :
	data = sys.stdin.readline()
	process(data)