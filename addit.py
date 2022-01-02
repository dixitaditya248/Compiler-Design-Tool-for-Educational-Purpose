 #!/usr/bin/python3
import sys
import ply.lex as lex
import ply.yacc as yacc




t_ignore = " \t\n"
t_plus=r'[\+]'

tokens = ( 
 'plus'
)

def t_error(t):
	print("Illegal character %s" % t.value[0])
	t.lexer.skip(1)def p_error(p):
	if p:
		print("syntax error at {0}".format(p.value))
	else:
		print("syntax error at EOF")

def process(data):
	lex.lex()
	yacc.yacc()
	yacc.parse(data)

if __name__ == "__main__" :
	data = sys.stdin.readline()
	process(data)