        # requests api 

import json
import requests

# This is a link of saral,which contains data and it will send request to this link:

data=requests.get("https://saral.navgurukul.org/api/courses").text

# Here it will write data in open.json file from link:

with open ("open.json","w")as file:
	json.dump(data,file,indent=4)
from pprint import pprint

# Here it will read open.json file and convert json data into dictionary format:

with open("open.json","r")as f:
	t=(json.load(f))
	l=json.loads(t)
	j=(l["availableCourses"])
	c=0

# This loop for pickup all courses name from availableCourses and for doing serial number:

	for i in j:
		n=(i["name"])
		c+=1
		print(c,".",n)
	l=[]

# This loop for pickup all id of courses and append into list l:

	for ide in j:
		a=ide["id"]
		l.append(a)
print()

# This input for selecting courses by entering serial number:

u=int(input("Enter your course: "))
print()
id=(l[u-1])
print("id of course =",id)
print()

# Here it will send again request for getting exercises related to his id:

data2=requests.get('http://saral.navgurukul.org/api/courses/'+str(id)+'/exercises').text
with open ("open.json","w") as v:
	json.dump(data2,v,indent=4)
from pprint import pprint

# This for topic contents:

with open("open.json","r") as k:
	s=json.load(k)
	h=json.loads(s)
	d=(h["data"])
	c=0
	l1=[]
	slugs=[]

# This loop for pickup all exercises names and slug: 

	for a in d:
		m=(a["name"])
		c+=1
		m1=a["slug"]
		l1.append(m1)
		print()
		q=(a["childExercises"])
		print(c,".",m)
		co=0
		t=[]

# This loop for pickup all childExercises name and slug of different contents:

		for j in q:
			z=(j["name"])
			co+=1
			t.append(j["slug"])
			print("              ",co,".",z)
			print()
		
		slugs.append(t)
print()

# This input for selecting exercises by entering serial number:

user1=int(input("Enter your exercises: "))
a1=l1[user1-1]
print()
print(a1)
print()

# This loop for printing slugs of exercises:

for s in slugs[user1-1]:
	print("     ",s)
						
	









































































# # # # a=["1.umesh","2.bijender","3.sonu"]
# # # # i=["23","24","25"]
# # # # for j in a:
# # # # 	print(j)
# # # # n=int(input("enter number"))
# # # # print(i[n-1])
























# # # # c=1
# # # # for i in range(96,123):
# # # # 	print(chr(i),c)
# # # # 	c+=1
