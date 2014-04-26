import urllib


#for json call only
import json

def calTerm(name):

	#return list
	output = ''

	url="http://vazzak2.ci.northwestern.edu/terms"
	page=urllib.urlopen(url)
	data=page.read()

	dict_data=json.loads(data)

	for data in dict_data:
		if (data['name']==name):
			output=data['term_id']

	return output



