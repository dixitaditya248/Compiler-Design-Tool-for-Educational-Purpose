def p_error(p):
	if p:
		print("syntax error at {0}".format(p.value))
	else:
		print("syntax error at EOF")


def p_g2(p):
	'''S:E'''

def p_mult(p):
	'''E'''

def p_pdfcfvfr(p):
	'''E'''

def p_g3(p):
	'''E:id'''