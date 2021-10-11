import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_1370901.xml'
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)
print(tree)

# list of trees (tags)
lst = tree.findall('comments')
print('Comments count:', len(lst))
# for item in lst:
#     print('Count', item.text)
