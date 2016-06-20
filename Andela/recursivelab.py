def recursive_factorial(n):
  if n ==1:
    return 1
  else:
    return n* (recursive_factorial(n-1))




def iterative_factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num