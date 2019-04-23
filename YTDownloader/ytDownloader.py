import webbrowser
import bs4 as bs
from urllib.request import Request, urlopen
import urllib
import requests
from urllib.request import FancyURLopener
import pynotify
from selenium import webdriver
import youtube_dl
import os
# import ffprobe


a=[]
a1=[]
word = input('ENTER THE VIDEO NAME TO DOWNLOAD')

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

ytplaylink = yt+matching[0]

print(ytplaylink)
def download():
		quality=input('WHICH QUALITY DO YOU WANT ME TO DOWNLOAD?')
		if '' in quality:
			pass
		if '240' in quality:
			r=os.system('youtube-dl -f 5 '+ytplaylink)
		if '360' in quality:
			r=os.system('youtube-dl -f 43 '+ytplaylink)
		elif '480' in quality:
			r=os.system('youtube-dl -f 18 '+ytplaylink)
		elif '720' in quality:
			r=os.system('youtube-dl -f 22 '+ytplaylink)
		if(r==1):
			print('THE FORMAT YOU SELECTED NOT FOUND... PELASE SELECT LOWER QUALITY')
			download()

download()
#webbrowser.open_new_tab(ytplaylink)