import webbrowser
import bs4 as bs
from urllib.request import Request, urlopen
import urllib
import requests
from urllib.request import FancyURLopener

def ytDownloader(word):
	a=[]
	

	url = 'https://www.youtube.com/results?search_query=+'+word
	yt='https://www.youtube.com'
	#webbrowser.open_new_tab(url)

	class MyOpener(FancyURLopener):
	    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'   # Set this to a string you want for your user agent

	myopener = MyOpener()
	page = myopener.open(url).read()
	webpage = page.decode('utf-8')

	soup = bs.BeautifulSoup(webpage,'lxml')

	div = soup.body
	for data in div.find_all(href=True):
		a.append(data.get('href'))

	#print(a)

	matching = [s for s in a if '/watch?' in s]
	# print(matching[0])

	ytplaylink = yt+matching[0]

	# print(ytplaylink)
	# pwrshllink= 'powershell -command Invoke-WebRequest '+ytplaylink+' -OutFile '+word+'.mp3'
	webbrowser.open_new_tab(ytplaylink)


word = input('Enter the video name')
ytDownloader(word)
