def get_algorithm_result(myList):
  Largest = myList[0]
  for Li in myList:
     if Largest < Li:
       temp = Li
       Largest = temp
       Li = temp
       if Li == myList[len(myList)-1]:
        return Largest
myList = [1, 78, 34, 12, 10, 3]
get_algorithm_result(myList)
print(myList)