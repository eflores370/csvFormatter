import re
import sys

tempClass = "CNIT"

print("======================")
print("1. CNITMajor")
fileName = input("File Name: ")
if fileName == "1":	
	fileName = "CNITMajor.txt"

file = open(fileName,"r")

writeFile = open("CNITMajor.csv", "w+")

for line in file:
	if(re.search('^' + re.escape(tempClass), line)):
		print(line)
		values = line.split("\xad")
		left = values[0].strip().split("\xa0")
		
		writeFile.write(left[0] + ";")
		writeFile.write(left[1] + ";")
		writeFile.write(values[1].strip() + "\n")
		


