import urllib.request, urllib.parse, urllib.error
import json

while True:
    counter = 0
    address = input('Enter URL: ')
    if len(address) < 1: break

    url = address
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    info = data.decode()
    newinfo = json.loads(info)
    print(newinfo)
    for item in newinfo['comments']:
        counter += item['count']
    print(counter)

