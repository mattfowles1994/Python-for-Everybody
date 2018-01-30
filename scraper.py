from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

l = soup.decode()

count = 0
sum = 0

numbers = re.findall('">([0-9]+)</', l)

print(numbers)


for figure in numbers:
    figure = float(figure)
    count = count + 1
    sum = figure + sum

print(count)
print(sum)