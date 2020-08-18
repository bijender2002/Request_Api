        # requests api 

import json
import requests
data=requests.get("https://saral.navgurukul.org/api/courses").text
with open ("open.json","w")as file:
	json.dump(data,file,indent=4)
from pprint import pprint
with open("open.json","r")as f:
	t=(json.load(f))
	l=json.loads(t)
	j=(l["availableCourses"])
	c=0
	for i in j:
		n=(i["name"])
		c+=1
		print(c,".",n)
	l=[]
	for ide in j:
		a=ide["id"]
		l.append(a)
print()
u=int(input("Enter your course: "))
print()
id=(l[u-1])
print("id of course =",id)
print()
data2=requests.get('http://saral.navgurukul.org/api/courses/'+str(id)+'/exercises').text
with open ("open.json","w") as v:
	json.dump(data2,v,indent=4)
from pprint import pprint
with open("open.json","r") as k:
	s=json.load(k)
	h=json.loads(s)
	d=(h["data"])
	c=0
	l1=[]
	slugs=[]
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
		for j in q:
			z=(j["name"])
			co+=1
			t.append(j["slug"])
			print("              ",co,".",z)
			print()
		
		slugs.append(t)
print()
user1=int(input("Enter your exercises: "))
a1=l1[user1-1]
print()
print(a1)
print()
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
