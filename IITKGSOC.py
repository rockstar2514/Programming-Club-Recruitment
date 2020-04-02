# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:03:23 2020

@author: dawood bin mansoor
"""

import json
import csv 
class Set3:
    def __init__(self, n, r, d):
        self.name=n
        self.roll=r
        self.dept=d
def Lex(Set):
    return(sorted(Set, key=lambda x: x.name))      
def valid(a):
    valid=0
    k=0;
    l=1;
    for c in a:
        if (c.isupper()):
            valid=1
        if(c==' ' and k!=2):
            k=1
        if(c.isupper() or c.islower() or c==' '):
            if(k==1 and c!=' '):
                k=2
        else:
            l=0
            
    
    if(k==2 and valid == 1 and l==1):
        return True
    else:
        return False
    
        
with open('students.json',encoding="utf-8") as f:
    data=json.load(f)
    
jname=[]    
namej=[]
print("People With Illegal Names")
for emp in data:
      a=emp["n"]
      if(valid(a)):
            jname.append(Set3(emp["n"],emp["i"],emp["d"]))
      else:
            print(a)      
namec=[]      

with open('info.csv',encoding="utf-8") as csv_file:
    csv_reader= csv.reader(csv_file,delimiter=',')
    line_count=0
    for row in csv_reader:
        if line_count == 0:
            None
        else:
            a=row[0]
            if(valid(a)):
                  namec.append(Set3(row[0],row[1],row[2]))
            else:
                  print(a)
        line_count+=1
finalJSON=Lex(jname)        
finalCSV=Lex(namec)

a=0


b=0
print("Common Candidates")
while(a<len(finalJSON) and b<len(finalCSV)):
     if(finalJSON[a].name==finalCSV[b].name):
          print(finalJSON[a].name,end='  Roll No.:- ')
          print(finalJSON[a].roll,end=' Branch:- ')
          print(finalJSON[a].dept,end='  Organization:- ')
          print(finalCSV[b].dept,end='  Project Topic:-')
          print(finalCSV[b].roll)
          a+=1
          b+=1
     elif(finalJSON[a].name<finalCSV[b].name):
         a+=1
     else:
         b+=1
                  