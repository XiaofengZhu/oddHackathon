import sys, json

def readJson():

	#return list
	output = []

	f = open('/static/findSource/data/termDetails.txt','r')
	jsonObj = json.read(f.read())

	# for obj in jsonObj:  
	#     termDict={}
	#     termDict['id']=obj['id']
	#     termDict['year']=obj['year']
	#     termDict['quarter']=obj['quarter']

	#     output.append(termDict)


	# years = list(set([i['year']for i in jsonObj])) #[2005,2007,....]
	# output['years'] = years

	# terms= list(set([i['quater']for i in jsonObj]))
	# output['quaters'] = quaters

	f.close()
	output['term']=jsonObj
	return output
