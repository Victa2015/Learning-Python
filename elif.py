
print ("Enter Grade: ")
grade = int(raw_input())

if grade >= 90:
	letterGrade = "A"
elif grade >=80:
	letterGrade = "B"
elif grade >=70:
	letterGrade = "C"

elif grade >=60:
	letterGrade = "D"
elif grade <= 59:
	letterGrade = "F"
else:
	print("Did not recognise your grade.")

print("Your Letter Grade is :  " + letterGrade)