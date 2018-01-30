import json
import urllib.request, urllib.parse, urllib.error

while True:
    url = input('Enter location: ')
    if len(url) < 1: break
    sum = 0
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    info = json.loads(data)

    scores = info['comments']
    for person in scores:
        score = person["count"]
        sum = score + sum
    print(sum)
