#find a grade by entering marks
a=int(input("enter your marks"))
if(a>85):
	print("DISTINCTION")
elif(a>=75):
	print("FIRST CLASS")
elif(a>=65):
	print("SECOND CLASS")
else:
	print("fail")