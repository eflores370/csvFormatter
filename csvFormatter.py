import re
import sys

classArray = ["CNIT", "MATH", "CS"]

def getFile():
	print("======================")
	print("1. CNIT Major")
	print("2. CS Major")
	fileName = input("File Name/Number: ")
	if fileName == "1":	
		fileName = "CNITMajor.txt"
	elif fileName == "2":
		fileName = "ComputerScienceMajor.txt"
	return fileName

def writeOutput(fileName):
# Open Write to file
	writeFile = open("output.csv", "w+")
	for item in classArray:
		# Open Text file
		file = open(fileName,"r")
		for line in file:
			if(re.search('^' + re.escape(item), line)):
				values = line.split("\xad")
				left = values[0].strip().split("\xa0")

				writeFile.write(left[0] + "\t")
				writeFile.write(left[1] + "\t")
				writeFile.write(values[1].strip() + "\n")

fileName = getFile()

writeOutput(fileName)

print("Finished!")		


