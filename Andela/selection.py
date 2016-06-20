def get_algorithm_result(myList):
   for a in range(len(myList)-1,0,-1):
       Largest=0
       for Li in range(1,a+1):
           if myList[Li]<myList[Largest]:
               Largest = Li

       temp = myList[a]
       myList[a] = myList[Largest]
       myList[Largest] = temp

myList = [54,26,93,17,77,31,44,55,20]
get_algorithm_result(myList)
print(myList)
