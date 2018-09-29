#printing snake and ladder game 
import random 

count=0

while(count<=100):
	n=input("press 'r' to roll the dice")
	if(n=='r'):
		r=random.randint(1,6)
		count=count+r
		print("u got",r)
		print("new position is",count)

		if(count==8):
			count=37
			print(" yeah!,i got a ladder")
		elif(count==11):
			count=2
			print("oh !,u got a snake")
		elif(count==13):
			count=34
			print("yeah!,i got a ladder")
		elif(count==25):
			count=4
			print("oh!,u got a snake")
		elif(count==38):
			count=9
			print("oh!!, u got a snake")
		elif(count==40):
			count=68
			print("yeah!,i got a ladder")
		elif(count==52):
			count=81
			print("yeah!, i got a ladder")
		elif(count==65):
			count=46
			print("oh!!,u got a snake")
		elif(count==76):
			count=97
			print("yeah!!,i got a ladder")
		elif(count==89):
			count=70
			print("ohh,u got a snake")
		elif(count==93):
			count=64
			print("ohh!!,u got a snake")
		elif(count==100):
			print("congragulations!, u won")
			exit()
		elif(count>100):
			print("stay in the same place")
			count=count-r



