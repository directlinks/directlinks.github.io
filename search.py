!#/usr/env/python
import cgi
data=cgi.FormContent()
print "Content-Type:text/html\n"

import urllib2
import requests
from bs4 import BeautifulSoup
print data
print "bye"

'''
global citelinks,watchable,srcoflinks, nondownloadable
citelinks=[]
watchable=[]
nondownloadable=[]
srcoflinks=[]
url="https://google.com/search?q=" + cat + " biqle.ru" 
print url


def linkscrapper(url):

	r=requests.get(url)
	soup= BeautifulSoup(r.content,"html.parser")
	#print soup
	global cite

	cite=soup.findAll('cite')
	print cite
	for i in range(len(cite)):
		if "biqle" in str(cite[i]):

			link= cite[i].text
			#print "\n\n\n\n" 
			#print link
			link=str(link)
			citelinks.append(link)
			print citelinks
		else:
			i=i


linkscrapper(url)

def requestmoduleforredirection(citelinks):
	r= requests.get(citelinks)
	soup= BeautifulSoup(r.content,"html.parser")
	a= soup.findAll('a')

	for i in range(len(a)):
			if "watch" in str(a[i]):
				href=a[i].attrs['href']
				href=str(href)
				href="https://biqle.ru" + href
				watchable.append(href)
				print "getting watch link " + str(i)
			else:
				i=i
for i in range(len(citelinks)):
	print "fetching from citelink " + str(i)
	if "https://" not in citelinks[i]:
		citelinks[i]= "https://" + str(citelinks[i])
	requestmoduleforredirection(citelinks[i])

def grabsrc(watchable):
	for i in range(len(watchable)):
		print "fetching src of " + str(i)
		try:
			url="http://www.tubeoffline.com/downloadFrom.php?host=PornHub&video=" + watchable[i]
			r=requests.get(url)
			if "3 super easy" in r.content:
				print "hi" + 5
			else:
				soup3 = BeautifulSoup(r.content,"html.parser")
				a= soup3.findAll('a')
				src= a[16].attrs["href"].encode("ascii","encode")
				print src
				srcoflinks.append(src)
		except:
			nondownloadable.append(watchable[i])

grabsrc(watchable)


print srcoflinks

length=len(srcoflinks)
f=open(cat+".txt","w")
for i in range(length/20):
	
	for i in range(20):
			src=str(srcoflinks[i])
			f.write(src)
			f.write("\n")
	f.write("\n\n")
	f.write ("------------above are 20 links-----------------")
	del srcoflinks[0:20]
	f.write("\n\n")

length=len(srcoflinks)

if length!=0:
	for i in range(length):
		f.write("\n")
		src=str(srcoflinks[i])
		f.write(src)
		f.write("\n")
f.close()
'''
