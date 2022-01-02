 #!/usr/bin/python3
import sys
import ply.lex as lex
import ply.yacc as yacc




t_ignore = " \t\n"
def t_g2(t):
	 r'[S:E+E]'
	 kjf jhbdf dhfvb
	

tokens = ( 
 'g2'
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