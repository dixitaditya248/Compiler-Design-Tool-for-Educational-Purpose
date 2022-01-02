 #!/usr/bin/python3
import sys
import ply.lex as lex
import ply.yacc as yacc




t_ignore = " \t\n"
t_plus=r'[\+]'
def t_num(t):
	 r'[0-9]+'
	   t.value=int(t.value)
	

tokens = ( 
 'plus','num'
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