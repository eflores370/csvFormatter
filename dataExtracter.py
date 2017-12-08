import re
import sys

print("======================")
print("1. CNITMajor")
fileName = input("File Name: ")
if fileName == "1":	
	fileName = "CNITMajor.txt"
file = open(fileName,"r")

for line in file:
	if(re.search('CNIT', line)):
		print(line)