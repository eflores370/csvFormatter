import re
import sys

classArray = {"MATH", "CNIT", "CS"}

print("======================")
print("1. CNIT Major")
print("2. CS Major")
fileName = input("File Name: ")
if fileName == "1":	
	fileName = "CNITMajor.txt"
elif fileName == "2":
	fileName = "ComputerScienceMajor.txt"

# Open Text file
file = open(fileName,"r")

# Open Write to file
writeFile = open("output.csv", "w+")

for line in file:
	if(re.search('^' + re.escape(tempClass), line)):
		values = line.split("\xad")
		left = values[0].strip().split("\xa0")

		writeFile.write(left[0] + "\t")
		writeFile.write(left[1] + "\t")
		writeFile.write(values[1].strip() + "\n")

print("Finished!")		


