
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = input('Enter Count - ')
count = int(count)
count = count - 1
position = input('Enter Position - ')
position = int(position)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    tag.get('href', None)

url = (tags[position - 1])
url = str(url)
url = re.findall('href="(.+)">', url)
print(url)

while True:
    if count == 0:
        break
    else:
        html = urllib.request.urlopen(url[0], context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        for tag in tags:
            tag.get('href', None)
        url = (tags[position-1])
        url = str(url)
        url = re.findall('href="(.+)">', url)
        print(url)
        count = count - 1



