import streamlit as st
from deta import Deta
from datetime import datetime
import pandas as pd
import time
st.set_page_config(

    page_title="Мировое господство",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed",  # expanded/collapsed
    menu_items={
        'Get Help': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'Report a bug': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        'About': "# Автор MangoVirus"
    })

with st.sidebar.container():
    col1, col2, col3, col4 = st.columns(4)

    with col2:
        st.image(
            'https://cdn.discordapp.com/attachments/890188503047077928/1070451124869533758/066443762463369c.png?ex=65f2164c&is=65dfa14c&hm=64806b58be52484d5a471b56f1c23e16a7111ced50bf8a0eaf40cf5aff31c855&',
            width=128)

Country_Name = ""
menu = ''
ok = 0
com = 0
Country_Name = 'vjcrdf11'
menu = st.sidebar.selectbox('Меню', ('Улучшение', 'Запуск ракет', 'Принятые запросы', 'Посещения', 'Перевод', 'Деньги', 'Логи'))

current_datetime = datetime.now()
deta = Deta("c07jfupdsmg_p62nqhnHwentnUYMZRxqXC4fxCzNEKyG")
Global = deta.Base("play")

city = Global.get(f'{Country_Name}')

photo = deta.Base('photo')
pp = photo.get('qt2b4gngncsi')
log = deta.Base('log')
db = deta.Base('request_all')
Attak = deta.Base('request_attak')
request = deta.Base('request')
request_money = deta.Base('request_money')
wait = deta.Base('wait')

key = ''
key1 = ''
lvl_eco = [0, 0, 0, 0]
lvl_up = [0, 0, 0, 0]
country1 = Global.get('German')
country2 = Global.get('Tadji')
country3 = Global.get('Norveg')
country4 = Global.get('Turkish')
country5 = Global.get('Yaponia')
country6 = Global.get('Tayland')
if menu == 'Деньги':
    give1 = (country1['up1'] + country1['up2'] + country1['up3'] + country1['up4']) * 5
    st.success(f'ЗП для Германия {give1}', icon='🤑')
    give2 = (country2['up1'] + country2['up2'] + country2['up3'] + country2['up4']) * 5
    st.success(f'ЗП для Таджикистан {give2}', icon='🤑')
    give3 = (country3['up1'] + country3['up2'] + country3['up3'] + country3['up4']) * 5
    st.success(f'ЗП для Норвегии {give3}', icon='🤑')
    give4 = (country4['up1'] + country4['up2'] + country4['up3'] + country4['up4']) * 5
    st.success(f'ЗП для Турции {give4}', icon='🤑')
    give5 = (country5['up1'] + country5['up2'] + country5['up3'] + country5['up4']) * 5
    st.success(f'ЗП для Японии {give5}', icon='🤑')
    give6 = (country6['up1'] + country6['up2'] + country6['up3'] + country6['up4']) * 5
    st.success(f'ЗП для Тайнланда {give6}', icon='🤑')
    if st.button('Выдать деньги'):
        give1 = int(country1['money']) + give1
        Global.update({"money": give1}, "German")
        give2 = int(country2['money']) + give2
        Global.update({"money": give2}, "Tadji")
        give3 = int(country3['money']) + give3
        Global.update({"money": give3}, "Norveg")
        give4 = int(country4['money']) + give4
        Global.update({"money": give4}, "Turkish")
        give5 = int(country5['money']) + give5
        Global.update({"money": give5}, "Yaponia")
        give6 = int(country6['money']) + give6
        Global.update({"money": give6}, "Tayland")
        st.success('Деньги успешно выданы!', icon='💰')
if menu == 'Улучшение':
    st.info('Запросы на улучшение')
    st.error('Не забудь заполнить санкции в ручную!')
    db_content = db.fetch().items
    for slash in range(0, len(db_content)):
        st.write(db_content[slash])
        if st.button(f'Принять улучшение {slash}'):
            slash += 1
            take = db.get(f'{slash}')
            wait_content = wait.fetch().items
            keys = len(wait_content) + 1
            take_info = take['info']
            take_money = take['money']
            take_reserch = take['reserch']
            take_roket = take['roket']
            take_shit = take['shit']
            take_sunks_for_who = take['sunks_for_who']
            take_up = take['up']
            wait.put({'key': f'{keys}', 'info': f'{take_info}', 'money': take_money, 'reserch': take_reserch,
                      'roket': take_roket, 'shit': take_shit,
                      'up': take_up, 'action': 'up'})
            db.delete(f'{slash}')
            st.success('Улучшение принято')
        if st.button(f'Отклонить улучшение {slash}'):
            slash += 1
            db.delete(f'{slash}')
            st.error('Улучшение удалено')
