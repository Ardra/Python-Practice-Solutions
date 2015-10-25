'''Problem 8: Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked from that webpage.'''
import re
import urllib
def link(url):
    page= urllib.urlopen(url)
    list = re.findall('http://[\w\d\s.-]+.html', page.read())
    for x in list:
        print x
