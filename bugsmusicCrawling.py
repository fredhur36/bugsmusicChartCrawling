#!/usr/bin/python
from sys import platform
import requests
import csv
from bs4 import BeautifulSoup
# This program crawls bugsmusic chart 
# then prints 1 ~ 100 chart of korea music as .txt or .csv

response=requests.get('https://music.bugs.co.kr/chart') # get response of bugsmusic chart

html=response.text
soup=BeautifulSoup(html,'html.parser')

song_name_list_tag=soup.find_all("p",{"class":"title"}) # get music title
song_name_list=[]

artist_name_list_tag=soup.find_all("p",{"class":"artist"})# get artist name
artist_name_list=[]


# this part is crawling part
#-------------------------------------#
#make array which saves song_name_list
k=0
for i in song_name_list_tag:
    tmp=(i.get_text())
    tmp=tmp[1::]
    song_name_list.append(tmp.strip('\r\n'))
    
#-----end of crawling song_name-------#   
# crawling artist name list
k=0
for j in artist_name_list_tag:

    tmp=(j.find('a').text)
    artist_name_list.append(tmp.strip('\r\n'))
    
# crawling part is ended
#---------------------------------#


#----------------------------------------------#
# now write txt or csv file for data showing.#
#----------------------------------------------#
print("Press 1 + Enter is printing file to txt,and Press 2 + enter is printing file to csv")
flag=input("choose file type, then press enter : ")
if(flag=="1"): # writing_file_to_txt
    
    writing="bugsmusic_chart"+".txt"
    #---- change new line depends on Operating System----#
    if(platform=="linux"): 
        new_line="\n"
    elif(platform=="win32"): 
        new_line="\r\n"
    elif(platform=="darwin"):
        new_line="\n"
    #--------------------------------------------------#
    f=open(writing,'w',encoding='utf-8',newline="")# file_open (.txt file)
    for i in range(0,100):
        f.write(str(i+1)+'.') # write ranking
        f.write(song_name_list[i].replace(u'\xa0',' '));
        f.write(' ');
        f.write(artist_name_list[i].replace(u'\xa0',' '))
        f.write(new_line)
    f.close()


else: #writing_file_to_csv
    
    writing="bugsmusic_chart"+".csv"
    f=open(writing,'w',encoding='euc_kr',newline="")#file_open and encoding(.csv file)
    csvWriter=csv.writer(f)
    for i in range(0,100):
        song_name_list[i] = song_name_list[i].replace(u'\xa0',' ')
        artist_name_list[i] = artist_name_list[i].replace(u'\xa0',' ')
        csvWriter.writerow([song_name_list[i],artist_name_list[i] ])
    f.close()
    
