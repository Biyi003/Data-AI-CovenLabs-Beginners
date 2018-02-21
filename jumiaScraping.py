#import Libraries
import urllib
import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen

data = []
#declare url
urltoScrap = "https://www.olx.com.ng/m/mobile-phones-tablets/q-iphone7-plus/"

#urltoScrap = "http://www.bloomberg.com/quote/SPX:IND"

#query the url
page = urlopen(urltoScrap)

#parse the html
parsed_html = BeautifulSoup(page, 'html.parser')
device_details = parsed_html.find_all('div', class_ = 'info-top')

for i in range(len(device_details)):
    first = device_details[i]
    name = first.find('p', class_ = 'title').text.strip()
    price = first.find('span', class_ = 'price').text.strip()
    price = price[3:]
    data.append([name,price])

myFile = open('index.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(data)   

print("Scrapped!!!")