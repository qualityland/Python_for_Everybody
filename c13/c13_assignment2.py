import urllib.request, urllib.parse, urllib.error
import ssl
import json
# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_42.json'
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_1370902.json'
raw = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(raw), 'characters')
data = json.loads(raw)
comments = data['comments']
print(comments)

sum = 0
for comment in comments:
    count = int(comment['count'])
    sum += count
print(sum)
