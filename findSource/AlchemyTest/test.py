import sys


#for json call only
import json

def calTerm(year, quater):

	#return list
	output = ""

	f = open("termDetails.txt")
	jsonObj = json.loads(f.read())

	for res in jsonObj:
		if((res['year']==year) and (res['quater']==quater)):
			output=res['id']
	return output


