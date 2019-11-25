#!usr/bin/python3
import sys 
print("I see ", len(sys.argv), " arguments")
print("They are", sys.argv)
if sys.argv[1].isnumeric():
	print("first arg is numeric: ", int(sys.argv[1]))
else: 
	print("First arg is non-numeric")

