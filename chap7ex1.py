tries = 0
answer = "Watson"
while(tries<=3):
	print("Whats the name of the comp that...")
	response = raw_input()

	tries = tries +1
	if(response == "Watson"):
		print("Thats right")
		break
	elif(tries == 3):
		print("sorry, the answer is Watson")
		break
	else:
		print("Sorry. Try again.")