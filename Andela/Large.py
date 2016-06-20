def get_algorithm_result(myList):
  Largest = myList[0]
  for Li in range(1, len(myList)):
    if Largest< Li:
      Largest = Li
    return Largest
get_algorithm_result([1,6,8,9])
