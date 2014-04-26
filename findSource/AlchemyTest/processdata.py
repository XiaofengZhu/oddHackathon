import urllib
import json

def readJson():

	#return list
	output={}

	url="http://vazzak2.ci.northwestern.edu/terms/"
	page=urllib.urlopen(url)
	data=page.read()

	dict_data=json.loads(data)

	# output['years']=dict_data['year']
	# output['quater']=dict_data['quater']
	# output['id']=dict_data['id']

	# print dict_data[0]['name']

	# f = open("termDetails.txt")
	# jsonObj = json.loads(f.read())


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

	# f.close()
	# return jsonObj

	return dict_data

