import csv
from bs4 import BeautifulSoup
import urllib2

url='http://runningstatus.in/status/13006-on-20161107'
page=urllib2.urlopen(url)
soup=BeautifulSoup(page.read(), "html.parser")

table=soup.find('tbody')
for row in table.findAll('tr'):
    f=0
    for cell in row.findAll('td'):
        if f==0:
            print cell.text+" ",
            f=1
    a=cell.find("font",{"color":"red"}) #this does not work 
    if a is None:
        print "Shit"
    else:
        print a.text
    
    #But this does
    #print cell.find('font',{'color':'red'}) 
