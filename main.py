import streamlit as st
from deta import Deta
from datetime import datetime
#from PIL import Image
import time
import json
import os
import pandas as pd
#import numpy as np
import re
import webbrowser

st.set_page_config(

    page_title="Мировое господство",
    page_icon="🚙",
    layout="wide",
    initial_sidebar_state="collapsed",  # expanded/collapsed
    menu_items={
        'Get Help': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'Report a bug': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'About': "# Автор MangoVirus"
    })


def info():
    code = '''Правила игры.
    1. Запрещены все угрозы в реальной жизни. Пример: 'Если ты не скинешь мне косарь, я с тобой перестану общаться!!!'
    2. Всем странам запрещено 'намерено уничтожать какую либо страну' в связи с обстановкой в реальном мире/личной неприязнью к конкретному человеку
        /по полу участников.
    3. Не давайте свои ключи другим людям. 'Ключ президента должен быть только у президента!'
    4. Перед тем как отправить запрос хорошо подумайте. 'Не надо спамить запросами.' Иначе они будут отказаны
    5. На протяжении всей игры ЗАПРЕШЕНО 'писать личные сообщения' другим странам или намерено портить игру другим, сливая информацию.
    6.  Во время этапа Дебатов всем странам кроме страны которая выступает, запрещается перебивать, шутить, включать Саундпады и т.д 
        Только если выступающая страна не задаст вопрос другой. В таком случае дается слово стране которой задали вопрос.
        Время на ответ на вопрос выступающей страны будет взято из времени выступающей страны.
    '''
    code1 = '''Странны участвующие в Мировом Господстве.
    Страна     Город 1    Город 2    Город 3   Город 4
    'Швеция' - Стокгольм, Мальмё,    Кируна,   Сигнута.
    'Сирия'  - Дамаск,    Хама,      Дума,     Ракка.
    'Индия'  - Нью-Дели,  Бангалор,  Агра,     Сурат.
    'Испания'- Мадрид,    Барселона, Пальма,   Гранда.
    'Канада' - Оттава,    Торонто,   Ванкувер, Виктория.
    'Россия' - Москва,    Санкт-Петербург, Екатеринбург, Магадан.
    '''
    code2='''Обратите внимание.
    Так обозначается 'целый' город 🏡
    Так обозначается 'уничтоженый' город 🏚️
    🛡️ - это 'щит', если в него прилетит ракет, то он сломается, а городу нанесется -20 от экологии 
    ⚙️- это 'уровню жизни' от неё зависит сколько денег вы получите в следующем раунде.(Деньги в след. раунде=сложить все ⚙️и умножить на 5)
    🌳 - это 'экология', если она упадет до 0 ваш город будет уничтожен.
    'Изучение ядерки' - в следующем раунде вы сможете производить ракеты.
    'Ракеты' - уничтожают город если на нем нет 'щита'. При производстве вы получите их в след. раунде. 
        Хранение ракеты наносит -0.5 общей экологии страны.
    '''
    st.code(code, language='python')
    st.code(code1, language='python')
    st.code(code2, language='python')
    st.error('Общее', icon="🚨")
    st.caption('⬆️ Это собщение видят все странны')
    st.warning('Личное',icon="⚠️")
    st.caption('⬆️ Это собщение видите только вы')

    '''# Над данным проектом работали'''
    st.subheader('MangoVirus')
    '''Разработчик сайта, создатель DataBase.'''
    st.subheader('Турба')
    '''Проектный руководитель, дизайнер.'''
    st.subheader(
        'Если вы хотите поддержать нас и в будущем видеть более маштабные нововедения вы можете скинуть нам пару тугриков по номеру телефона 8 (977) 382-41-17')
    '''Если вам нужна помощь по сайту или вы нашли баг, можете нажать на 3 полосочки справа и Get Help или Report Bug'''

with st.sidebar.container():
    col1, col2, col3, col4= st.columns(4)

    with col2:
        st.image('https://cdn.discordapp.com/attachments/890188503047077928/1070451124869533758/066443762463369c.png', width=128)

Country_Name=""
menu=''
ok=0
lid=0
com=0
string = st.sidebar.text_input('Введите ключ','')
new_string = string.lower()[1::2]
if new_string!='':
    com+=1
if com==0:
    st.title('Добро пожаловать в Мировое Господство!')
    st.error('Нет ключа', icon='‼️')
    st.info('Чтобы начать играть введите ключ, который вам дал представитель ООН', icon='ℹ️')
    st.info('Чтобы ввести ключ нажмите на стрелочку слева сверху', icon='ℹ️')
    info()
if new_string.find('-lid')>0:
    new_string=new_string.replace('-lid','')
    lid=1
if new_string == 'siria':
    Country_Name='Siria'
    test_name='Сирия'
    title_name='Сирию'
    city_1 = 'Дамаск'
    city_2 = 'Хама'
    city_3 = 'Дума'
    city_4 = 'Ракка'
elif new_string== 'india':
    Country_Name = 'India'
    test_name = 'Индия'
    title_name='Индию'
    city_1 = 'Нью-Дели'
    city_2 = 'Бангалор'
    city_3 = 'Агра'
    city_4 = 'Сурат'
elif new_string == "canada":
    Country_Name = 'Canada'
    test_name = 'Канада'
    title_name = 'Канаду'
    city_1 = 'Оттава'
    city_2 = 'Торонто'
    city_3 = 'Ванкувер'
    city_4 = 'Виктория'
elif new_string == 'ispania':
    Country_Name = 'Ispania'
    test_name = 'Испания'
    title_name='Испанию'
    city_1 = 'Мадрид'
    city_2 = 'Барселона'
    city_3 = 'Пальма'
    city_4 = 'Гранда'
elif new_string == 'shvechia':
    Country_Name = 'Shvechia'
    test_name = 'Швеция'
    title_name='Швецию'
    city_1 = 'Стокгольм'
    city_2 = 'Мальмё'
    city_3 = 'Кируна'
    city_4 = 'Сигнута'
elif new_string == 'russia':
    Country_Name = 'Russia'
    test_name = 'Россия'
    title_name='Россию'
    city_1 = 'Москва'
    city_2 = 'Санкт-Петербург'
    city_3 = 'Екатеринбург'
    city_4 = 'Магадан'
elif new_string=='vjcrdf11':
    Country_Name = 'vjcrdf11'
    menu=st.sidebar.selectbox('Меню',('Улучшение','Запуск ракет','Принятые запросы','Посещения','Перевод','Деньги','Логи'))

