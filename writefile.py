# outFile = open("text.txt", 'w')
# outFile.write('Thsi is line 1\n')
# outFile.write('This is line 2\n')
# outFile.close()

outFile = open ('grades.txt', 'w')
grade = 0
print("Enter a grade (q to quit):")
grade = raw_input()


while (grade != 'q'):

	outFile.write(str(grade) + '\n')
	print("Enter a grade (q to quit):")
	grade = raw_input()
	
outFile.close()