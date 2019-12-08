import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime



headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

base_url = 'https://rasp.unecon.ru/raspisanie_grp.php?g=12057'

def unecon_parse(base_url, headers):
    session =  requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        rasp = soup.find_all('div',class_='rasp')
        table = soup.find_all('table')
        
       #div = soup.find_all('td', attrs={'class':'day'})
       #div1 = soup.find_all('td',attrs ={'colspan': '5'})
       #div2 = soup.find_all('td',attrs ={'class': 'no_480 time'})
       #div3 = soup.find_all('td',attrs ={'class': 'no_768 aud marker'})
       #div4 = soup.find_all('span',attrs ={'class': 'predmet'})
       #div5 = soup.find_all('span', attrs)
        
        for cash in rasp:
            s = cash.find_all('h1')
            ss = s[0].text.strip()
            print(ss)
            
            b = cash.find_all('h2',class_='current_date_week')
            bb = b[0].text.strip()
            print(bb)
            
            v = cash.find_all('span',class_='week')
            vv = v[0].text.strip()
            print('Расписание с',vv)
            print('<><><><><><><><><><><><><><><><><><><><><><>')
        
        
        #print('Кол-во дней',len(div))
        #print('Кол-во разделительныйх полос, после начальной идет понедельник',len(div1))
        #print('Кол-во времени',len(div2))
        #print('Кол-во аудиторий',len(div3))
        #print('Кол-во предметов',len(div4))
        #print('\n','\n')
        
        i=0
        tt=''                
        while i <=17:
            for jak in table:
                    dayy = jak.find_all('td',class_='day')
                    row = dayy[i].text.strip()
                    if row != tt:
                        print('-------------------------------','\n',row)
             
                    timee = jak.find_all('td', class_='no_480 time')
                    row1 = timee[i].text.strip()           
                    print(row1,)
                                                                                                                                     
                    predmett = jak.find_all('span', class_='predmet')
                    row3 = predmett[i].text.strip()                           
                    print(row3,)
            i+=1       
    else:
        print('ERROR')
       
        
        
       
        

        
        
        
        
       
       
       
       

unecon_parse(base_url,headers) 