current_datetime = datetime.now()
deta = Deta("c07jfupdsmg_p62nqhnHwentnUYMZRxqXC4fxCzNEKyG")
Global = deta.Base("play")
if Country_Name!='':
    city = Global.get(f'{Country_Name}')
if Country_Name!='vjcrdf11' and Country_Name!='':
    money = int(city['money']) - ((int(city['sunks_of_you']) * 50) + (int(city['sunks_for_you']) * 100))
photo = deta.Base('photo')
pp = photo.get('qt2b4gngncsi')
log=deta.Base('log')
db = deta.Base('request_all')
Attak = deta.Base('request_attak')
request = deta.Base('request')
request_money = deta.Base('request_money')
wait=deta.Base('wait')

key=''
key1=''
lvl_eco=[0,0,0,0]
lvl_up=[0,0,0,0]
country1 = Global.get('India')
country2 = Global.get('Siria')
country3 = Global.get('Canada')
country4 = Global.get('Shvechia')
country5 = Global.get('Russia')
country6 = Global.get('Ispania')
if menu=='Деньги':
    give1=(country1['up1']+country1['up2']+country1['up3']+country1['up4'])*5
    st.success(f'ЗП для Индии {give1}',icon='🤑')
    give2=(country2['up1']+country2['up2']+country2['up3']+country2['up4'])*5
    st.success(f'ЗП для Сирии {give2}',icon='🤑')
    give3=(country3['up1']+country3['up2']+country3['up3']+country3['up4'])*5
    st.success(f'ЗП для Канады {give3}',icon='🤑')
    give4=(country4['up1']+country4['up2']+country4['up3']+country4['up4'])*5
    st.success(f'ЗП для Швеции {give4}',icon='🤑')
    give5=(country5['up1']+country5['up2']+country5['up3']+country5['up4'])*5
    st.success(f'ЗП для России {give5}',icon='🤑')
    give6=(country6['up1']+country6['up2']+country6['up3']+country6['up4'])*5
    st.success(f'ЗП для Филиппин {give6}',icon='🤑')
    if st.button('Выдать деньги'):
        give1=int(country1['money'])+give1
        Global.update({"money": give1}, "India")
        give2 = int(country2['money']) + give2
        Global.update({"money": give2}, "Siria")
        give3 = int(country3['money']) + give3
        Global.update({"money": give3}, "Canada")
        give4 = int(country4['money']) + give4
        Global.update({"money": give4}, "Shvechia")
        give5 = int(country5['money']) + give5
        Global.update({"money": give5}, "Russia")
        give6 = int(country6['money']) + give6
        Global.update({"money": give6}, "Ispania")
        st.success('Деньги успешно выданы!', icon='💰')
if menu == 'Улучшение':
    st.info('Запросы на улучшение')
    st.error('Не забудь заполнить санкции в ручную!')
    db_content = db.fetch().items
    for slash in range(0, len(db_content)):
        st.write(db_content[slash])
        if st.button(f'Принять улучшение {slash}'):
            slash += 1
            take=db.get(f'{slash}')
            wait_content=wait.fetch().items
            keys=len(wait_content)+1
            take_info=take['info']
            take_money=take['money']
            take_reserch=take['reserch']
            take_roket=take['roket']
            take_shit=take['shit']
            take_sunks_for_who=take['sunks_for_who']
            take_up=take['up']
            wait.put({'key':f'{keys}','info':f'{take_info}','money':take_money,'reserch':take_reserch,'roket':take_roket,'shit':take_shit,
                      'up':take_up,'action':'up'})
            db.delete(f'{slash}')
            st.success('Улучшение принято')
        if st.button(f'Отклонить улучшение {slash}'):
            slash+=1
            db.delete(f'{slash}')
            st.error('Улучшение удалено')
if menu=='Запуск ракет':
    st.info('Запросы на запуск ракет')
    db_content=Attak.fetch().items
    for slash in range(0,len(db_content)):
        st.write(db_content[slash])
        if st.button(f'Принять запуск {slash}'):
            slash += 1
            take= Attak.get(f'{slash}')
            wait_content = wait.fetch().items
            keys = len(wait_content) + 1
            take_info=take['info']
            take_final_roket=take['final_roket']
            take_country1=take['Сирия']
            take_country2 =take['Россия']
            take_country3 =take['Канада']
            take_country4 =take['Индия']
            take_country5 =take['Испания']
            take_country6 =take['Швеция']
            wait.put({'key': f'{keys}', 'info': f'{take_info}', 'Сирия': take_country1, 'Россия': take_country2,
                      'Канада': take_country3, 'Индия': take_country4,
                      'Испания': take_country5, 'Швеция': take_country6, 'action':'attak'})
            Attak.delete(f'{slash}')
            st.success('Запуск принят')
        if st.button(f'Отклонить запуск {slash}'):
            slash+=1
            Attak.delete(f'{slash}')
            st.error('Запуск удален')

