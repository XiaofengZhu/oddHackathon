import requests
r = requests.get('http://vazzak2.ci.northwestern.edu/courses/?term=4530&subject=MATH');
data =  r.json()
