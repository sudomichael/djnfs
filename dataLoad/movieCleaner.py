from bs4 import BeautifulSoup
#!/usr/bin/env python
# -*- coding: utf-8 -*- 


content = ""
with open ('movies.txt', 'r') as textFile:
    content = textFile.read()

soup = BeautifulSoup(content, 'html.parser')
fw = open('txtonly.txt', 'w')
text2 = (str(soup.getText().encode('utf-8')))
text4 = text2;
for x in range(1940, 2017):
    text4 = text4.replace(str(x), '');
for x in range(0, 30):
    thisstring = "Season " + str(x);
    thatstring = "Series " + str(x);
    text4 = text4.replace(thatstring, '');
    text4 = text4.replace(thisstring, '')
badchars = ['-', '(U.S.)', '(U.K.)', '(', ')', '#', "'", "...", ", the"]

for x in badchars:
    text4 = text4.replace(x, '');


fw.write(text4)
fw.close()
