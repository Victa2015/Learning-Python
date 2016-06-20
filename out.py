file = open("Output.txt", 'a')

print >> file, "This is a different output stream."

import sys

sys.stdout= file

print("This must be even cooler....")