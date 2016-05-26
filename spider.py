import sys
from bs4 import BeautifulSoup
import urllib2
import re


if len(sys.argv) < 2:
    print '%s url limit' % sys.argv[0]
    sys.exit(0)

url = str(sys.argv[1])
limit = sys.argv[2]

head = {'User-Agent' : "geckoO"} 
req = urllib2.Request(url, headers=head)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page.read())
for a in soup.findAll('a', href=True):
    if re.match('^\/\/[a-z0-9]', a['href']):
        current_a = re.sub(r'^\/\/', '', a['href'])
    if re.match('^\/[a-z0-9]', a['href']):
        current_a = url + a['href']

    print current_a
