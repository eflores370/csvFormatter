import os
import re
import sys
import requests

classArray = ["CNIT", "MATH", "CS","VMD","LIBR"]

def askUser():
	while True:
		userFile = input("Download PDF(1) or Local File(2): ")
		if not (userFile == "1") and not (userFile == "2"):
			print("Error: Please enter 1 or 2")
		elif userFile == "1":
			return getPDF()
		elif userFile == "2":
			return getFile()


def getFile():
	print("======================")
	print("1. CNIT Major")
	print("2. CS Major")
	fileName = input("File Name/Number: ")
	if fileName == "1":	
		fileName = "CNITMajor.pdf"
	elif fileName == "2":
		fileName = "ComputerScienceMajor.pdf"
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

# Pulls PDF from web
def getPDF():
	wf = open("temp.pdf", 'wb')
	url = input("Enter PDF url: ")
	r = requests.get(url, stream = True)

	with open('temp.pdf', 'wb'):
		wf.write(r.content)

	return "temp.txt"


fileName = askUser()

os.system("pdf2txt.py temp.pdf > temp.txt")

writeOutput(fileName)

print("Finished!")		

os.system("cat output.csv")


