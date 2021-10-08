import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ') or 'http://py4e-data.dr-chuck.net/known_by_Cacie.html'
count = int(input('Enter count: ') or 7)
pos = int(input('Enter position: ') or 18)

for c in range(count + 1):
    print('Retrieving:',url)
    # parse html
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # retrieve 3rd entry of anchor tags
    tags = soup('a')
    url = tags[pos - 1].get('href', None)
