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


#сделать city['up1']-хранилищем информации о шестеренке
#также сделать с city['eco']-хранилище для экологии

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

with st.sidebar.container():
    col1, col2, col3, col4= st.columns(4)

    with col2:
        st.image('https://cdn.discordapp.com/attachments/890188503047077928/1070451124869533758/066443762463369c.png', width=128)

Country_Name=""
menu=''
ok=0
lid=0
com=0
Country_Name = st.sidebar.text_input('Введите ключ','')
if Country_Name!='':
    com+=1
if com==0:
    st.title('Добро пожаловать в Мировое Господство!')
    st.error('Нет ключа',icon='‼️')
    st.info('Чтобы начать играть введите ключ, который вам дал представитель ООН',icon='ℹ️')
    st.info('Чтобы ввести ключ нажмите на стрелочку слева сверху',icon='ℹ️')

    code='''Правила игры
    1. Запрещены все угрозы в реальной жизни. Пример: 'Если ты не скинешь мне косарь, я с тобой перестану общаться!!!'
    2. Запрещается предвзятое отношение к другим странам: 'По названию страны, по полу игроков, к конкретным людям.'
    3. Не давайте свои ключи другим людям. 'Ключ президента должен быть только у президента!'
    4. Перед тем как отправить запрос хорошо подумайте. 'Не надо спамить запросами.' Иначе они будут отказаны
    '''
    st.code(code, language='python')
if Country_Name.find('-lid')>0:
    Country_Name=Country_Name.replace('-lid','')
    lid=1
if Country_Name == 'Australia':
    title_name='Австралию'
    city_1 = 'Буэнос-Айрес'
    city_2 = 'Сальта'
    city_3 = 'Кордова'
    city_4 = 'Мендоса'
elif Country_Name == 'Mexica':
    title_name='Мексику'
    city_1 = 'Мехико'
    city_2 = 'Канкун'
    city_3 = 'Мерида'
    city_4 = 'Таско'
elif Country_Name == "Canada":
    title_name = 'Канаду'
    city_1 = 'Оттава'
    city_2 = 'Торонто'
    city_3 = 'Канкувер'
    city_4 = 'Квебей'
elif Country_Name == 'Filipin':
    title_name='Филипинские острова'
    city_1 = 'Лусон'
    city_2 = 'Боракай'
    city_3 = 'Себу'
    city_4 = 'Панай'
elif Country_Name == 'Shvechia':
    title_name='Швецию'
    city_1 = 'Стокгольм'
    city_2 = 'Вестерсон'
    city_3 = 'Висбю'
    city_4 = 'Евле'
elif Country_Name == 'Argentina':
    title_name='Аргентину'
    city_1 = 'Буэнос-Айрес'
    city_2 = 'Сальта'
    city_3 = 'Кордова'
    city_4 = 'Мендоса'
elif Country_Name=='vjcrdf11':
    menu=st.sidebar.selectbox('Меню',('Запросы на улучшение','Запросы на запуск ракет','Принятые запросы','Деньги','Логи'))

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
mex = Global.get('Mexica')
au = Global.get('Australia')
ca = Global.get('Canada')
sh = Global.get('Shvechia')
ar = Global.get('Argentina')
ph = Global.get('Filipin')
if menu=='Деньги':
    give1=(mex['up1']+mex['up2']+mex['up3']+mex['up4'])*5
    st.success(f'ЗП для Мексики {give1}',icon='🤑')
    give2=(au['up1']+au['up2']+au['up3']+au['up4'])*5
    st.success(f'ЗП для Австралии {give2}',icon='🤑')
    give3=(ca['up1']+ca['up2']+ca['up3']+ca['up4'])*5
    st.success(f'ЗП для Канады {give3}',icon='🤑')
    give4=(sh['up1']+sh['up2']+sh['up3']+sh['up4'])*5
    st.success(f'ЗП для Швеции {give4}',icon='🤑')
    give5=(ar['up1']+ar['up2']+ar['up3']+ar['up4'])*5
    st.success(f'ЗП для Аргентины {give5}',icon='🤑')
    give6=(ph['up1']+ph['up2']+ph['up3']+ph['up4'])*5
    st.success(f'ЗП для Филиппин {give6}',icon='🤑')
    if st.button('Выдать деньги'):
        give1=int(mex['money'])+give1
        Global.update({"money": f"{give1}"}, "Mexica")
        give2 = int(au['money']) + give2
        Global.update({"money": f"{give2}"}, "Australia")
        give3 = int(ca['money']) + give3
        Global.update({"money": f"{give3}"}, "Canada")
        give4 = int(sh['money']) + give4
        Global.update({"money": f"{give4}"}, "Shvechia")
        give5 = int(ar['money']) + give5
        Global.update({"money": f"{give5}"}, "Argentina")
        give6 = int(ph['money']) + give6
        Global.update({"money": f"{give6}"}, "Filipin")
        st.success('Деньги успешно выданы!', icon='💰')
