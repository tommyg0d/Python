import requests
from bs4 import BeautifulSoup as bs
#from datetime import datetime, date, time


headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

base_url = 'https://rasp.unecon.ru/raspisanie_grp.php?g=12055'

def unecon_parse(base_url, headers):
    session =  requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        
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
            
        data = soup.find('table') 
        dataa = data.find_all('span', class_='date')
        dataaa = dataa[day_nedeli].text.strip()
        print(dataaa)
        
    
        
       
        
        tbody = soup.find('tbody')
        time = soup.find('table')
        while tbody in time:
            
            i=j=k=0 
            
            timee = time.find_all('span', class_='time')
            if timee[i].text.strip() == timee[i+1].text.strip():
                timeee = timee[i].text.strip()
                i =i+1
                print(timeee)
            else:
                timeee = timee[i+1].text.strip()
                print(timeee)
                
            
            aud = soup.find('table')
            audd = aud.find_all('span', class_='aud')
            if audd[j].text.strip() == audd[j+1].text.strip():
                auddd = audd[j].text.strip()
                j = j+1
                print(auddd)
            else:
                auddd = audd[j+1].text.strip()
                print(auddd)
            
            predmet = soup.find('table')
            predmett = predmet.find_all('span', class_='predmet')
            if predmett[k].text.strip() == predmett[k+1].text.strip():
                predmettt = predmett[k].text.strip()
                k = k+1
                print(predmettt)
            else:
                predmettt = predmett[k+1].text.strip()
                print(predmettt)
            
        
        

unecon_parse(base_url,headers) 



