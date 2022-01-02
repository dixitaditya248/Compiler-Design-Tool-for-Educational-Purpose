#!/usr/bin/python3
import sys


filename1=sys.argv[1]
foldername=filename1.split(".")
filename2=sys.argv[2]

file = open(filename1, "r")
file1 = open(filename2,"r")
var=str(foldername[0])+"final.py"

file2=open(var,"w")

f1=file.read()
f2=file1.read()
str=""
for i in f1:
	if i == '\n':
		if str == "	t.lexer.skip(1)":
			file2.write(i)
			for j in f2:
				file2.write(j)
		else:
			file2.write(i)
	else:
		file2.write(i)
		
		
			
		

