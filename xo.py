#printing the game tic-tac toe
a=["1","2","3","4","5","6","7","8","9"]

def printBoard():
	print(a[0],"|",a[1],"|",a[2])
	print("---------")
	print(a[3],"|",a[4],"|",a[5])
	print("---------")
	print(a[6],"|",a[7],"|",a[8])

playerOneturn=True
while True:
	printBoard()
	p=input("select a place :")

	if(p in a):
		if(a[int(p)-1]=='X' or [int(p)-1]=='O'):
			print("place already taken,select other a place")
			continue
		else:
			if playerOneturn:
				print("player1>>")
				a[int(p)-1]='X'
				playerOneturn=not playerOneturn
			else:
				print("player2>>")
				a[int(p)-1]='O'
				playerOneturn=not playerOneturn
			for i in(0,3,6):
				if(a[i]==a[i+1] and a[i]==a[i+2]):
					print("Game Over")
					exit()
			for i in range(3):
				if(a[i]==a[i+3] and a[i]==a[i+6]):
					print("Game Over")
					exit()		
	else:
		continue






