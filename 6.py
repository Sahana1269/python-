#printing a program to import ramdom function
import random


while True:
	i=input("enter 'n' to quit")
	if(i=='n'):
		print("Bye!")
		exit()


	else:
		print("You got",random.radint(1,6))
		
