import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


sum = 0

address = input('Enter location: ')


url =  address
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
data = data.decode()
commentinfo = ET.fromstring(data)
lst = commentinfo.findall('comments/comment')
print('Comment Count: ', len(lst))
for item in lst:
    x = (item.find('count').text)
    x = float(x)
    sum = x + sum

print(sum)