if menu == 'Принятые запросы':
    st.info('Принятые запросы')
    db_content = wait.fetch().items
    for slash in range(0, len(db_content)):
        st.write(db_content[slash])
    if st.button('Завершить раунд'):
        for end in range(0,len(db_content)):
            end+=1
            wait_end=wait.get(f'{end}')
            if wait_end['action']=='attak' and int(wait_end['key'])>1:
                #key=int(wait_end['key'])-1
                #wait.update({'key':f'{key}'})
                pass
            elif wait_end['action']=='up':
                money_end = wait_end['money']
                roket_end=wait_end['roket']
                shit_end=wait_end['shit']
                up_end=wait_end['up']
                coutn = 0
                up_end1, up_end2, up_end3, up_end4 = up_end[0], up_end[1], up_end[2], up_end[3]
                if wait_end['info'].find('India')>0:
                    if wait_end['reserch']==1:
                        reserch=1
                    elif country1['reserch']==1:
                        reserch=1
                    else:
                        reserch=0
                    if country1['shit1']=='🛡️':
                        shit_end[0]='🛡️'
                    if country1['shit2']=='🛡️':
                        shit_end[1] = '🛡️'
                    if country1['shit3']=='🛡️':
                        shit_end[2] = '🛡️'
                    if country1['shit4']=='🛡️':
                        shit_end[3] = '🛡️'
                    Global.update({'money': money_end, 'reserch': reserch, 'roket': country1['roket']+roket_end,
                                   'shit1': shit_end[0], 'shit2': shit_end[1], 'shit3': shit_end[2], 'shit4': shit_end[3],
                                   'up1': country1['up1']+up_end1, 'up2': country1['up2']+up_end2, 'up3': country1['up3']+up_end3, 'up4': country1['up4']+up_end4,
                                   'eco1': country1['eco1']+up_end1,'eco2': country1['eco2']+up_end2,'eco3': country1['eco3']+up_end3,'eco4': country1['eco4']+up_end4}, 'India')
                elif wait_end['info'].find('Siria') > 0:
                    if wait_end['reserch'] == 1:
                        reserch = 1
                    elif country2['reserch'] == 1:
                        reserch = 1
                    else:
                        reserch = 0
                    if country2['shit1']=='🛡️':
                        shit_end[0]='🛡️'
                    if country2['shit2']=='🛡️':
                        shit_end[1] = '🛡️'
                    if country2['shit3']=='🛡️':
                        shit_end[2] = '🛡️'
                    if country2['shit4']=='🛡️':
                        shit_end[3] = '🛡️'
                    Global.update({'money': money_end, 'reserch': reserch, 'roket': country2['roket']+roket_end,
                                   'shit1': shit_end[0], 'shit2': shit_end[1], 'shit3': shit_end[2], 'shit4': shit_end[3],
                                   'up1': country2['up1'] + up_end1, 'up2': country2['up2'] + up_end2,
                                   'up3': country2['up3'] + up_end3, 'up4': country2['up4'] + up_end4,
                                   'eco1': country2['eco1'] + up_end1, 'eco2': country2['eco2'] + up_end2,
                                   'eco3': country2['eco3'] + up_end2, 'eco4': country2['eco4'] + up_end4}, 'Siria')
                elif wait_end['info'].find('Canada') > 0:
                    if wait_end['reserch'] == 1:
                        reserch = 1
                    elif country3['reserch'] == 1:
                        reserch = 1
                    else:
                        reserch = 0
                    if country3['shit1']=='🛡️':
                        shit_end[0]='🛡️'
                    if country3['shit2']=='🛡️':
                        shit_end[1] = '🛡️'
                    if country3['shit3']=='🛡️':
                        shit_end[2] = '🛡️'
                    if country3['shit4']=='🛡️':
                        shit_end[3] = '🛡️'
                    Global.update({'money': money_end, 'reserch': reserch, 'roket': country3['roket']+roket_end,
                                   'shit1': shit_end[0], 'shit2': shit_end[1], 'shit3': shit_end[2], 'shit4': shit_end[3],
                                   'up1': country3['up1'] + up_end1, 'up2': country3['up2'] + up_end2,
                                   'up3': country3['up3'] + up_end3, 'up4': country3['up4'] + up_end4,
                                   'eco1': country3['eco1'] + up_end1, 'eco2': country3['eco2'] + up_end2,
                                   'eco3': country3['eco3'] + up_end3, 'eco4': country3['eco4'] + up_end4}, 'Canada')
                elif wait_end['info'].find('Shvechia') > 0:
                    if wait_end['reserch'] == 1:
                        reserch = 1
                    elif country4['reserch'] == 1:
                        reserch = 1
                    else:
                        reserch = 0
                    if country4['shit1']=='🛡️':
                        shit_end[0]='🛡️'
                    if country4['shit2']=='🛡️':
                        shit_end[1] = '🛡️'
                    if country4['shit3']=='🛡️':
                        shit_end[2] = '🛡️'
                    if country4['shit4']=='🛡️':
                        shit_end[3] = '🛡️'
                    Global.update({'money': money_end, 'reserch': reserch, 'roket': country4['roket']+roket_end,
                                   'shit1': shit_end[0], 'shit2': shit_end[1], 'shit3': shit_end[2], 'shit4': shit_end[3],
                                   'up1': country4['up1'] + up_end1, 'up2': country4['up2'] + up_end2,
                                   'up3': country4['up3'] + up_end3, 'up4': country4['up4'] + up_end4,
                                   'eco1': country4['eco1'] + up_end1, 'eco2': country4['eco2'] + up_end2,
                                   'eco3': country4['eco3'] + up_end3, 'eco4': country4['eco4'] + up_end4}, 'Shvechia')
                elif wait_end['info'].find('Russia') > 0:
                    if wait_end['reserch'] == 1:
                        reserch = 1
                    elif country5['reserch'] == 1:
                        reserch = 1
                    else:
                        reserch = 0
                    if country5['shit1']=='🛡️':
                        shit_end[0]='🛡️'
                    if country5['shit2']=='🛡️':
                        shit_end[1] = '🛡️'
                    if country5['shit3']=='🛡️':
                        shit_end[2] = '🛡️'
                    if country5['shit4']=='🛡️':
                        shit_end[3] = '🛡️'
                    Global.update({'money': money_end, 'reserch': reserch, 'roket': country5['roket']+roket_end,
                                   'shit1': shit_end[0], 'shit2': shit_end[1], 'shit3': shit_end[2], 'shit4': shit_end[3],
                                   'up1': country5['up1'] + up_end1, 'up2': country5['up2'] + up_end2, 'up3': country5['up3'] + up_end3,
                                   'up4': country5['up4'] + up_end4,
                                   'eco1': country5['eco1'] + up_end1, 'eco2': country5['eco2'] + up_end2,
                                   'eco3': country5['eco3'] + up_end3, 'eco4': country5['eco4'] + up_end4}, 'Russia')
                elif wait_end['info'].find('Ispania') > 0:
                    if wait_end['reserch'] == 1:
                        reserch = 1
                    elif country6['reserch'] == 1:
                        reserch = 1
                    else:
                        reserch = 0
                    if country6['shit1']=='🛡️':
                        shit_end[0]='🛡️'
                    if country6['shit2']=='🛡️':
                        shit_end[1] = '🛡️'
                    if country6['shit3']=='🛡️':
                        shit_end[2] = '🛡️'
                    if country6['shit4']=='🛡️':
                        shit_end[3] = '🛡️'
                    Global.update({'money': money_end, 'reserch': reserch, 'roket': country6['roket']+roket_end,
                                   'shit1': shit_end[0]+country6['shit1'], 'shit2': shit_end[1]+country6['shit2'], 'shit3': shit_end[2]+country6['shit3'], 'shit4': shit_end[3]+country6['shit4'],
                                   'up1': country6['up1'] + up_end1, 'up2': country6['up2'] + up_end2,
                                   'up3': country6['up3'] + up_end3,'up4': country6['up4'] + up_end4,
                                   'eco1': country6['eco1'] + up_end1, 'eco2': country6['eco2'] + up_end2,
                                   'eco3': country6['eco3'] + up_end3, 'eco4': country6['eco4'] + up_end4}, 'Ispania')
                wait.delete(f'{end}')

        st.success('Улучшения отправлены')
        for end in range(1,len(db_content)+1):
            shit_end1,shit_end2,shit_end3,shit_end4='','','',''
            ec1, ec2, ec3, ec4 = 666, 666, 666, 666
            up1, up2, up3, up4 = 666, 666, 666, 666
            roket=0
            wait_end=wait.get(f'{end}')
            if wait_end['action']=='attak':
                if len(wait_end['Сирия'])>0:
                    chose=wait_end['Сирия']
                    shit_end1, shit_end2, shit_end3, shit_end4 = country2['shit1'], country2['shit2'], country2['shit3'], country2['shit4']
                    ec1, ec2, ec3, ec4 = country2['eco1'], country2['eco2'], country2['eco3'], country2['eco4']
                    up1, up2, up3, up4 = country2['up1'], country2['up2'], country2['up3'], country2['up4']
                    for o in range(0, len(chose)):
                        if chose[o]=='Дамаск':
                            if country2['shit1']=='🛡️':
                                ec1-=20
                                shit_end1 = ' '
                            else:
                                ec1=0
                                up1=0
                            roket+=1
                        elif chose[o]=='Хама':
                            if country2['shit2']== '🛡️':
                                ec2 -= 20
                                shit_end2 = ' '
                            else:
                                ec2 = 0
                                up2 = 0
                            roket += 1
                        elif chose[o]=='Дума':
                            if country2['shit3']== '🛡️':
                                ec3 -= 20
                                shit_end3 = ' '
                            else:
                                ec3 = 0
                                up3 = 0
                            roket += 1
                        elif chose[o]=='Ракка':
                            if country2['shit4']== '🛡️':
                                ec4 -= 20
                                shit_end4 = ' '
                            else:
                                ec4 = 0
                                up4 = 0
                            roket += 1
                    Global.update({'eco1':ec1,'up1':up1,'eco2':ec2,'up2':up2,'eco3':ec3,'up3':up3,'eco4':ec4,'up4':up4,
                                   'shit1': shit_end1, 'shit2': shit_end2, 'shit3': shit_end3, 'shit4': shit_end4},'Siria')
                if len(wait_end['Индия'])>0:
                    chose = wait_end['Индия']
                    shit_end1, shit_end2, shit_end3, shit_end4 = country1['shit1'], country1['shit2'], country1['shit3'], country1['shit4']
                    ec1, ec2, ec3, ec4 = country1['eco1'], country1['eco2'], country1['eco3'], country1['eco4']
                    up1, up2, up3, up4 = country1['up1'], country1['up2'], country1['up3'], country1['up4']
                    for o in range(0, len(chose)):
                        if chose[o] == 'Нью-Дели':
                            if country1['shit1']== '🛡️':
                                ec1 -= 20
                                shit_end1 = ' '
                            else:
                                ec1 = 0
                                up1 = 0
                            roket += 1
                        elif chose[o] == 'Бангалор':
                            if country1['shit2']== '🛡️':
                                ec2 -= 20
                                shit_end2 = ' '
                            else:
                                ec2 = 0
                                up2 = 0
                            roket += 1
                        elif chose[o] == 'Агра':
                            if country1['shit3']== '🛡️':
                                ec3 -= 20
                                shit_end3 = ' '
                            else:
                                ec3 = 0
                                up3 = 0
                            roket += 1
                        elif chose[o] == 'Сурат':
                            if country1['shit4']== '🛡️':
                                ec4 -= 20
                                shit_end4 = ' '
                            else:
                                ec4 = 0
                                up4 = 0
                            roket += 1
                    Global.update(
                    {'eco1': ec1, 'up1': up1, 'eco2': ec2, 'up2': up2, 'eco3': ec3, 'up3': up3, 'eco4': ec4, 'up4': up4,
                     'shit1': shit_end1, 'shit2': shit_end2, 'shit3': shit_end3, 'shit4': shit_end4},
                    'India')
                if len(wait_end['Канада'])>0:
                    chose = wait_end['Канада']
                    shit_end1, shit_end2, shit_end3, shit_end4 = country3['shit1'], country3['shit2'], country3['shit3'], country3['shit4']
                    ec1, ec2, ec3, ec4 = country3['eco1'], country3['eco2'], country3['eco3'], country3['eco4']
                    up1, up2, up3, up4 = country3['up1'], country3['up2'], country3['up3'], country3['up4']
                    for o in range(0, len(chose)):
                        if chose[o] == 'Оттава':
                            if country3['shit1']== '🛡️':
                                ec1 -= 20
                                shit_end1 = ' '
                            else:
                                ec1 = 0
                                up1 = 0
                            roket += 1
                        elif chose[o] == 'Торонто':
                            if country3['shit2']== '🛡️':
                                ec2 -= 20
                                shit_end2 = ' '
                            else:
                                ec2 = 0
                                up2 = 0
                            roket += 1
                        elif chose[o] == 'Ванкувер':
                            if country3['shit3']== '🛡️':
                                ec3 -= 20
                                shit_end3 = ' '
                            else:
                                ec3 = 0
                                up3 = 0
                            roket += 1
                        elif chose[o] == 'Виктория':
                            if country3['shit4']== '🛡️':
                                ec4 -= 20
                                shit_end4 = ' '
                            else:
                                ec4 = 0
                                up4 = 0
                            roket += 1
                    Global.update(
                    {'eco1': ec1, 'up1': up1, 'eco2': ec2, 'up2': up2, 'eco3': ec3, 'up3': up3,
                     'eco4': ec4, 'up4': up4, 'shit1': shit_end1, 'shit2': shit_end2, 'shit3': shit_end3, 'shit4': shit_end4},
                    'Canada')
                if len(wait_end['Швеция'])>0:
                    chose = wait_end['Швеция']
                    shit_end1, shit_end2, shit_end3, shit_end4 = country4['shit1'], country4['shit2'], country4['shit3'], country4['shit4']
                    ec1, ec2, ec3, ec4 = country4['eco1'], country4['eco2'], country4['eco3'], country4['eco4']
                    up1, up2, up3, up4 = country4['up1'], country4['up2'], country4['up3'], country4['up4']
                    for o in range(0, len(chose)):
                        if chose[o] == 'Стокгольм':
                            if country4['shit1']== '🛡️':
                                ec1 -= 20
                                shit_end1 = ' '
                            else:
                                ec1 = 0
                                up1 = 0
                            roket += 1
                        elif chose[o] == 'Мальмё':
                            if country4['shit2']== '🛡️':
                                ec2 -= 20
                                shit_end2 = ' '
                            else:
                                ec2 = 0
                                up2 = 0
                            roket += 1
                        elif chose[o] == 'Кируна':
                            if country4['shit3']== '🛡️':
                                ec3 -= 20
                                shit_end3 = ' '
                            else:
                                ec3 = 0
                                up3 = 0
                            roket += 1
                        elif chose[o] == 'Сигнута':
                            if country4['shit4']== '🛡️':
                                ec4 -= 20
                                shit_end4 = ' '
                            else:
                                ec4 = 0
                                up4 = 0
                            roket += 1
                    Global.update(
                    {'eco1': ec1, 'up1': up1, 'eco2': ec2, 'up2': up2, 'eco3': ec3, 'up3': up3,
                     'eco4': ec4, 'up4': up4,'shit1': shit_end1, 'shit2': shit_end2, 'shit3': shit_end3, 'shit4': shit_end4},
                    'Shvechia')
                if len(wait_end['Россия'])>0:
                    chose = wait_end['Россия']
                    shit_end1, shit_end2, shit_end3, shit_end4 = country5['shit1'], country5['shit2'], country5['shit3'], country5['shit4']
                    ec1, ec2, ec3, ec4 = country5['eco1'], country5['eco2'], country5['eco3'], country5['eco4']
                    up1, up2, up3, up4 = country5['up1'], country5['up2'], country5['up3'], country5['up4']
                    for o in range(0,len(chose)):
                        if chose[o] == 'Москва':
                            if country5['shit1']== '🛡️':
                                ec1 -= 20
                                shit_end1=' '
                            else:
                                ec1 = 0
                                up1 = 0
                            roket += 1
                        elif chose[o] == 'Санкт-Петербург':
                            if country5['shit2']== '🛡️':
                                ec2 -= 20
                                shit_end2=' '
                            else:
                                ec2 = 0
                                up2 = 0
                            roket += 1
                        elif chose[o] == 'Екатеринбург':
                            if country5['shit3']== '🛡️':
                                ec3 -= 20
                                shit_end3=' '
                            else:
                                ec3 = 0
                                up3 = 0
                            roket += 1
                        elif chose[o] == 'Магадан':
                            if country5['shit4']== '🛡️':
                                ec4 -= 20
                                shit_end4=' '
                            else:
                                ec4 = 0
                                up4 = 0
                            roket += 1
                    Global.update(
                    {'eco1': ec1, 'up1': up1, 'eco2': ec2, 'up2': up2, 'eco3': ec3, 'up3': up3, 'eco4': ec4, 'up4': up4,'shit1':shit_end1,'shit2':shit_end2,'shit3':shit_end3,'shit4':shit_end4},
                    'Russia')
                if len(wait_end['Испания'])>0:
                    chose = wait_end['Испания']
                    shit_end1, shit_end2, shit_end3, shit_end4 = country5['shit1'], country5['shit2'], country5['shit3'], country5['shit4']
                    ec1, ec2, ec3, ec4 = country6['eco1'], country6['eco2'], country6['eco3'], country6['eco4']
                    up1, up2, up3, up4 = country6['up1'], country6['up2'], country6['up3'], country6['up4']
                    for o in range(0, len(chose)):
                        if chose[o] == 'Мадрид':
                            if country6['shit1']== '🛡️':
                                ec1 -= 20
                                shit_end1 = ' '
                            else:
                                ec1 = 0
                                up1 = 0
                            roket += 1
                        elif chose[o] == 'Барселона':
                            if country6['shit2']== '🛡️':
                                ec2 -= 20
                                shit_end1 = ' '
                            else:
                                ec2 = 0
                                up2 = 0
                            roket += 1
                        elif chose[o] == 'Пальма':
                            if country6['shit3']== '🛡️':
                                ec3 -= 20
                                shit_end1 = ' '
                            else:
                                ec3 = 0
                                up3 = 0
                            roket += 1
                        elif chose[o] == 'Гранда':
                            if country6['shit4']== '🛡️':
                                ec4 -= 20
                                shit_end1 = ' '
                            else:
                                ec4 = 0
                                up4 = 0
                            roket += 1
                    Global.update(
                    {'eco1': ec1, 'up1': up1, 'eco2': ec2, 'up2': up2, 'eco3': ec3, 'up3': up3,
                     'eco4': ec4, 'up4': up4, 'shit1': shit_end1, 'shit2': shit_end2, 'shit3': shit_end3, 'shit4': shit_end4},
                    'Ispania')
            if wait_end['info'].find('India')>0:
                roket=country1['roket']-roket
                Global.update({'roket':roket},'India')
            elif wait_end['info'].find('Siria')>0:
                roket=country2['roket']-roket
                Global.update({'roket':roket},'Siria')
            elif wait_end['info'].find('Canada')>0:
                roket=country3['roket']-roket
                Global.update({'roket':roket},'Canada')
            elif wait_end['info'].find('Shvechia')>0:
                roket=country4['roket']-roket
                Global.update({'roket':roket},'Shvechia')
            elif wait_end['info'].find('Russia')>0:
                roket=country5['roket']-roket
                Global.update({'roket':roket},'Russia')
            elif wait_end['info'].find('Ispania')>0:
                roket=country6['roket']-roket
                Global.update({'roket':roket},'Ispania')
            wait.delete(f'{end}')
        st.success('Ракеты запущенны')
