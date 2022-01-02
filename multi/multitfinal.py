
 #!/usr/bin/python3
import sys
import ply.lex as lex
import ply.yacc as yacc




t_ignore = " \t\n"
t_mult=r'\*'
def t_num(t):
	r'[0-9]+'
	t.value=int(t.value)
	print(str(t.value))
	return t
	

tokens = ( 
 'mult','num'
)

def t_error(t):
	print("Illegal character %s" % t.value[0])
	t.lexer.skip(1)


	
def p_g1(p):
	 ''' E : num '''
	 p[0]=p[1]
	 print('found number')
	
def p_g2(p):
	 ''' E : E mult E '''
	 p[0]=p[1]*p[3]
	 print('found plus')
	


def p_error(p):
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
