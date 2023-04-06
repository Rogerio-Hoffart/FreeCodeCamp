import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
position = int(input('Enter Position:'))
counter = int(input('Enter Count:'))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
print('Retrieving:', url)

def searchingfor(x):
    count = 0
    for tag in x:
        # Look at the parts of a tag
        # #print('TAG:', tag)
        count += 1
        if count == position:
            #tags = tag.get('href')
            url = (tag.get('href'))
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, "html.parser")
            tags = soup('a')
            #print(tags)
            y = tags
            print('Retrieving:', tag.get('href', None))
            return y

for x in range(counter):
    y = searchingfor(tags)
    #print(tags)
    tags = y

    #print('Contents:', tag.contents[0])
    #total += int(tag.contents[0])
    #print('Attrs:', tag.attrs)


'''fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())'''