if menu == 'Запросы на улучшение':
    st.info('Запросы на улучшение')
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
            wait.put({'key':f'{keys}','info':f'{take_info}','money':f'{take_money}','reserch':f'{take_reserch}','roket':f'{take_roket}','shit':f'{take_shit}',
                      'sunks_for_who':f'{take_sunks_for_who}','up':f'{take_up}','action':'up'})
            db.delete(f'{slash}')
            st.success('Улучшение принято')
        if st.button(f'Отклонить улучшение {slash}'):
            slash+=1
            db.delete(f'{slash}')
            st.error('Улучшение удалено')
if menu=='Запросы на запуск ракет':
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
            take_country1=take['Австралия']
            take_country2 =take['Аргентина']
            take_country3 =take['Канада']
            take_country4 =take['Мексика']
            take_country5 =take['Филипинские острова']
            take_country6 =take['Швеция']
            wait.put({'key': f'{keys}', 'info': f'{take_info}', 'Австралия': f'{take_country1}', 'Аргентина': f'{take_country2}',
                      'Канада': f'{take_country3}', 'Мексика': f'{take_country4}',
                      'Филипинские острова': f'{take_country5}', 'Швеция': f'{take_country6}', 'action':'attak'})
            Attak.delete(f'{slash}')
            st.success('Запуск принято')
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
            wait.get(f'{end}')
            if wait['action']=='attak' and wait['key']>1:
                key=wait['key']-1
                wait.update({'key':f'{key}'})
            elif wait['action']=='up':
                wait.get(f'{end}')
                money_end = wait['money']
                roket_end=wait['roket']
                shit_end=wait['shit']
                sunks_for_who_end=wait['sunks_for_who']
                up_end=wait['up']
                if wait['info'].find('Argentina')>0:
                    if wait['reserch'] == 1:
                        reserch = 1
                    elif ar['reserch'] == 1:
                        reserch = 1
                    else:
                        reserch = 0
                    Global.update({'money': f'{money_end}', 'reserch': f'{reserch}', 'roket': f'{roket_end}',
                                       'shit': f'{shit_end}', 'sunks_for_who': f'{sunks_for_who_end}',
                                       'up': f'{up_end}'}, 'Argentina')
                elif wait['info'].find('Mexica')>0:
                    if wait['reserch'] == 1:
                        reserch = 1
                    elif mex['reserch'] == 1:
                        reserch = 1
                    else:
                        reserch = 0
                    Global.update({'money': f'{money_end}', 'reserch': f'{reserch}', 'roket': f'{roket_end}',
                                       'shit': f'{shit_end}', 'sunks_for_who': f'{sunks_for_who_end}',
                                       'up': f'{up_end}'}, 'Mexica')#Добавить остальные страны
            wait.delete(f'{end}')
        for end in range(0,len(db_content)):
            wait.get(f'{end}')
            if wait['action']=='attak':
                if len(wait['Австралия'])>0:
                    chose=wait['Австралия']
                    shit_try=au['shit']
                    for chek in range(0,len(chose)):
                        if chose[chek]=='Кенберра':
                            if shit_try[1]==' 🛡️':
                                Global.
            else:
                pass