if menu == 'Запуск ракет':
    st.info('Запросы на запуск ракет')
    db_content = Attak.fetch().items
    for slash in range(0, len(db_content)):
        st.write(db_content[slash])
        if st.button(f'Принять запуск {slash}'):
            slash += 1
            take = Attak.get(f'{slash}')
            wait_content = wait.fetch().items
            keys = len(wait_content) + 1
            take_info = take['info']
            take_final_roket = take['final_roket']
            take_country1 = take['Таджикистан']
            take_country2 = take['Япония']
            take_country3 = take['Норвегия']
            take_country4 = take['Германия']
            take_country5 = take['Тайланд']
            take_country6 = take['Турция']
            wait.put({'key': f'{keys}', 'info': f'{take_info}', 'Таджикистан': take_country1, 'Япония': take_country2,
                      'Норвегия': take_country3, 'Германия': take_country4,
                      'Тайланд': take_country5, 'Турция': take_country6, 'action': 'attak'})
            Attak.delete(f'{slash}')
            st.success('Запуск принят')
        if st.button(f'Отклонить запуск {slash}'):
            slash += 1
            Attak.delete(f'{slash}')
            st.error('Запуск удален')

if menu == 'Принятые запросы':
    st.info('Принятые запросы')
    db_content = wait.fetch().items
    for slash in range(0, len(db_content)):
        st.write(db_content[slash])
    if st.button('Завершить раунд'):
        for end in range(0, len(db_content)):
            end += 1
            wait_end = wait.get(f'{end}')
            if wait_end['action'] == 'attak' and int(wait_end['key']) > 1:
                pass
            elif wait_end['action'] == 'up':
                money_end = wait_end['money']
                roket_end = wait_end['roket']
                shit_end = wait_end['shit']
                up_end = wait_end['up']
                coutn = 0
                up_end1, up_end2, up_end3, up_end4 = up_end[0], up_end[1], up_end[2], up_end[3]
                if wait_end['info'].find('German') > 0:
                    if wait_end['reserch'] == 1:
                        reserch = 1
                    elif country1['reserch'] == 1:
                        reserch = 1
                    else:
                        reserch = 0
                    if country1['shit1'] == '🛡️':
                        shit_end[0] = '🛡️'
                    if country1['shit2'] == '🛡️':
                        shit_end[1] = '🛡️'
                    if country1['shit3'] == '🛡️':
                        shit_end[2] = '🛡️'
                    if country1['shit4'] == '🛡️':
                        shit_end[3] = '🛡️'
                    Global.update({'money': money_end, 'reserch': reserch, 'roket': country1['roket'] + roket_end,
                                   'shit1': shit_end[0], 'shit2': shit_end[1], 'shit3': shit_end[2],
                                   'shit4': shit_end[3],
                                   'up1': country1['up1'] + up_end1, 'up2': country1['up2'] + up_end2,
                                   'up3': country1['up3'] + up_end3, 'up4': country1['up4'] + up_end4,
                                   'eco1': country1['eco1'] + up_end1, 'eco2': country1['eco2'] + up_end2,
                                   'eco3': country1['eco3'] + up_end3, 'eco4': country1['eco4'] + up_end4}, 'German')
                elif wait_end['info'].find('Tadji') > 0:
                    if wait_end['reserch'] == 1:
                        reserch = 1
                    elif country2['reserch'] == 1:
                        reserch = 1
                    else:
                        reserch = 0
                    if country2['shit1'] == '🛡️':
                        shit_end[0] = '🛡️'
                    if country2['shit2'] == '🛡️':
                        shit_end[1] = '🛡️'
                    if country2['shit3'] == '🛡️':
                        shit_end[2] = '🛡️'
                    if country2['shit4'] == '🛡️':
                        shit_end[3] = '🛡️'
                    Global.update({'money': money_end, 'reserch': reserch, 'roket': country2['roket'] + roket_end,
                                   'shit1': shit_end[0], 'shit2': shit_end[1], 'shit3': shit_end[2],
                                   'shit4': shit_end[3],
                                   'up1': country2['up1'] + up_end1, 'up2': country2['up2'] + up_end2,
                                   'up3': country2['up3'] + up_end3, 'up4': country2['up4'] + up_end4,
                                   'eco1': country2['eco1'] + up_end1, 'eco2': country2['eco2'] + up_end2,
                                   'eco3': country2['eco3'] + up_end2, 'eco4': country2['eco4'] + up_end4}, 'Tadji')
                elif wait_end['info'].find('Norveg') > 0:
                    if wait_end['reserch'] == 1:
                        reserch = 1
                    elif country3['reserch'] == 1:
                        reserch = 1
                    else:
                        reserch = 0
                    if country3['shit1'] == '🛡️':
                        shit_end[0] = '🛡️'
                    if country3['shit2'] == '🛡️':
                        shit_end[1] = '🛡️'
                    if country3['shit3'] == '🛡️':
                        shit_end[2] = '🛡️'
                    if country3['shit4'] == '🛡️':
                        shit_end[3] = '🛡️'
                    Global.update({'money': money_end, 'reserch': reserch, 'roket': country3['roket'] + roket_end,
                                   'shit1': shit_end[0], 'shit2': shit_end[1], 'shit3': shit_end[2],
                                   'shit4': shit_end[3],
                                   'up1': country3['up1'] + up_end1, 'up2': country3['up2'] + up_end2,
                                   'up3': country3['up3'] + up_end3, 'up4': country3['up4'] + up_end4,
                                   'eco1': country3['eco1'] + up_end1, 'eco2': country3['eco2'] + up_end2,
                                   'eco3': country3['eco3'] + up_end3, 'eco4': country3['eco4'] + up_end4}, 'Norveg')
                elif wait_end['info'].find('Turkish') > 0:
                    if wait_end['reserch'] == 1:
                        reserch = 1
                    elif country4['reserch'] == 1:
                        reserch = 1
                    else:
                        reserch = 0
                    if country4['shit1'] == '🛡️':
                        shit_end[0] = '🛡️'
                    if country4['shit2'] == '🛡️':
                        shit_end[1] = '🛡️'
                    if country4['shit3'] == '🛡️':
                        shit_end[2] = '🛡️'
                    if country4['shit4'] == '🛡️':
                        shit_end[3] = '🛡️'
                    Global.update({'money': money_end, 'reserch': reserch, 'roket': country4['roket'] + roket_end,
                                   'shit1': shit_end[0], 'shit2': shit_end[1], 'shit3': shit_end[2],
                                   'shit4': shit_end[3],
                                   'up1': country4['up1'] + up_end1, 'up2': country4['up2'] + up_end2,
                                   'up3': country4['up3'] + up_end3, 'up4': country4['up4'] + up_end4,
                                   'eco1': country4['eco1'] + up_end1, 'eco2': country4['eco2'] + up_end2,
                                   'eco3': country4['eco3'] + up_end3, 'eco4': country4['eco4'] + up_end4}, 'Turkish')
                elif wait_end['info'].find('Yaponia') > 0:
                    if wait_end['reserch'] == 1:
                        reserch = 1
                    elif country5['reserch'] == 1:
                        reserch = 1
                    else:
                        reserch = 0
                    if country5['shit1'] == '🛡️':
                        shit_end[0] = '🛡️'
                    if country5['shit2'] == '🛡️':
                        shit_end[1] = '🛡️'
                    if country5['shit3'] == '🛡️':
                        shit_end[2] = '🛡️'
                    if country5['shit4'] == '🛡️':
                        shit_end[3] = '🛡️'
                    Global.update({'money': money_end, 'reserch': reserch, 'roket': country5['roket'] + roket_end,
                                   'shit1': shit_end[0], 'shit2': shit_end[1], 'shit3': shit_end[2],
                                   'shit4': shit_end[3],
                                   'up1': country5['up1'] + up_end1, 'up2': country5['up2'] + up_end2,
                                   'up3': country5['up3'] + up_end3,
                                   'up4': country5['up4'] + up_end4,
                                   'eco1': country5['eco1'] + up_end1, 'eco2': country5['eco2'] + up_end2,
                                   'eco3': country5['eco3'] + up_end3, 'eco4': country5['eco4'] + up_end4}, 'Yaponia')
                elif wait_end['info'].find('Tayland') > 0:
                    if wait_end['reserch'] == 1:
                        reserch = 1
                    elif country6['reserch'] == 1:
                        reserch = 1
                    else:
                        reserch = 0
                    if country6['shit1'] == '🛡️':
                        shit_end[0] = '🛡️'
                    if country6['shit2'] == '🛡️':
                        shit_end[1] = '🛡️'
                    if country6['shit3'] == '🛡️':
                        shit_end[2] = '🛡️'
                    if country6['shit4'] == '🛡️':
                        shit_end[3] = '🛡️'
                    Global.update({'money': money_end, 'reserch': reserch, 'roket': country6['roket'] + roket_end,
                                   'shit1': country6['shit1'] + shit_end[0], 'shit2': country6['shit2'] + shit_end[1],
                                   'shit3': country6['shit3'] + shit_end[2], 'shit4': country6['shit4'] + shit_end[3],
                                   'up1': country6['up1'] + up_end1, 'up2': country6['up2'] + up_end2,
                                   'up3': country6['up3'] + up_end3, 'up4': country6['up4'] + up_end4,
                                   'eco1': country6['eco1'] + up_end1, 'eco2': country6['eco2'] + up_end2,
                                   'eco3': country6['eco3'] + up_end3, 'eco4': country6['eco4'] + up_end4}, 'Tayland')
                wait.delete(f'{end}')

        st.success('Улучшения отправлены')
        for end in range(1, len(db_content) + 1):
            shit_end1, shit_end2, shit_end3, shit_end4 = '', '', '', ''
            ec1, ec2, ec3, ec4 = 666, 666, 666, 666
            up1, up2, up3, up4 = 666, 666, 666, 666
            roket = 0
            wait_end = wait.get(f'{end}')
            if wait_end['action'] == 'attak':
                if len(wait_end['Таджикистан']) > 0:
                    chose = wait_end['Таджикистан']
                    shit_end1, shit_end2, shit_end3, shit_end4 = country2['shit1'], country2['shit2'], country2[
                        'shit3'], country2['shit4']
                    ec1, ec2, ec3, ec4 = country2['eco1'], country2['eco2'], country2['eco3'], country2['eco4']
                    up1, up2, up3, up4 = country2['up1'], country2['up2'], country2['up3'], country2['up4']
                    for o in range(0, len(chose)):
                        if chose[o] == 'Душанбе':
                            if country2['shit1'] == '🛡️':
                                ec1 -= 20
                                shit_end1 = ' '
                            elif ec1 < 1:
                                ec1 -= 0.5
                            else:
                                ec1 = 0
                                up1 = 0
                            roket += 1
                        elif chose[o] == 'Бохтар':
                            if country2['shit2'] == '🛡️':
                                ec2 -= 20
                                shit_end2 = ' '
                            elif ec2 < 1:
                                ec2 - 0.5
                            else:
                                ec2 = 0
                                up2 = 0
                            roket += 1
                        elif chose[o] == 'Куляб':
                            if country2['shit3'] == '🛡️':
                                ec3 -= 20
                                shit_end3 = ' '
                            elif ec3 < 1:
                                ec3 -= 0.5
                            else:
                                ec3 = 0
                                up3 = 0
                            roket += 1
                        elif chose[o] == 'Исфара':
                            if country2['shit4'] == '🛡️':
                                ec4 -= 20
                                shit_end4 = ' '
                            elif ec4 < 1:
                                ec4 -= 0.5
                            else:
                                ec4 = 0
                                up4 = 0
                            roket += 1
                    Global.update(
                        {'eco1': ec1, 'up1': up1, 'eco2': ec2, 'up2': up2, 'eco3': ec3, 'up3': up3, 'eco4': ec4,
                         'up4': up4,
                         'shit1': shit_end1, 'shit2': shit_end2, 'shit3': shit_end3, 'shit4': shit_end4}, 'Tadji')
                if len(wait_end['Германия']) > 0:
                    chose = wait_end['Германия']
                    shit_end1, shit_end2, shit_end3, shit_end4 = country1['shit1'], country1['shit2'], country1[
                        'shit3'], country1['shit4']
                    ec1, ec2, ec3, ec4 = country1['eco1'], country1['eco2'], country1['eco3'], country1['eco4']
                    up1, up2, up3, up4 = country1['up1'], country1['up2'], country1['up3'], country1['up4']
                    for o in range(0, len(chose)):
                        if chose[o] == 'Берлин':
                            if country1['shit1'] == '🛡️':
                                ec1 -= 20
                                shit_end1 = ' '
                            elif ec1 < 1:
                                ec1 -= 0.5
                            else:
                                ec1 = 0
                                up1 = 0
                            roket += 1
                        elif chose[o] == 'Гамбург':
                            if country1['shit2'] == '🛡️':
                                ec2 -= 20
                                shit_end2 = ' '
                            elif ec2 < 1:
                                ec2 -= 0.5
                            else:
                                ec2 = 0
                                up2 = 0
                            roket += 1
                        elif chose[o] == 'Мюнхен':
                            if country1['shit3'] == '🛡️':
                                ec3 -= 20
                                shit_end3 = ' '
                            elif ec3 < 1:
                                ec3 -= 0.5
                            else:
                                ec3 = 0
                                up3 = 0
                            roket += 1
                        elif chose[o] == 'Кёльн':
                            if country1['shit4'] == '🛡️':
                                ec4 -= 20
                                shit_end4 = ' '
                            elif ec4 < 1:
                                ec4 -= 0.5
                            else:
                                ec4 = 0
                                up4 = 0
                            roket += 1
                    Global.update(
                        {'eco1': ec1, 'up1': up1, 'eco2': ec2, 'up2': up2, 'eco3': ec3, 'up3': up3, 'eco4': ec4,
                         'up4': up4,
                         'shit1': shit_end1, 'shit2': shit_end2, 'shit3': shit_end3, 'shit4': shit_end4},
                        'German')
                if len(wait_end['Норвегия']) > 0:
                    chose = wait_end['Норвегия']
                    shit_end1, shit_end2, shit_end3, shit_end4 = country3['shit1'], country3['shit2'], country3[
                        'shit3'], country3['shit4']
                    ec1, ec2, ec3, ec4 = country3['eco1'], country3['eco2'], country3['eco3'], country3['eco4']
                    up1, up2, up3, up4 = country3['up1'], country3['up2'], country3['up3'], country3['up4']
                    for o in range(0, len(chose)):
                        if chose[o] == 'Осло':
                            if country3['shit1'] == '🛡️':
                                ec1 -= 20
                                shit_end1 = ' '
                            elif ec1 < 1:
                                ec1 -= 0.5
                            else:
                                ec1 = 0
                                up1 = 0
                            roket += 1
                        elif chose[o] == 'Берген':
                            if country3['shit2'] == '🛡️':
                                ec2 -= 20
                                shit_end2 = ' '
                            elif ec2 < 1:
                                ec2 -= 0.5
                            else:
                                ec2 = 0
                                up2 = 0
                            roket += 1
                        elif chose[o] == 'Тронхейм':
                            if country3['shit3'] == '🛡️':
                                ec3 -= 20
                                shit_end3 = ' '
                            elif ec3 < 1:
                                ec3 -= 0.5
                            else:
                                ec3 = 0
                                up3 = 0
                            roket += 1
                        elif chose[o] == 'Саннвика':
                            if country3['shit4'] == '🛡️':
                                ec4 -= 20
                                shit_end4 = ' '
                            elif ec4 < 1:
                                ec4 -= 0.5
                            else:
                                ec4 = 0
                                up4 = 0
                            roket += 1
                    Global.update(
                        {'eco1': ec1, 'up1': up1, 'eco2': ec2, 'up2': up2, 'eco3': ec3, 'up3': up3,
                         'eco4': ec4, 'up4': up4, 'shit1': shit_end1, 'shit2': shit_end2, 'shit3': shit_end3,
                         'shit4': shit_end4},
                        'Norveg')
                if len(wait_end['Турция']) > 0:
                    chose = wait_end['Турция']
                    shit_end1, shit_end2, shit_end3, shit_end4 = country4['shit1'], country4['shit2'], country4[
                        'shit3'], country4['shit4']
                    ec1, ec2, ec3, ec4 = country4['eco1'], country4['eco2'], country4['eco3'], country4['eco4']
                    up1, up2, up3, up4 = country4['up1'], country4['up2'], country4['up3'], country4['up4']
                    for o in range(0, len(chose)):
                        if chose[o] == 'Стамбул':
                            if country4['shit1'] == '🛡️':
                                ec1 -= 20
                                shit_end1 = ' '
                            elif ec1 < 1:
                                ec1 -= 0.5
                            else:
                                ec1 = 0
                                up1 = 0
                            roket += 1
                        elif chose[o] == 'Анталья':
                            if country4['shit2'] == '🛡️':
                                ec2 -= 20
                                shit_end2 = ' '
                            elif ec2 < 1:
                                ec2 -= 0.5
                            else:
                                ec2 = 0
                                up2 = 0
                            roket += 1
                        elif chose[o] == 'Анкара':
                            if country4['shit3'] == '🛡️':
                                ec3 -= 20
                                shit_end3 = ' '
                            elif ec3 < 1:
                                ec3 -= 0.5
                            else:
                                ec3 = 0
                                up3 = 0
                            roket += 1
                        elif chose[o] == 'Измир':
                            if country4['shit4'] == '🛡️':
                                ec4 -= 20
                                shit_end4 = ' '
                            elif ec4 < 1:
                                ec4 -= 0.5
                            else:
                                ec4 = 0
                                up4 = 0
                            roket += 1
                    Global.update(
                        {'eco1': ec1, 'up1': up1, 'eco2': ec2, 'up2': up2, 'eco3': ec3, 'up3': up3,
                         'eco4': ec4, 'up4': up4, 'shit1': shit_end1, 'shit2': shit_end2, 'shit3': shit_end3,
                         'shit4': shit_end4},
                        'Turkish')
                if len(wait_end['Япония']) > 0:
                    chose = wait_end['Япония']
                    shit_end1, shit_end2, shit_end3, shit_end4 = country5['shit1'], country5['shit2'], country5[
                        'shit3'], country5['shit4']
                    ec1, ec2, ec3, ec4 = country5['eco1'], country5['eco2'], country5['eco3'], country5['eco4']
                    up1, up2, up3, up4 = country5['up1'], country5['up2'], country5['up3'], country5['up4']
                    for o in range(0, len(chose)):
                        if chose[o] == 'Токио':
                            if country5['shit1'] == '🛡️':
                                ec1 -= 20
                                shit_end1 = ' '
                            elif ec1 < 1:
                                ec1 -= 0.5
                            else:
                                ec1 = 0
                                up1 = 0
                            roket += 1
                        elif chose[o] == 'Осака':
                            if country5['shit2'] == '🛡️':
                                ec2 -= 20
                                shit_end2 = ' '
                            elif ec2 < 1:
                                ec2 -= 0.5
                            else:
                                ec2 = 0
                                up2 = 0
                            roket += 1
                        elif chose[o] == 'Нагоя':
                            if country5['shit3'] == '🛡️':
                                ec3 -= 20
                                shit_end3 = ' '
                            elif ec3 < 1:
                                ec3 -= 0.5
                            else:
                                ec3 = 0
                                up3 = 0
                            roket += 1
                        elif chose[o] == 'Кавасаки':
                            if country5['shit4'] == '🛡️':
                                ec4 -= 20
                                shit_end4 = ' '
                            elif ec4 < 1:
                                ec4 -= 0.5
                            else:
                                ec4 = 0
                                up4 = 0
                            roket += 1
                    Global.update(
                        {'eco1': ec1, 'up1': up1, 'eco2': ec2, 'up2': up2, 'eco3': ec3, 'up3': up3, 'eco4': ec4,
                         'up4': up4, 'shit1': shit_end1, 'shit2': shit_end2, 'shit3': shit_end3, 'shit4': shit_end4},
                        'Yaponia')
                if len(wait_end['Тайланд']) > 0:
                    chose = wait_end['Тайланд']
                    shit_end1, shit_end2, shit_end3, shit_end4 = country5['shit1'], country5['shit2'], country5[
                        'shit3'], country5['shit4']
                    ec1, ec2, ec3, ec4 = country6['eco1'], country6['eco2'], country6['eco3'], country6['eco4']
                    up1, up2, up3, up4 = country6['up1'], country6['up2'], country6['up3'], country6['up4']
                    for o in range(0, len(chose)):
                        if chose[o] == 'Бангкок':
                            if country6['shit1'] == '🛡️':
                                ec1 -= 20
                                shit_end1 = ' '
                            elif ec1 < 1:
                                ec1 -= 0.5
                            else:
                                ec1 = 0
                                up1 = 0
                            roket += 1
                        elif chose[o] == 'Кхонкэн':
                            if country6['shit2'] == '🛡️':
                                ec2 -= 20
                                shit_end1 = ' '
                            elif ec2 < 1:
                                ec2 -= 0.5
                            else:
                                ec2 = 0
                                up2 = 0
                            roket += 1
                        elif chose[o] == 'Чиангмай':
                            if country6['shit3'] == '🛡️':
                                ec3 -= 20
                                shit_end1 = ' '
                            elif ec3 < 1:
                                ec3 -= 0.5
                            else:
                                ec3 = 0
                                up3 = 0
                            roket += 1
                        elif chose[o] == 'Паттайя':
                            if country6['shit4'] == '🛡️':
                                ec4 -= 20
                                shit_end1 = ' '
                            elif ec4 < 1:
                                ec4 -= 0.5
                            else:
                                ec4 = 0
                                up4 = 0
                            roket += 1
                    Global.update(
                        {'eco1': ec1, 'up1': up1, 'eco2': ec2, 'up2': up2, 'eco3': ec3, 'up3': up3,
                         'eco4': ec4, 'up4': up4, 'shit1': shit_end1, 'shit2': shit_end2, 'shit3': shit_end3,
                         'shit4': shit_end4},
                        'Tayland')
            if wait_end['info'].find('German') > 0:
                roket = country1['roket'] - roket
                Global.update({'roket': roket}, 'German')
            elif wait_end['info'].find('Tadji') > 0:
                roket = country2['roket'] - roket
                Global.update({'roket': roket}, 'Tadji')
            elif wait_end['info'].find('Norveg') > 0:
                roket = country3['roket'] - roket
                Global.update({'roket': roket}, 'Norveg')
            elif wait_end['info'].find('Turkish') > 0:
                roket = country4['roket'] - roket
                Global.update({'roket': roket}, 'Turkish')
            elif wait_end['info'].find('Yaponia') > 0:
                roket = country5['roket'] - roket
                Global.update({'roket': roket}, 'Yaponia')
            elif wait_end['info'].find('Tayland') > 0:
                roket = country6['roket'] - roket
                Global.update({'roket': roket}, 'Tayland')
            wait.delete(f'{end}')
        st.success('Ракеты запущенны')

