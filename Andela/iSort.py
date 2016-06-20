def get_algorithm_result(myList):
   for index in range(1,len(myList)):

     Largest = myList[index]
     Li = index

     while Li>0 and myList[Li-1]<Largest:
         myList[Li]=myList[Li-1]
         Li = Li-1

     myList[Li]=Largest

myList = [1, 78, 34, 12, 10, 3]
get_algorithm_result(myList)
print(myList)