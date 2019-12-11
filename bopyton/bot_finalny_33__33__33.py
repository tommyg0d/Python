import vk_api
import random
import json
import bs4
import requests
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
from bs4 import BeautifulSoup as bs
import wikipedia



appid = '9012a24470566b92443cac530ba95cc9'

import requests



# Проверка наличия в базе информации о нужном населенном пункте
def get_city_id(s_city_name):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                     params={'q': s_city_name, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        print("city:", cities)
        city_id = data['list'][0]['id']
        print('city_id=', city_id)
    except Exception as e:
        print("Exception (find):", e)
        pass
    assert isinstance(city_id, int)
    return city_id

# Запрос текущей погоды
def request_current_weather(city_id):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                     params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()

        os=("&#127782; осадки:", data['weather'][0]['description'],"\n&#127777; температура:", data['main']['temp'],"\n&#10145; минимальная температура:", data['main']['temp_min'],"\n&#10145; максимальная температура:", data['main']['temp_max'])


        return os


    except Exception as e:
        print("Exception (weather):", e)
        pass


#city_id for SPb
city_id = 498817



request_current_weather(city_id)
text=(request_current_weather(498817))

with open("pogoda.txt",'w') as file:
    with open("pogoda.txt", "w") as file:
        print(*text, file=file)

#text=open("pogoda.txt","r", encoding="utf-8").read()
text=open("pogoda.txt","r").read()
# РАСПИСАНИЕ_______________________________
headers = {'accept': '*/*',
           'user-agent': ''}

base_url = 'https://rasp.unecon.ru/raspisanie_grp.php?g=12057'
file=open("rasp.txt",'w')
file.close()
file=open("rasp.txt",'a')
def unecon_parse(base_url, headers):
    session =  requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        rasp = soup.find_all('div',class_='rasp')
        table = soup.find_all('table')
        timee = soup.find_all('td', class_='no_480 time')
        div4 = soup.find_all('span',attrs ={'class': 'predmet'})
       
        
        for cash in rasp:
            s = cash.find_all('h1')
            ss = s[0].text.strip()
            file.write(ss)
            file.write('\n\n')
            
            b = cash.find_all('h2',class_='current_date_week')
            bb = b[0].text.strip()
            file.write('&#128204;'+bb+'\n')
            
            v = cash.find_all('span',class_='week')
            vv = v[0].text.strip()
            #file.write('Расписание с '+vv)
            file.write('\n')
            file.write('<><><><><><><><><><><><><><><><><>\n')
                   
        
        j= len(div4)
        i=0
        tt=''                
        while i <= j-1:
            for jak in table:
                    dayy = jak.find_all('td',class_='day')
                    row = dayy[i].text.strip()
                    if row != tt:
                        file.write('-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n\n\n')
                        file.write('&#128197;'+row+'\n')
             
                    
                
                    d1 = jak.find_all('span',class_='time only_480')  
                    row1 = d1[i].text.strip()
                    file.write(row1+'\n')
                    
                    aud = jak.find_all('td',class_='no_768 aud marker')
                    row2 = aud[i].text.strip()
                    file.write(row2+' ')
                                                                                                                                     
                    predmett = jak.find_all('span', class_='predmet')
                    row3 = predmett[i].text.strip()                           
                    file.write('\n'+row3+'\n\n\n')
            i+=1       
    else:
        print('ERROR')
       
        
unecon_parse(base_url,headers)        
file.close()
text1=open("rasp.txt","r").read()

def write_msg(user_id,message):
    vk.method('messages.send',{'user_id':user_id,'message':message,'random_id':random.randint(0,2048)})
def write_php(user_id,d):
    vk.method('messages.send',{'user_id':user_id,'attachment':d,'random_id':random.randint(0,2048)})
def write_key(user_id,key):
    vk.method('messages.send',{'user_id':user_id,'message':key,'keyboard':keyboard,'random_id':random.randint(0,2048)})





token='f337f49aa7c3df88539ed93512d0e3f44f561a573809e83716131486dc0019e1e4c705dc1e799a3524a55'
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

keyboard=open("keyboard1.json", 'r', encoding="utf-8").read()


while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me :
            request=event.text
            if request.lower() == 'привет':
                write_msg(event.user_id,"Доброе утро &#127774;")
                write_php(event.user_id,'photo-188882042_457239019')
            elif request.lower() == 'начать':
                write_msg(event.user_id,"Приветик!&#128075;\n Я знаю твое расписание, а еще уже успел выглянуть в окно и расскажу тебе о погоде на сегодняшний день.\nНепонятно значение какого-то слова? Я пришлю статью из Википедии!\nКнопки снизу помогут тебе.&#127752;")
                write_key(event.user_id,"&#11015;       &#11015;       &#11015;")
            elif request.lower() == 'кнопки':
                write_key(event.user_id,"Хотел, получай!")
            elif request.lower()=='погода':
                 write_msg(event.user_id,"Смотрим прогноз...&#127757;")
                 write_msg(event.user_id,text)
                 write_msg(event.user_id,"Одевайся по погоде!!&#128062;")
            elif request.lower()=='я ухожу!':
                write_msg(event.user_id, "Пока, мой друг! &#9829;")
            elif request.lower()=='расписание':
                write_msg(event.user_id,text1)
            elif request.lower()=='википедия':
                write_msg(event.user_id,"Введите слово/словосочетание которое хотите найти в Википедии:")
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me :
                        a=event.text

                        def wiki(a):
                            try:
                                    wikipedia.set_lang('ru')
                                    result =(wikipedia.page(a))
                                    return str((result.summary))
                        #text3=str((wiki(a)))
                        #write_msg(event.user_id,text3)

                            except Exception as e:
                                write_msg(event.user_id,"Нет такой статьи")
                                pass
                        
                        text3=str((wiki(a)))
                        write_msg(event.user_id,text3)
                        break
                
            

            else:
                write_msg(event.user_id, "Я не понимаю вашу команду... &#128575;")
