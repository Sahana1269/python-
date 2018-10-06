#
import random
a=['r','p','s']
d=0
e=0
while(True):
	p=input("enter your choice r/p/s")
	q=random.choice(a)

	print("you chose",p,"computer chose",q)
	if(p=='r' or p=='p' or p=='s'):
		if(p==q):
			print("tie")
		elif((p=='r' and q=='p') or (p=='p' and q=='s')):
			d==d-1
			print("computer won",d,"times")
		else:
			e==e-1
			print("i won",e,"times")
	else:
		print("give proper input")
		break
	if(d==3 or e==3):
		if(d==3):
			print("Oh no,computer won")
		else:
			print("congrats u won,have a great day")
		break
		
			


