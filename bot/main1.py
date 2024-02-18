import telebot
import time
from telebot import types
from datetime import datetime
from deta import Deta
from datetime import datetime

deta = Deta("c0hqbepjrcp_YWerRut2VNYfRixXNojXJ3Hy3kN3SxnK")#TG bot
db = deta.Base("users")
db_content = db.fetch().items
maths=deta.Base('maths')
mt=maths.get('1')
teams=deta.Base('teams')
bot = telebot.TeleBot('6651595825:AAEVJU49UaQdiEm8EWGTc37Tl0PouCo0PQg')

markup = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Личный кабинет')
btn2 = types.KeyboardButton('Связь с нами')
btn3= types.KeyboardButton('Регистрация на игру')
if mt['start']==1:
    btn4 = types.KeyboardButton('Запустить игровой режим')
    markup.row(btn4)
markup.row(btn1, btn2)
markup.row(btn3)
back=types.KeyboardButton('Главная')

@bot.message_handler(commands=['start'])
def welcome1(message):
    bot.send_message(message.from_user.id, 'Приветствую! Я бот-помощник для проведения МГ.',reply_markup=markup)
    test=message.from_user.id
    db.put({'key': f'{test}','nick':f'{message.from_user.username}','country':'None'})
    return test
def welcome(message):
    bot.send_message(message.from_user.id, 'Приветствую! Я бот-помощник для проведения МГ.', reply_markup=markup)



@bot.message_handler()
def callback_query_handler(message):
    if message.text =='Запустить игровой режим':
        user=db.get(f'{message.from_user.id}')
        g = user['country'].replace('request.', '')
        g = g.replace('rill.','')
        if user['country'].find('rill.')==0:
            bot.send_message(message.from_user.id,'Игровой режим запущен')
            bot.send_message(message.from_user.id,f'Вы играете за {g}')
        elif user['country'].find('request.')==0:
            bot.send_message(message.from_user.id,f'Ваша заявка на вход в команду страны {g} ещё не принята, если игра уже началась обратитесь к админестратору')
        elif user['country'].find('None')==0:
            bot.send_message(message.from_user.id,'Вы не отправляли заявку на вступление в команду страны, если вы участвуете в игре, отправте заявку и сообщите админестратору')
        else:
            bot.send_message(message.from_user.id,'Ошибка 03')
    if message.text == 'Личный кабинет':
        lk_markup = types.ReplyKeyboardMarkup()
        lk_btn1 = types.InlineKeyboardButton('Выбрать страну')
        lk_markup.row(lk_btn1)
        lk_markup.add(back)
        bot.reply_to(message, 'Тут информация про вас.')
        info = db.get(f'{message.from_user.id}')
        t1='Никнейм: '+info['name']
        t2='ID: '+info['key']
        if info['country'].find('request.')==0:
            ll=info['country'].replace('request.','')
            qq=f'Ваш запрос на добавление в команду страны {ll} на рассмотрении'
        elif info['country'].find('None')==0:
            qq='Вы ещё не выбрали страну'
        elif info['country'].find('rill.')==0:
            qq=info['country'].replace('rill.','')
        else:
            bot.send_message(message.from_user.id,'Ошибка 02')
        t3='Страна: '+qq
        txt=f'''{t1}
{t2}
{t3}
                '''
        bot.send_message(message.from_user.id,txt,reply_markup=lk_markup)

    if message.text == 'start' or message.text == 'Главная':
        welcome(message)
    if message.text == 'Связь с нами':
        bot.reply_to(message, '8 800 555 35 35')
    if message.text=='Регистрация на игру':
        bot.send_message(message.from_user.id,'''Очень рад, что вы хотите зарегестрироваться на игру.
В приоретете будут рассматриваться заявки командой, так как знакомые люди, лучше сыграны, чем соло.
Если Вы оставите заявку в одиночку, мы постараемся найти вам хорошую команду.
        ''')
        match_info(message)
    if message.text == 'Выбрать страну':
        cnt = types.InlineKeyboardMarkup()
        cnt1 = types.InlineKeyboardButton('Канада', callback_data='Canada')
        cnt2 = types.InlineKeyboardButton('Индия', callback_data='India')
        cnt3 = types.InlineKeyboardButton('Испания', callback_data='Ispania')
        cnt.row(cnt1, cnt2,cnt3)
        cnt4 = types.InlineKeyboardButton('Россия', callback_data='Russia')
        cnt5 = types.InlineKeyboardButton('Швеция', callback_data='Shvechia')
        cnt6 = types.InlineKeyboardButton('Сирия', callback_data='Siria')
        cnt.row(cnt4,cnt5,cnt6)
        bot.send_message(message.from_user.id,'Выберете страну за которую вы играете',reply_markup=cnt)

