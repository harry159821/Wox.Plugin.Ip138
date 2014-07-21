#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2,json
from bs4 import BeautifulSoup

def query(Allkey):
	Allkey = Allkey.encode("utf-8")
	results = []		
	html = requests('http://www.ip138.com/')
	bs = BeautifulSoup(html)
	url = bs.select("tr td iframe")[0]['src']
	html = requests(url)
	html = html.decode('gb2312')#.encode('utf-8')
	bs = BeautifulSoup(html)
	res = {}
	res["Title"] = bs.select("body center")[0].text.encode('utf-8')
	#res["SubTitle"] = 
	res["IcoPath"] = './icon.png'
	results.append(res)
	return json.dumps(results)



#re.findall(r'\d+.\d+.\d+.\d+', s)

def requests(url,timeouts=5):
	header = {
			'Referer': 'http://www.ip138.com/',
			'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
			}	
	request = urllib2.Request(url,headers=header)
	response = urllib2.urlopen(request,timeout=timeouts)
	html = response.read()
	if html:	
		return html
	return False

def getIp(domain):
    import socket
    myaddr = socket.getaddrinfo(domain,'http')[0][4][0]
    return myaddr

if __name__ == '__main__':
	print query(u"ip")
