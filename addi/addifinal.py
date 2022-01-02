 #!/usr/bin/python3
import sys
import ply.lex as lex
import ply.yacc as yacc



tokens = (
 'PLUS','NUM'
)

t_ignore = " \t\n"
t_PLUS=r'\+'
def t_NUM(t):
	 r'\d+'
	 t.value=int(t.value)
	 print(str(t.value))
    return t




def t_error(t):
	print("Illegal character %s" % t.value[0])
	t.lexer.skip(1)



def p_g2(p):
	 ''' E : E PLUS E '''
	 p[0]=p[1]+p[3]
	 print('found exp')


def p_g1(p):
	 ''' E : NUM  '''
	 p[0]=p[1]
	 print('found number')




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