if menu=='Логи':
    st.info('Логи')
    db_content = log.fetch().items
    for slash in range(0, len(db_content)):
        st.write(db_content[slash])





if Country_Name!='vjcrdf11' and Country_Name!='':
    menu = st.sidebar.selectbox('Меню', ('Стартовая страница', 'Улучшения', 'Запуск ракет', 'Посещения', 'Гуманитарная помощь', 'Авторы'))
    if pp['Atention'] != '':
        st.sidebar.error(pp['Atention'], icon="🔥")
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
            masiv_home[i_home]='🏠'

    if menu == 'Авторы':
        '''# Над данным проектом работали'''
        st.subheader('MangoVirus')
        '''Разработчик сайта, создатель DataBase.'''
        st.subheader('Турба')
        '''Проектный руководитель, дизайнер.'''
        st.subheader(
            'Если вы хотите поддержать нас и в будущем видеть более маштабные нововедения вы можете скинуть нам пару тугриков по номеру телефона 8 (977) 382-41-17')
        '''Если вам нужна помощь по сайту или вы нашли баг, можете нажать на 3 полосочки справа и Get Help или Report Bug'''


    if menu == 'Гуманитарная помощь':
        st.write('Деньги:', money)
        visit_money = st.selectbox('Кому вы хотите перевести деньги?',('Мексике', 'Канаде', 'Австралия', 'Швеции', 'Филипинские острова'))
        how_money = st.number_input('Сумма перевода?',0)
        if lid==1:
            if st.button('Перевести'):
                nowtime = str(current_datetime.hour) + ':' + str(current_datetime.minute) + ':' + str(current_datetime.second) + ' '
                request_money_content=request_money.fetch().items
                keys=len(request_money_content)+1
                request_money.put({'key': f'{keys}','info':f'{nowtime}{Country_Name}','come': visit_money, 'price': how_money})
                st.success('Запрос на перевод отправлен.(Деньги придут в течение 5 минут)')


    if menu == 'Посещения':
        visit = st.selectbox('Какую старану вы хотите посетить?', ('Мексика', 'Канада', 'Австралия', 'Швеция', 'Филипинские острова'))
        if lid==1:
            if st.button('Отправить запрос'):
                nowtime = str(current_datetime.hour) + ':' + str(current_datetime.minute) + ':' + str(current_datetime.second) + ' '
                request_content=request.fetch().items
                keys=len(request_content)+1
                request.put({'key':f'{keys}','info': f'{nowtime}{Country_Name}','come': visit})
                st.success('Запрос на посещение отправлен')


    if menu == 'Запуск ракет':
        final_roket = -1999
        friendly_fire=0
        if city['reserch'] == '0':
            st.error('Дружок ты еще не изучил ракеты')
        else:
            st.write('Количество ваших ракет:', city['roket'])
            country = st.multiselect('Какие страны атакуем?', ['Мексику', 'Канаду', 'Австралию', 'Швецию', 'Филипинские острова','Аргентину'])
            for l in range(0, len(country)):
                if country[l]==title_name:
                    st.error('Ты точно уверене, что хочешь сам в себя стрелять?',icon='🛑')
                    friendly_fire+=1
                if country[l] == 'Мексику' and friendly_fire==0:
                    attak = st.multiselect('Какие города атакуем в Максика?', ['Мехико', 'Канкун', 'Мерида', 'Таско'])
                if country[l] == 'Канаду' and friendly_fire==0:
                    attak1 = st.multiselect('Какие города атакуем в Канада?', ['Оттава', 'Торонто', 'Ванкувер', 'Квебек'])
                if country[l] == 'Австралию' and friendly_fire==0:
                    attak2 = st.multiselect('Какие города атакуем в Австралия?', ['Кенберра', 'Сидней', 'Мельбрун', 'Перт'])
                if country[l] == 'Швецию' and friendly_fire==0:
                    attak3 = st.multiselect('Какие города атакуем в Швеция?', ['Стокгольм', 'Вестерсон', 'Висбю', 'Евле'])
                if country[l] == 'Филипинские острова' and friendly_fire==0:
                    attak4 = st.multiselect('Какие города атакуем в Филипинские острова?', ['Лусон', 'Боракай', 'Себу', 'Панай'])
                if country[l] == 'Аргентину' and friendly_fire==0:
                    attak5=st.multiselect('Какие города атакуем в Аргентине?',['Буэнос-Айрес','Сальта','Кордова','Мендоса'])
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
                        Attak.put({'key':f'{keys}','info': f'{nowtime}{Country_Name}', 'Мексика': str(attak), 'Канада': str(attak1),'Австралия': str(attak2), 'Швеция': str(attak3),
                                   'Филипинские острова': str(attak4),'Аргентина':str(attak5),'final_roket':final_roket})
                        log_content=log.fetch().items
                        keys1=len(log_content)+1
                        log.put({'key':f'{keys1}','info': f'{nowtime}{Country_Name}','operation':'attak', 'Мексика':  str(attak), 'Канада': str(attak1),'Австралия': str(attak2), 'Швеция': str(attak3),
                                   'Филипинские острова': str(attak4),'Аргентина':str(attak5),'final_roket':final_roket})
                        db_content = Attak.fetch().items
                        st.write(db_content)
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
        if count_up<4:
            up = st.checkbox(f'{city_1}')
            if up:
                masiv_up[0] += 1
                money -= cost_up_city
                count_up += 1
                if count_up<4:
                    x = st.checkbox(f'Улучшить {city_1} 2 раза?')
                    if x:
                        masiv_up[0] += 1
                        money -= cost_up_city
                        count_up += 1
        if count_up<4:
            up1 = st.checkbox(f'{city_2}')
            if up1:
                masiv_up[1] += 1
                money -= cost_up_city
                count_up+=1
                if count_up<4:
                    x1 = st.checkbox(f'Улучшить {city_2} 2 раза?')
                    if x1:
                        masiv_up[1] += 1
                        money -= cost_up_city
                        count_up+=1
        if count_up<4:
            up2 = st.checkbox(f'{city_3}')
            if up2:
                masiv_up[2] += 1
                money -= cost_up_city
                count_up+=1
                if count_up<4:
                    x2 = st.checkbox(f'Улучшить {city_3} 2 раза?')
                    if x2:
                        masiv_up[2] += 1
                        money -= cost_up_city
                        count_up+=1
        if count_up<4:
            up3 = st.checkbox(f'{city_4}')
            if up3:
                masiv_up[3] += 1
                money -= cost_up_city
                count_up+=1
                if count_up<4:
                    x3 = st.checkbox(f'Улучшить {city_4} 2 раза?')
                    if x3:
                        masiv_up[3] += 1
                        money -= cost_up_city
                        count_up+=1

        st.write('На какие города установим щиты?')
        shit = st.checkbox(f'{city_1}  ')
        if shit:
            if city['shit1'] == ' 🛡️':
                st.error('Дружок, у нас так не принято. По 1 щиту на город...')
            else:
                masiv_shit[0] += ' 🛡️'
                money -= cost_shit
        shit1 = st.checkbox(f'{city_2} ')
        if shit1:
            if city['shit2'] == ' 🛡️':
                st.error('Дружок, у нас так не принято. По 1 щиту на город...')
            else:
                masiv_shit[1] += ' 🛡️️'
                money -= cost_shit
        shit2 = st.checkbox(f'{city_3} ')
        if shit2:
            if city['shit3'] == ' 🛡️':
                st.error('Дружок, у нас так не принято. По 1 щиту на город...')
            else:
                masiv_shit[2] += ' 🛡️'
                money -= cost_shit
        shit3 = st.checkbox(f'{city_4} ')
        if shit3:
            if city['shit4'] == ' 🛡️':
                st.error('Дружок, у нас так не принято. По 1 щиту на город...')
            else:
                masiv_shit[3] += ' 🛡️'
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

        sunks_for_who = st.multiselect('На какие страны вы хотите наложить санкции?',['Мексика', 'Канада', 'Австралия', 'Швеция', 'Филипинские острова'])
        money -= 50 * len(sunks_for_who)

        st.write('Ваш баланс после операции:', money)
        col1, col2, col3, col4= st.columns(4)
        col1.metric(masiv_home[1] + city['shit1'] + masiv_shit[0] + f'{city_1}','⚙️' + str(city['up1']+10*masiv_up[0]) + '%' + ' 🌳 ' + str(city['eco1']+10*masiv_up[0]) + '%', masiv_up[0] * 10)
        col2.metric(masiv_home[2] + city['shit2'] + masiv_shit[1] + f'{city_2}','⚙️' + str(city['up2']+10*masiv_up[1]) + '%' + ' 🌳 ' + str(city['eco1']+10*masiv_up[0]) + '%', masiv_up[1] * 10)
        col3.metric(masiv_home[3] + city['shit3'] + masiv_shit[2] + f'{city_3}','⚙️' + str(city['up3']+10*masiv_up[2]) + '%' + ' 🌳 ' + str(city['eco1']+10*masiv_up[0]) + '%', masiv_up[2] * 10)
        col4.metric(masiv_home[4] + city['shit4'] + masiv_shit[3] + f'{city_4}','⚙️' + str(city['up4']+10*masiv_up[3]) + '%' + ' 🌳 ' + str(city['eco1']+10*masiv_up[0]) + '%', masiv_up[3] * 10)

        if lid==1:
            if st.button('Отправить данные'):
                if money >= 0:
                    nowtime=str(current_datetime.hour)+':'+str(current_datetime.minute)+':'+str(current_datetime.second)+' '
                    db_content=db.fetch().items
                    keys=len(db_content)+1
                    db.put({'key':f'{keys}','info': f'{nowtime}{Country_Name}', "money": money, "roket": number, "shit": str(masiv_shit), "up": str(masiv_up),'sunks_for_who': str(sunks_for_who), 'reserch': reserch1})
                    log_content=log.fetch().items
                    keys1=len(log_content)+1
                    log.put({'key':f'{keys1}','info': f'{nowtime}{Country_Name}', 'operation':'upgrade',"money": money, "roket": number, "shit": str(masiv_shit), "up": str(masiv_up),'sunks_for_who': str(sunks_for_who), 'reserch': reserch1})
                    with st.spinner('Wait for it...'):
                        time.sleep(1)
                        st.success('Данные обновлены!')
                        db_content = db.fetch().items
                        st.write(db_content)
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
        first = Global.get('Mexica')
        second=Global.get('Australia')
        third=Global.get('Canada')
        four=Global.get('Filipin')
        five=Global.get('Shvechia')
        six=Global.get('Argentina')
        df=pd.DataFrame(
            [
                {'Страна':'Мексика',
                 'Первый город':'⚙️' + str(first['up1']) + '%' + ' 🌳 ' + str(first['eco1']) + '%',
                 'Второй город':'⚙️' + str(first['up2']) + '%' + ' 🌳 '+ str(first['eco2']) + '%',
                 'Третий город':'⚙️' + str(first['up3']) + '%' + ' 🌳 ' + str(first['eco3']) + '%',
                 'Четвертый город':'⚙️' + str(first['up3']) + '%' + ' 🌳 ' + str(first['eco4']) + '%',
                 'Средний уровень жизни':(first['eco1']+first['eco2']+first['eco3']+first['eco4'])/4},
                {'Страна': 'Австралия',
                 'Первый город': '⚙️' + str(second['up1']) + '%' + ' 🌳 ' + str(second['eco1']) + '%',
                 'Второй город': '⚙️' + str(second['up2']) + '%' + ' 🌳 ' + str(second['eco2']) + '%',
                 'Третий город': '⚙️' + str(second['up3']) + '%' + ' 🌳 ' + str(second['eco3']) + '%',
                 'Четвертый город': '⚙️' + str(second['up3']) + '%' + ' 🌳 ' + str(second['eco4']) + '%',
                 'Средний уровень жизни': (second['eco1'] + second['eco2'] + second['eco3'] + second['eco4']) / 4},
                {'Страна': 'Канада',
                 'Первый город': '⚙️' + str(third['up1']) + '%' + ' 🌳 ' + str(third['eco1']) + '%',
                 'Второй город': '⚙️' + str(third['up2']) + '%' + ' 🌳 ' + str(third['eco2']) + '%',
                 'Третий город': '⚙️' + str(third['up3']) + '%' + ' 🌳 ' + str(third['eco3']) + '%',
                 'Четвертый город': '⚙️' + str(third['up3']) + '%' + ' 🌳 ' + str(third['eco4']) + '%',
                 'Средний уровень жизни': (third['eco1'] + third['eco2'] + third['eco3'] + third['eco4']) / 4},
                {'Страна': 'Филипинские острова',
                 'Первый город': '⚙️' + str(four['up1']) + '%' + ' 🌳 ' + str(four['eco1']) + '%',
                 'Второй город': '⚙️' + str(four['up2']) + '%' + ' 🌳 ' + str(four['eco2']) + '%',
                 'Третий город': '⚙️' + str(four['up3']) + '%' + ' 🌳 ' + str(four['eco3']) + '%',
                 'Четвертый город': '⚙️' + str(four['up3']) + '%' + ' 🌳 ' + str(four['eco4']) + '%',
                 'Средний уровень жизни': (four['eco1'] + four['eco2'] + four['eco3'] + four['eco4']) / 4},
                {'Страна': 'Швеция',
                 'Первый город': '⚙️' + str(five['up1']) + '%' + ' 🌳 ' + str(five['eco1']) + '%',
                 'Второй город': '⚙️' + str(five['up2']) + '%' + ' 🌳 ' + str(five['eco2']) + '%',
                 'Третий город': '⚙️' + str(five['up3']) + '%' + ' 🌳 ' + str(five['eco3']) + '%',
                 'Четвертый город': '⚙️' + str(five['up3']) + '%' + ' 🌳 ' + str(five['eco4']) + '%',
                 'Средний уровень жизни': (five['eco1'] + five['eco2'] + five['eco3'] + five['eco4']) / 4},
                {'Страна': 'Аргентина',
                 'Первый город': '⚙️' + str(six['up1']) + '%' + ' 🌳 ' + str(six['eco1']) + '%',
                 'Второй город': '⚙️' + str(six['up2']) + '%' + ' 🌳 ' + str(six['eco2']) + '%',
                 'Третий город': '⚙️' + str(six['up3']) + '%' + ' 🌳 ' + str(six['eco3']) + '%',
                 'Четвертый город': '⚙️' + str(six['up3']) + '%' + ' 🌳 ' + str(six['eco4']) + '%',
                 'Средний уровень жизни': (six['eco1'] + six['eco2'] + six['eco3'] + six['eco4']) / 4}
            ]
        )
        st.table(df)
        df_chart=pd.DataFrame([
            {'Мексика':(first['eco1']+first['eco2']+first['eco3']+first['eco4'])/4},
            {'Австралия':(second['eco1'] + second['eco2'] + second['eco3'] + second['eco4']) / 4},
            {'Канада': (third['eco1'] + third['eco2'] + third['eco3'] + third['eco4']) / 4},
            {'Филипинские острова': (four['eco1'] + four['eco2'] + four['eco3'] + four['eco4']) / 4},
            {'Швеция': (five['eco1'] + five['eco2'] + five['eco3'] + five['eco4']) / 4},
            {'Аргентина': (six['eco1'] + six['eco2'] + six['eco3'] + six['eco4']) / 4}
        ])
        st.bar_chart(df_chart)