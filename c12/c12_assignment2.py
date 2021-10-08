import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_1370899.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all of the anchor tags
tags = soup('span')
nums = list()
for tag in tags:
    num = int(tag.contents[0])
    nums.append(num)
print(sum(nums))
