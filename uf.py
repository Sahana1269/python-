#using functions
#reading the values
x=int(input("enter a number"))
y=int(input("enter another number"))
#calling add function
def add():
	return x+y
#calling sub function
def sub():
	return x-y
#calling mult function
def mult():
	return x*y
#calling div function
def div():
	return x/y
print("addition=")
z=add()#calling add function
print(z)
print("subtraction=")
p=sub()#calling sub function
print(p)#printing p value
print("multiplication=")
q=mult()#calling mult function
print(q)#printing q value
print("division=")
r=div()#calling div function
print(r)#printing r value

