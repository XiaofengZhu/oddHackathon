import sys, json

f = open("termDetails.txt")
jsonObj = json.loads(f.read())

output=[]

for obj in jsonObj:  
    termDict={}
    termDict['id']=obj['id']
    termDict['year']=obj['year']
    termDict['quater']=obj['quater']

    output.append(termDict)


# years = list(set([i['year']for i in jsonObj])) #[2005,2007,....]
# output['years'] = years

# terms= list(set([i['quater']for i in jsonObj]))
# output['quaters'] = quaters
print output
f.close()
