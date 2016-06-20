answer  = "Watson"
print("Here's a guessing game. You have 3 tries.")

print("Whats the name of the computer that played on Jeopardy")

response = raw_input()
if response == answer:
	print("That's right.")
else:
	print("Sorry, try again.")
	response = raw_input()
	if response == answer:
		print("Yeah, that's it.")
	else:
		print("Sorry, One more guess.")
		response ==raw_input()
		if response == answer:
			print("OK, you got it!")
		else:
			print("Sorry. No more guesses, The Answer is " + answer)

