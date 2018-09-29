#printing roll,quit,bye
import random

#using random function
while True:	
	i=input("enter 'r' to roll, 'q' to quit")#entering a letter
	if(i=='q'):
		print("Bye!")#printing a bye
		exit()#exiting the program

	elif(i=='r'):#entering r
		print("You got",random.randint(1,6))#printing a random number
    