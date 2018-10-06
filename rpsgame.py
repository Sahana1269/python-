#orinting the game rock paper scissor 
import random 
u=input("enter ,r,p,s,:")
a={1:'r',2:'p',3:'s'}
c=a[random.randint(1,3)]
if(u=='r' or u=='p' or u=='s'):
	if(u==c):
		print("tie")
	elif((u=="p" and c=="s") or (u=="r"and c=="s") or (u=="s" and c=="p") or (u=="p" and c=="r")):
		print("Computer wins")
	else:
		print("I won")
else:
	print("enter a proper key")
	

