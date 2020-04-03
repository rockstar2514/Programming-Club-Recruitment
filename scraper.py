# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 13:27:16 2020

@author: dawood bin mansoor
"""
import requests
import urllib3
import time
import csv
from bs4 import BeautifulSoup

quote_page = 'https://summerofcode.withgoogle.com/archive/2019/projects/'
response = requests.get(quote_page)


soup= BeautifulSoup(response.content,'html.parser')

#price_box = soup.find('div', attrs={'class':'price'})
#price = price_box.text
#print(price)
with open('info.csv','a',encoding="utf-8",newline='') as csv_file:
     writer = csv.writer(csv_file)
     writer.writerow(["Name","Project","Organization"])
     for name_box in soup.find_all('h4',class_="archive-project-card__student-name"):
        name = name_box.text.strip()
        #print(name)
        prop=name_box.find_all_next('div',limit=2)
        project=prop[0].text.strip()
        #print(project)
        Organization=prop[1].text.strip()
        Organization=Organization[14: ]
        #print(Organization)
        writer.writerow([name,project,Organization])

		
    