if menu == 'Посещения':
    st.info('Запросы на посещения')
    db_content = request.fetch().items
    for slash in range(0, len(db_content)):
        st.write(db_content[slash])
        if st.button(f'Удалить запрос{slash}'):
            forgot = db_content[slash]['key']
            slash += 1
            request.delete(f'{forgot}')

if menu == 'Перевод':
    st.info('Перевод денег')
    db_content = request_money.fetch().items
    for slash in range(0, len(db_content)):
        st.write(db_content[slash])
        if st.button('Принять преревод'):
            slash += 1
            give_money = request_money.get(f'{slash}')
            money_from = country1['money'] - give_money['price']
            hihi = give_money['from']
            if give_money['come'] == 'Турция':
                money_who = country4['money'] + give_money['price']
                Global.update({'money': money_from}, f'{hihi}')
                Global.update({'money': money_who}, 'Turkish')
            elif give_money['come'] == 'Норвегия':
                money_who = country3['money'] + give_money['price']
                Global.update({'money': money_from}, f'{hihi}')
                Global.update({'money': money_who}, 'Norveg')
            elif give_money['come'] == 'Таджикистан':
                money_who = country2['money'] + give_money['price']
                Global.update({'money': money_from}, f'{hihi}')
                Global.update({'money': money_who}, 'Tadji')
            elif give_money['come'] == 'Тайланд':
                money_who = country6['money'] + give_money['price']
                Global.update({'money': money_from}, f'{hihi}')
                Global.update({'money': money_who}, 'Tayland')
            elif give_money['come'] == 'Япония':
                money_who = country5['money'] + give_money['price']
                Global.update({'money': money_from}, f'{hihi}')
                Global.update({'money': money_who}, 'Yaponia')
            elif give_money['come'] == 'Германия':
                money_who = country1['money'] + give_money['price']
                Global.update({'money': money_from}, f'{hihi}')
                Global.update({'money': money_who}, 'German')

if menu == 'Логи':
    st.info('Логи')
    db_content = log.fetch().items
    for slash in range(0, len(db_content)):
        st.write(db_content[slash])