def match_info(message):
    lore=mt['lore']
    if lore=='None':
        bot.send_message(message.from_user.id,'Запланированных матчей пока нет')
    else:
        reg_markup = types.InlineKeyboardMarkup()
        solo=types.InlineKeyboardButton('Зерегестрироваться Соло',callback_data='solo')
        team=types.InlineKeyboardButton('Зарегестрироваться Командой',callback_data='team')
        reg_markup.row(solo,team)
        bot.send_message(message.from_user.id,f'{lore}',reply_markup=reg_markup)


@bot.callback_query_handler(func=lambda callback: True)
def ans_country(callback):
    if callback.data=='Canada':
        db.update({'country':f'request.Canada'},f'{callback.from_user.id}')
        bot.send_message(callback.from_user.id,'Заявка на вступление в команду страны Canada, была отправлена')
    if callback.data=='India':
        db.update(db.update({'country':f'request.India'},f'{callback.from_user.id}'))
        bot.send_message(callback.from_user.id, 'Заявка на вступление в команду страны India, была отправлена')
    if callback.data=='Ispania':
        db.update(db.update({'country':f'request.Ispania'},f'{callback.from_user.id}'))
        bot.send_message(callback.from_user.id, 'Заявка на вступление в команду страны Ispania, была отправлена')
    if callback.data=='Russia':
        db.update(db.update({'country': f'request.Russia'}, f'{callback.from_user.id}'))
        bot.send_message(callback.from_user.id, 'Заявка на вступление в команду страны Russia, была отправлена')
    if callback.data=='Shvechia':
        db.update(db.update({'country': f'request.Shvechia'}, f'{callback.from_user.id}'))
        bot.send_message(callback.from_user.id, 'Заявка на вступление в команду страны Shvechia, была отправлена')
    if callback.data=='Siria':
        db.update(db.update({'country': f'request.Siria'}, f'{callback.from_user.id}'))
        bot.send_message(callback.from_user.id, 'Заявка на вступление в команду страны Siria, была отправлена')
    if callback.data=='solo':
        adm = types.InlineKeyboardMarkup()
        adm.add(types.InlineKeyboardButton('Администратор', url='t.me/mangovirus'))

        bot.send_message(callback.message.chat.id,'''Соло игроков пока не принимаем, ждите новостей.
Или напишите Администратору.''', reply_markup=adm)
    if callback.data=='team':
        bot.send_message(callback.message.chat.id,'''Напишите Username из телеграма участников вашей команды.
(Пример: @vanysqq, @mangovirus, @ignatevphotos)
        ''')
        bot.register_next_step_handler(callback.message, reg_team)
def reg_team(message):
    teameats=message.text
    id_owner=message.from_user.id
    bot.send_message(id_owner,'''Введите пару стран за которые вы хотели бы отыграть?
(Пример: Швеция, Филипинские острова)
Убедительная просьба проявить креативность. Не надо писать Россия и Украина.''')
    now = datetime.now()
    teams.put({'key':f'{id_owner}','teameats':f'{teameats}','time':f'{now}'})
    bot.register_next_step_handler(message, reg_team2)
def reg_team2(message):
    teams.update({'country':message.text},f'{message.from_user.id}')
    bot.send_message(message.from_user.id,'''Готовы ли вы отыграть интересную РПшку?
Например, Австралия играла с перевернутой камерой, а индия в подходящих шапочках.
(Да, это бонально, но свое хаха появляется и настроение улучшается)''')
    bot.register_next_step_handler(message, reg_team3)
def reg_team3(message):
    teams.update({'RP':message.text},f'{message.from_user.id}')
    bot.send_message(message.from_user.id,'Ваша заявка была отправлена')

bot.infinity_polling()
