
#data scraping from cleartrip phase 1
import csv
from bs4 import BeautifulSoup
import urllib2

url='https://www.cleartrip.com/trains/list?page=5'
page=urllib2.urlopen(url)
soup=BeautifulSoup(page.read(), "html.parser")

#print soup.prettify()
table=soup.find('tbody')

outfile=open('./train_list.csv','a')
writer=csv.writer(outfile)

for row in table.findAll('tr'):
    list_of_rows=[]
    list_of_cells=[]
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text)
    list_of_rows.append(list_of_cells)
    writer.writerows(list_of_rows)

outfile.close()