if menu=='Посещения':
    st.info('Запросы на посещения')
    db_content = request.fetch().items
    for slash in range(0, len(db_content)):
        st.write(db_content[slash])
        if st.button(f'Удалить запрос{slash}'):
            forgot=db_content[slash]['key']
            slash+=1
            request.delete(f'{forgot}')
    
if menu=='Перевод':
    st.info('Перевод денег')
    db_content = request_money.fetch().items
    for slash in range(0, len(db_content)):
        st.write(db_content[slash])
        if st.button('Принять преревод'):
            slash+=1
            give_money=request_money.get(f'{slash}')
            money_from=country1['money']-give_money['price']
            hihi=give_money['from']
            if give_money['come']=='Швеция':
                money_who=country4['money']+give_money['price']
                Global.update({'money':money_from},f'{hihi}')
                Global.update({'money':money_who},'Shvechia')
            elif give_money['come'] == 'Канада':
                money_who = country3['money'] + give_money['price']
                Global.update({'money': money_from}, f'{hihi}')
                Global.update({'money': money_who}, 'Canada')
            elif give_money['come'] == 'Сирия':
                money_who = country2['money'] + give_money['price']
                Global.update({'money': money_from}, f'{hihi}')
                Global.update({'money': money_who}, 'Siria')
            elif give_money['come'] == 'Филиппинские острова':
                money_who = country6['money'] + give_money['price']
                Global.update({'money': money_from}, f'{hihi}')
                Global.update({'money': money_who}, 'Ispania')
            elif give_money['come'] == 'Россия':
                money_who = country5['money']+give_money['price']
                Global.update({'money': money_from}, f'{hihi}')
                Global.update({'money': money_who}, 'Russia')
            elif give_money['come']=='Индия':
                money_who=country1['money']+give_money['price']
                Global.update({'money': money_from}, f'{hihi}')
                Global.update({'money': money_who}, 'India')



