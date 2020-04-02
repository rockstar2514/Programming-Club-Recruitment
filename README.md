# Programming-Club-Recruitment
The files in this directory are solution of the first question.
The program can be run by importing the  scraper.py and IITKGSOC.py files and the students.json file to the 
same directory on a computer and running the program with a good enough Internet 
Connection.
Steps:-
1. Import files to a directory on a computer with a working Internet Connection( Do not import info.csv . Program will fail ).
2. Now, run scraper.py. This will generate a .csv file.
3. Now run IITKGSOC.py and the result will come on stdout.

Note- 
I have made a mistake by naming the Set3 variables as roll and dept.  It does not make sense when I use it to store Organization 
and Project name too. Please ignore the ethical blunder. 

XXX------------------------------Implementation---Part----------------------------------------------XXX

scraper.py

This file has the program which scraps the GSOC website and extracts the 
name of candidates from it. It uses BeautifulSoup3 for the job. It scanned 
for all <h> tags with a specific class (refer code). From there on find_all_next("a",limit=2) 
was used to find Project name and Organization Name. We stored all this data in .csv file 
(row wise (except row no.1 which contains headings)).
  
IITKGSOC.py

In this we have a .json databse and the previously generated .csv file which we need to process 
to give incorrect names in .csv file ( It is ambiguous from the question wheather Incorrect names 
from both files or just the .csv file need to be printed, but i have assumed this, Nevertheless,
I just have to replace line 50  with print(a) ) and then print common candidates with their Roll No.
Dept and other Data. The searching Algorithm has complexity O(mlogm + nlogn) where m and n are sizes 
of the .json and .csv files respectively. It does so by sorting name wise and then using two pointers 
on both lists to traverse it. If there is a match print else increment the pointer of the lists corresponding 
to the lexicographically smaller string. Sorting requires O(mlogm + nlogn) and this O(m+n). Hence, O(mlogm+nlogn).




