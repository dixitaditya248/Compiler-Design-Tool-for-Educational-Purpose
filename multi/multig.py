
def p_g0(p):
	 ''' S : E '''
	
def p_g1(p):
	 ''' E : num '''
	 p[0]=p[1]
	 print('found number')
	
def p_g2(p):
	 ''' E : E mult E '''
	 p[0]=p[1]*p[3]
	 print('found plus')
	