if menu=='Логи':
    st.info('Логи')
    db_content = log.fetch().items
    for slash in range(0, len(db_content)):
        st.write(db_content[slash])





if Country_Name!='vjcrdf11' and Country_Name!='':
    menu = st.sidebar.selectbox('Меню', ('Стартовая страница', 'Улучшения', 'Запуск ракет', 'Посещения', 'Гуманитарная помощь', 'INFO'))
    if pp['Atention'] != '':
        st.sidebar.error(pp['Atention'], icon="🚨")
    if city['sms'] != '':
        st.sidebar.warning(city['sms'],icon="⚠️")
    st.sidebar.caption('Автор MangoVirus')

    masiv_home=['j',"j",'h',"h",'h']
    masiv_up = [0, 0, 0, 0]
    masiv_shit = [' ', ' ', ' ', ' ']
    attak = []
    attak1 = []
    attak2 = []
    attak3 = []
    attak4 = []
    attak5 = []
    cost_up_city=200
    cost_shit=350
    for i_home in range(1,5):
        if city[f'eco{i_home}']<1:
            masiv_home[i_home]='🏚️'
        else:
            masiv_home[i_home]='🏡'

    if menu == 'INFO':
        info()

    if menu == 'Гуманитарная помощь':
        st.write('Деньги:', money)
        visit_money = st.selectbox('Кому вы хотите перевести деньги?',('Россия','Индия', 'Канада', 'Сирия', 'Швеция', 'Испания'))
        if visit_money!=test_name:
            how_money = st.number_input('Сумма перевода?',0)
        else:
            st.error('Нельзя переводить деньги самому себе!',icon='🛑')
        if lid==1:
            if st.button('Перевести'):
                nowtime = str(current_datetime.hour) + ':' + str(current_datetime.minute) + ':' + str(current_datetime.second) + ' '
                request_money_content=request_money.fetch().items
                keys=len(request_money_content)+1
                request_money.put({'key': f'{keys}','info':f'{nowtime}','from':f'{Country_Name}','come': visit_money, 'price': how_money})
                st.success('Запрос на перевод отправлен.(Деньги придут в течение 5 минут)')


    if menu == 'Посещения':
        visit = st.selectbox('Какую старану вы хотите посетить?', ('Россия','Индия', 'Канада', 'Сирия', 'Швеция', 'Испания'))
        if visit!=test_name:
            if lid==1:
                if st.button('Отправить запрос'):
                    nowtime = str(current_datetime.hour) + ':' + str(current_datetime.minute) + ':' + str(current_datetime.second) + ' '
                    request_content=request.fetch().items
                    keys=str(request_content[str(len(request_content)-1)]['key']+1)
                    request.put({'key':f'{keys}','info': f'{nowtime}{Country_Name}','come': visit})
                    st.success('Запрос на посещение отправлен')
        else:
            st.error('И как ты собрался себя посетить?',icon='🛑')


    if menu == 'Запуск ракет':
        final_roket = -1999
        friendly_fire=0
        if city['reserch'] == '0':
            st.error('Дружок ты еще не изучил ракеты')
        else:
            st.write('Количество ваших ракет:', city['roket'])
            country = st.multiselect('Какие страны атакуем?', ['Индию', 'Канаду', 'Сирию', 'Швецию', 'Испанию','Россию'])
            for l in range(0, len(country)):
                if country[l]==title_name:
                    st.error('Ты точно уверене, что хочешь сам в себя стрелять?',icon='🛑')
                    friendly_fire+=1
                if country[l] == 'Индию' and friendly_fire==0:
                    attak = st.multiselect('Какие города атакуем в Индии?', ['Нью-Дели', 'Бангалор', 'Агра', 'Сурат'])
                if country[l] == 'Канаду' and friendly_fire==0:
                    attak1 = st.multiselect('Какие города атакуем в Канаде?', ['Оттава', 'Торонто', 'Ванкувер', 'Виктория'])
                if country[l] == 'Сирию' and friendly_fire==0:
                    attak2 = st.multiselect('Какие города атакуем в Сирии?', ['Дамаск', 'Хама', 'Дума', 'Ракка'])
                if country[l] == 'Швецию' and friendly_fire==0:
                    attak3 = st.multiselect('Какие города атакуем в Швеция?', ['Стокгольм', 'Мальмё', 'Кируна', 'Сигнута'])
                if country[l] == 'Испанию' and friendly_fire==0:
                    attak4 = st.multiselect('Какие города атакуем в Испания?', ['Мадрид', 'Барселона', 'Пальма', 'Гранда'])
                if country[l] == 'Россию' and friendly_fire==0:
                    attak5=st.multiselect('Какие города атакуем в Россия?',['Москва','Санкт-Петербург','Екатеринбург','Магадан'])
                final_roket = city['roket'] - (len(attak) + len(attak1) + len(attak2) + len(attak3) + len(attak4)+len(attak5))
                st.write('У вас останеться ракет:', final_roket)

            if lid==1:
                if st.button('Отправить данные'):
                    if final_roket >= 0:
                        for ll in range(0, 6):
                            if len(country) < 6:
                                count = 6 - len(country)
                                for lll in range(0, count):
                                    country.append(' ')
                        nowtime = str(current_datetime.hour) + ':' + str(current_datetime.minute) + ':' + str(current_datetime.second) + ' '
                        Attak_content=Attak.fetch().items
                        keys=len(Attak_content)+1
                        Attak.put({'key':f'{keys}','info': f'{nowtime}{Country_Name}', 'Индия': attak, 'Канада': attak1,'Сирия': attak2, 'Швеция': attak3,
                                   'Испания': attak4,'Россия':attak5,'final_roket':final_roket})
                        log_content=log.fetch().items
                        keys1=len(log_content)+1
                        log.put({'key':f'{keys1}','info': f'{nowtime}{Country_Name}','operation':'attak', 'Индия':  attak, 'Канада': attak1,'Сирия': attak2, 'Швеция': attak3,
                                   'Испания': attak4,'Россия':attak5,'final_roket':final_roket})
                        with st.spinner('Wait for it...'):
                            time.sleep(1)
                            st.success('Данные обновлены!')
                    elif final_roket == -1999:
                        st.error('Дружок не надо мне засарять базу данных...')
                    else:
                        st.error('Вы выпустили больше ракет чем у вас есть...')


    if menu == 'Улучшения':
        count_up=0
        number = 0
        reserch1 = 0
        st.write('Деньги:', money)
        st.write('Какие города вы хотите улучшить?')
        st.caption('Можно улучшить только 4 города за раунд')
        if count_up<4 and city['eco1']>0:
            up = st.checkbox(f'{city_1}')
            if up:
                masiv_up[0] += 10
                money -= cost_up_city
                count_up += 1
                if count_up<4:
                    x = st.checkbox(f'Улучшить {city_1} 2 раза?')
                    if x:
                        masiv_up[0] += 10
                        money -= cost_up_city
                        count_up += 1
        if count_up<4 and city['eco2']>0:
            up1 = st.checkbox(f'{city_2}')
            if up1:
                masiv_up[1] += 10
                money -= cost_up_city
                count_up+=1
                if count_up<4:
                    x1 = st.checkbox(f'Улучшить {city_2} 2 раза?')
                    if x1:
                        masiv_up[1] += 10
                        money -= cost_up_city
                        count_up+=1
        if count_up<4 and city['eco3']>0:
            up2 = st.checkbox(f'{city_3}')
            if up2:
                masiv_up[2] += 10
                money -= cost_up_city
                count_up+=1
                if count_up<4:
                    x2 = st.checkbox(f'Улучшить {city_3} 2 раза?')
                    if x2:
                        masiv_up[2] += 10
                        money -= cost_up_city
                        count_up+=1
        if count_up<4 and city['eco4']>0:
            up3 = st.checkbox(f'{city_4}')
            if up3:
                masiv_up[3] += 10
                money -= cost_up_city
                count_up+=1
                if count_up<4:
                    x3 = st.checkbox(f'Улучшить {city_4} 2 раза?')
                    if x3:
                        masiv_up[3] += 10
                        money -= cost_up_city
                        count_up+=1

        st.write('На какие города установим щиты?')
        shit = st.checkbox(f'{city_1}  ')
        if shit:
            if city['shit1'] == '🛡️':
                st.error('Дружок, у нас так не принято. По 1 щиту на город...')
            elif city['eco1']<1:
                st.error('Этот город разрушен')
            else:
                masiv_shit[0] = '🛡️'
                money -= cost_shit
        shit1 = st.checkbox(f'{city_2} ')
        if shit1:
            if city['shit2'] == '🛡️':
                st.error('Дружок, у нас так не принято. По 1 щиту на город...')
            elif city['eco2']<1:
                st.error('Этот город разрушен')
            else:
                masiv_shit[1] = '🛡️️'
                money -= cost_shit
        shit2 = st.checkbox(f'{city_3} ')
        if shit2:
            if city['shit3'] == '🛡️':
                st.error('Дружок, у нас так не принято. По 1 щиту на город...')
            elif city['eco3']<1:
                st.error('Этот город разрушен')
            else:
                masiv_shit[2] = '🛡️'
                money -= cost_shit
        shit3 = st.checkbox(f'{city_4} ')
        if shit3:
            if city['shit4'] == '🛡️':
                st.error('Дружок, у нас так не принято. По 1 щиту на город...')
            elif city['eco4']<1:
                st.error('Этот город разрушен')
                #11
            else:
                masiv_shit[3] = '🛡️'
                money -= cost_shit
        if city['reserch'] == 1:
            number = st.number_input('Сколько ракет делаем?', 0)
            st.write('Вы получите в следующие количество ракет', number)
            money -= 500 * number
        else:
            st.write(' ')
            reserch = st.checkbox('Изучить ядерные ракеты')
            st.write(' ')
            if reserch:
                money -= 500
                reserch1 = 1

        sunks_for_who = st.multiselect('На какие страны вы хотите наложить санкции?',['Индия', 'Канада', 'Сирия', 'Швеция', 'Испания'])
        money -= 50 * len(sunks_for_who)

        st.write('Ваш баланс после операции:', money)
        col1, col2, col3, col4= st.columns(4)
        col1.metric(masiv_home[1] + city['shit1'] + masiv_shit[0] + f'{city_1}','⚙️' + str(city['up1']+masiv_up[0]) + '%' + ' 🌳 ' + str(city['eco1']+masiv_up[0]) + '%', masiv_up[0])
        col2.metric(masiv_home[2] + city['shit2'] + masiv_shit[1] + f'{city_2}','⚙️' + str(city['up2']+masiv_up[1]) + '%' + ' 🌳 ' + str(city['eco2']+masiv_up[1]) + '%', masiv_up[1])
        col3.metric(masiv_home[3] + city['shit3'] + masiv_shit[2] + f'{city_3}','⚙️' + str(city['up3']+masiv_up[2]) + '%' + ' 🌳 ' + str(city['eco3']+masiv_up[2]) + '%', masiv_up[2])
        col4.metric(masiv_home[4] + city['shit4'] + masiv_shit[3] + f'{city_4}','⚙️' + str(city['up4']+masiv_up[3]) + '%' + ' 🌳 ' + str(city['eco4']+masiv_up[3]) + '%', masiv_up[3])

        if lid==1:
            if st.button('Отправить данные'):
                if money >= 0:
                    nowtime=str(current_datetime.hour)+':'+str(current_datetime.minute)+':'+str(current_datetime.second)+' '
                    db_content=db.fetch().items
                    keys=len(db_content)+1
                    db.put({'key':f'{keys}','info': f'{nowtime}{Country_Name}', "money": money, "roket": number, "shit": masiv_shit, "up": masiv_up,'sunks_for_who': str(sunks_for_who), 'reserch': reserch1})
                    log_content=log.fetch().items
                    keys1=len(log_content)+1
                    log.put({'key':f'{keys1}','info': f'{nowtime}{Country_Name}', 'operation':'upgrade',"money": money, "roket": number, "shit": masiv_shit, "up": masiv_up,'sunks_for_who': str(sunks_for_who), 'reserch': reserch1})
                    with st.spinner('Wait for it...'):
                        time.sleep(1)
                        st.success('Данные обновлены!')
                else:
                    st.error('Вы потратили больше денег чем у вас есть...')


    if menu == 'Стартовая страница':
        st.title(f'Вы играете за {title_name}')
        st.write('Деньги:', money)
        st.write('Ракеты:', city['roket'])
        st.write('Санкции наложеные вами:', city['sunks_of_you'])
        st.write('Санкции наложеные на вас:', city['sunks_for_you'])
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(masiv_home[1] + city['shit1'] + f'{city_1}', '⚙️' + str(city['up1']) + '%' + ' 🌳 ' + str(city['eco1']) + '%')
        col2.metric(masiv_home[2] + city['shit2'] + f'{city_2}', '⚙️' + str(city['up2']) + '%' + ' 🌳 ' + str(city['eco2']) + '%')
        col3.metric(masiv_home[3] + city['shit3'] + f'{city_3}', '⚙️' + str(city['up3']) + '%' + ' 🌳 ' + str(city['eco3']) + '%')
        col4.metric(masiv_home[4] + city['shit4'] + f'{city_4}', '⚙️' + str(city['up4']) + '%' + ' 🌳 ' + str(city['eco4']) + '%')
        sr_country1=((country1['eco1']+country1['eco2']+country1['eco3']+country1['eco4'])/4) - (country1['roket']/2)
        sr_country2=((country2['eco1'] + country2['eco2'] + country2['eco3'] + country2['eco4']) / 4)  - (country2['roket']/2)
        sr_country3=((country3['eco1'] + country3['eco2'] + country3['eco3'] + country3['eco4']) / 4) - (country3['roket']/2)
        sr_country6=((country6['eco1'] + country6['eco2'] + country6['eco3'] + country6['eco4']) / 4) - (country4['roket']/2)
        sr_country4=((country4['eco1'] + country4['eco2'] + country4['eco3'] + country4['eco4']) / 4) - (country5['roket']/2)
        sr_country5=((country5['eco1'] + country5['eco2'] + country5['eco3'] + country5['eco4']) / 4) - (country6['roket']/2)
        df=pd.DataFrame(
            [
                {'Страна':'Индия',
                 'Первый город':'⚙️' + str(country1['up1']) + '%' + ' 🌳 ' + str(country1['eco1']) + '%',
                 'Второй город':'⚙️' + str(country1['up2']) + '%' + ' 🌳 '+ str(country1['eco2']) + '%',
                 'Третий город':'⚙️' + str(country1['up3']) + '%' + ' 🌳 ' + str(country1['eco3']) + '%',
                 'Четвертый город':'⚙️' + str(country1['up3']) + '%' + ' 🌳 ' + str(country1['eco4']) + '%',
                 'Средний уровень жизни': sr_country1},
                {'Страна': 'Сирия',
                 'Первый город': '⚙️' + str(country2['up1']) + '%' + ' 🌳 ' + str(country2['eco1']) + '%',
                 'Второй город': '⚙️' + str(country2['up2']) + '%' + ' 🌳 ' + str(country2['eco2']) + '%',
                 'Третий город': '⚙️' + str(country2['up3']) + '%' + ' 🌳 ' + str(country2['eco3']) + '%',
                 'Четвертый город': '⚙️' + str(country2['up3']) + '%' + ' 🌳 ' + str(country2['eco4']) + '%',
                 'Средний уровень жизни': sr_country2},
                {'Страна': 'Канада',
                 'Первый город': '⚙️' + str(country3['up1']) + '%' + ' 🌳 ' + str(country3['eco1']) + '%',
                 'Второй город': '⚙️' + str(country3['up2']) + '%' + ' 🌳 ' + str(country3['eco2']) + '%',
                 'Третий город': '⚙️' + str(country3['up3']) + '%' + ' 🌳 ' + str(country3['eco3']) + '%',
                 'Четвертый город': '⚙️' + str(country3['up3']) + '%' + ' 🌳 ' + str(country3['eco4']) + '%',
                 'Средний уровень жизни': sr_country3},
                {'Страна': 'Испания',
                 'Первый город': '⚙️' + str(country6['up1']) + '%' + ' 🌳 ' + str(country6['eco1']) + '%',
                 'Второй город': '⚙️' + str(country6['up2']) + '%' + ' 🌳 ' + str(country6['eco2']) + '%',
                 'Третий город': '⚙️' + str(country6['up3']) + '%' + ' 🌳 ' + str(country6['eco3']) + '%',
                 'Четвертый город': '⚙️' + str(country6['up3']) + '%' + ' 🌳 ' + str(country6['eco4']) + '%',
                 'Средний уровень жизни': sr_country6},
                {'Страна': 'Швеция',
                 'Первый город': '⚙️' + str(country4['up1']) + '%' + ' 🌳 ' + str(country4['eco1']) + '%',
                 'Второй город': '⚙️' + str(country4['up2']) + '%' + ' 🌳 ' + str(country4['eco2']) + '%',
                 'Третий город': '⚙️' + str(country4['up3']) + '%' + ' 🌳 ' + str(country4['eco3']) + '%',
                 'Четвертый город': '⚙️' + str(country4['up3']) + '%' + ' 🌳 ' + str(country4['eco4']) + '%',
                 'Средний уровень жизни': sr_country4},
                {'Страна': 'Россия',
                 'Первый город': '⚙️' + str(country5['up1']) + '%' + ' 🌳 ' + str(country5['eco1']) + '%',
                 'Второй город': '⚙️' + str(country5['up2']) + '%' + ' 🌳 ' + str(country5['eco2']) + '%',
                 'Третий город': '⚙️' + str(country5['up3']) + '%' + ' 🌳 ' + str(country5['eco3']) + '%',
                 'Четвертый город': '⚙️' + str(country5['up3']) + '%' + ' 🌳 ' + str(country5['eco4']) + '%',
                 'Средний уровень жизни': sr_country5}
            ]
        )
        st.table(df)
        st.write('Средняя экология планеты',((sr_country1+sr_country2+sr_country3+sr_country6+sr_country4+sr_country5)/6))
        df_chart=pd.DataFrame([
            {'Индия':sr_country1},
            {'Сирия':sr_country2},
            {'Канада': sr_country3},
            {'Испания': sr_country6},
            {'Швеция': sr_country4},
            {'Россия': sr_country5}
        ])
        st.bar_chart(df_chart)
