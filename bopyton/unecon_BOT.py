import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime



headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

base_url = 'https://rasp.unecon.ru/raspisanie_grp.php?g=12055'

def unecon_parse(base_url, headers):
    session =  requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        div = soup.find_all('tr',class_='day')
        #Введим день недели
        print('Введите день недели')
        day_nedeli = input()
        if day_nedeli == 'понедельник':
            day_nedeli = 0;
        if day_nedeli == 'вторник':
            day_nedeli = 1;
        if day_nedeli == 'среда':
            day_nedeli = 2;
        if day_nedeli == 'четверг':
            day_nedeli = 3;
        if day_nedeli == 'пятница':
            day_nedeli = 4;
        if day_nedeli == 'суббота':
            day_nedeli = 5;
            
            
        table = soup.find('table')    
        rows = table.find_all('td')
        linia = table.find('tr',class_='new_day_border')
        
        #печатается дата и день недели
        dataa = table.find_all('span', class_='date')
        dataaa = dataa[day_nedeli].text.strip()
        print(dataaa)
            
            
        i=j=k=9
        a=0
        for row in rows:
            
            if linia in row:
                a=a+1
                print('--------------------------------')
            
           
            
 
    while i != 13:
        while j != 13:
            while k!= 13:
                      
                       timee = table.find_all('span', class_='time')
                       row1 = timee[i].text.strip()           
                       i=i+1
                        
                
                        
                 
                       audd = table.find_all('span', class_='aud')
                       row2 = audd[j].text.strip()
                        
                       j=j+1
                        
                    
                          
                        
            
                       predmett = table.find_all('span', class_='predmet')
                       row3 = predmett[k].text.strip()
                        
                       k=k+1
                       print(row1,'\n',row2,'\n',row3)
    print(a)
        
        

unecon_parse(base_url,headers) 


