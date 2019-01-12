import urllib.request, urllib.parse,urllib.error
import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

url= input('Enter URL::-')
print('Retrieving',url)
rawdata=urllib.request.urlopen(url).read()
data=rawdata.decode()
print('Retrieved: ',len(data),' Characters')
info = json.loads(data)
sum=0
count=0
# print(json.dumps(info,indent=4))
for item in info["comments"]:
    count+=1
    sum+=int(item["count"])
print('Count:',count)
print('Sum: ',sum)
        # print('Each count',item["comments['count']"])

         # counts=["comments"]["counts"]
         # print(counts)

     # print('Name', item['name'])
     # print('Id', item['id'])
     # print('Attribute', item['x'])
