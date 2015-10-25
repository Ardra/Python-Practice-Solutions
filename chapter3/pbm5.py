'''Problem 5: Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html.'''
def wget(url):
    import sys
    import urllib
   
    file_name = url.split('/')[-1]
    if '.html'in file_name:
        urllib.urlretrieve(url, filename = file_name)
        print 'saving'+' '+url+'as'+file_name
    else:
        urllib.urlretrieve(url, filename = 'index.html')
        print 'saving'+' '+url+'as'+' '+'index.html'
        
        
