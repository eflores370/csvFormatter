import os
import re
import sys
import requests

classArray = ["CNIT", "MATH", "CS","VMD","LIBR"]

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
	writeFile = open("csv/output.csv", "w+")
	for item in classArray:
		# Open Text file
		file = open("txt/"+fileName,"r")
		for line in file:
			if(re.search('^' + re.escape(item), line)):
				values = line.split("\xad")
				left = values[0].strip().split("\xa0")

				writeFile.write(left[0] + "\t")
				writeFile.write(left[1] + "\t")
				writeFile.write(values[1].strip() + "\n")

def getPDF():
	wf = open("pdf/temp.pdf", 'wb')
	url = input("Enter PDF url: ")
	r = requests.get(url, stream = True)

	with open('pdf/temp.pdf', 'wb'):
		wf.write(r.content)

# Gets pdf document from URL
getPDF()

os.system("pdf2txt.py pdf/temp.pdf > txt/temp.txt")

# Gets fileName from the user
# fileName = getFile()
fileName = "temp.txt"

writeOutput(fileName)

print("Finished!")		


