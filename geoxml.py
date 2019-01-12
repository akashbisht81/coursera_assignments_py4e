import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://py4e-data.dr-chuck.net/comments_118022.xml'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    url = serviceurl

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)
    results = tree.findall('comments//comment/count')
    mycount=0
    for item in results:
        lat = item.text
        mycount=int(mycount)+int(lat)
    print(mycount)
    #faltu ke comments jo kaam ke nahi the un sabko maine ek taraf kar diya hai yaha neeche, kyuki program code neat lagna chahiye, warna koi bhi confuse hojayega...
    # + urllib.parse.urlencode({'address': address})
    # print(data.decode())
    # for item in tree:
    # counts = tree.findall('.//count')
    # print(results)
    # print('count',item.find('count').text)
    # print(lat)
    # lng = results[0].find('geometry').find('location').find('lng').text
    # location = results[0].find('formatted_address').text
    # print('lat', lat, 'lng', lng)
    # print(location)
