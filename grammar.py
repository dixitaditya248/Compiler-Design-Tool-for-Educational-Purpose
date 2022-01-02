#!/usr/bin/python3
import sys
import ply.lex as lex
import ply.yacc as yacc


naam=0
live={}
turn=0

tokens = (
        'ID', 'EXP' , 'BODY'
)


words=[]
filename1=sys.argv[1]
filenamel1=filename1.split(".")
filename1=filenamel1[0]
filenamed=filename1+"g.dot"
file1 = open(filenamed, "w")
str1="digraph G { ordering=out "
file1.write(str1)
file1.write("\n")
filename=filename1+"g"+".py"
file = open(filename, "w")

s='''def p_error(p):\n\tif p:\n\t\tprint("syntax error at {0}".format(p.value))\n\telse:\n\t\tprint("syntax error at EOF")
'''
file.write(s)

t_ID = r'[a-zA-Z][0-9a-zA-Z]*'
t_EXP=r'[#](.+)[#]'
t_BODY=r'[$](.+)[$]'

t_ignore = " \t\n"

def t_error(t):
	print("Illegal character %s" % t.value[0])
	t.lexer.skip(1)


def p_s(p):
    " S : E E E "
    global words
    global naam
    global live
    global turn
    save=[]
    flag=1
    print(str(p[1])+str(p[2]))
    print("found")
    ss=str(p[2])
    ss=ss[1:len(ss)-1]
    s="\n\ndef p_"+str(p[1])+"(p):\n\t"+"'''"+ss+"'''"
    file.write(s)
    s='''n'''+str(naam)+''' [ label = "Grammar"]'''+";"
    #print(s)
    live.update({"n"+str(naam):0})
    #print(live)
    file1.write(s)
    file1.write("\n")
    for i in range(naam-1,0,-1):
        
        if turn % 2 == 0:

          if i % 2 == 1 and flag <=2 :

                zz="n"+str(i)
                if(live[zz]==0):
                  s="n"+str(naam)+"->"+"n"+str(i)+";"
                  save.append(s)
               #print(s)
                  zz="n"+str(i)
                  live[zz]=1
               #print(live)
                  flag+=1
               #file.write(s)
                if(i==naam-2):
                  s="n"+str(naam)+"->"+"n"+str(naam-1)+";"
                  save.append(s)
                #print(s)
                  zz="n"+str(naam-1)
                  live[zz]=1
                #file.write(s) 

        elif turn % 2 == 1:


          if i % 2 == 0 and flag <=2 :

                zz="n"+str(i)
                if(live[zz]==0):
                  s="n"+str(naam)+"->"+"n"+str(i)+";"
                  save.append(s)
               #print(s)
                  zz="n"+str(i)
                  live[zz]=1
               #print(live)
                  flag+=1
               #file.write(s)
                if(i==naam-2):
                  s="n"+str(naam)+"->"+"n"+str(naam-1)+";"
                  save.append(s)
                #print(s)
                  zz="n"+str(naam-1)
                  live[zz]=1
                #file.write(s) 

 

    for i in range(len(save)-1,-1,-1):
       file1.write(save[i])
       file1.write("\n")

    naam+=1
    flag=0
    turn+=1
       #del save[:]




def p_s1(p):
    " E : EXP "
    global naam
    global live
    global turn
    print(p[1])
    p[0]=p[1]
    print("found2")


    s='''n'''+str(naam)+''' [ label = "Rule:'''+str(p[1])+'''"]'''+";"
    #print(s)



    live.update({"n"+str(naam):0})
    #print(live)
    file1.write(s)
    file1.write("\n")
    naam+=1

    s='''n'''+str(naam)+''' [ label = "E"]'''+";"
    #print(s)
    live.update({"n"+str(naam):0})
    #print(live)
    file1.write(s)
    file1.write("\n")
    s="n"+str(naam)+"->"+"n"+str(naam-1)+";"
    zz="n"+str(naam-1)
    live[zz]=1
    #print(s)

    file1.write(s)
    file1.write("\n")
    naam+=1




def p_s2(p):
    " E : ID "
    global naam
    global live
    global turn
    print(p[1])
    print("found3")
    p[0]=p[1]

    s='''n'''+str(naam)+''' [ label = "Name:'''+str(p[1])+'''"]'''+";"
    #print(s)



    live.update({"n"+str(naam):0})
    #print(live)
    file1.write(s)
    file1.write("\n")
    naam+=1

    s='''n'''+str(naam)+''' [ label = "E"]'''+";"
    #print(s)
    live.update({"n"+str(naam):0})
    #print(live)
    file1.write(s)
    file1.write("\n")
    s="n"+str(naam)+"->"+"n"+str(naam-1)+";"
    zz="n"+str(naam-1)
    live[zz]=1
    #print(s)

    file1.write(s)
    file1.write("\n")
    naam+=1
    

def p_s3(p):
    " E : BODY "
    global naam
    global live
    global turn
    print(p[1])
    print("found3")
    p[0]=p[1]

    s='''n'''+str(naam)+''' [ label = "Name:'''+str(p[1])+'''"]'''+";"
    #print(s)



    live.update({"n"+str(naam):0})
    #print(live)
    file1.write(s)
    file1.write("\n")
    naam+=1

    s='''n'''+str(naam)+''' [ label = "E"]'''+";"
    #print(s)
    live.update({"n"+str(naam):0})
    #print(live)
    file1.write(s)
    file1.write("\n")
    s="n"+str(naam)+"->"+"n"+str(naam-1)+";"
    zz="n"+str(naam-1)
    live[zz]=1
    #print(s)

    file1.write(s)
    file1.write("\n")
    naam+=1
    

def p_error(p):
	if p:
		print("syntax error at {0}".format(p.value))
	else:
		print("syntax error at EOF")


def process(data):
	lex.lex()
	yacc.yacc()
	yacc.parse(data)



if __name__ == "__main__":
    aaa=filename1+".g" 
    file2 = open(aaa, "r")
    f=file2.read()
    ls=[]
    s=""
    s1=""
    for i in f:
        if i != "\n":
           if i != ' ':
              s=s+i
           else:
               ls.append(s)
               s=""
        else:
            ls.append(s)
            print(ls)
            s=""
            ls[len(ls)-1]="#"+str(ls[len(ls)-1])+"#"
            s1=str(ls[len(ls)-2])+" "+str(ls[len(ls)-1])
            process(s1)
            s1=""

    str1="}"
    file1.write(str1)
