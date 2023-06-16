# from asyncio import sleep
from time import sleep
from PIL import Image
from PIL import ImageFilter
from PIL import ImageGrab, ImageOps
from PIL import ImageDraw
# from PIL import ParseMode
from random import randint as rint
from PIL import ImageColor
import telebot
from telebot import types
import os
import math
from telebot.types import InputMediaPhoto

token='5958086903:AAE1Th8DsgCthbxwkbaaDoOvsZkn8fxKzFg'
bot=telebot.TeleBot(token)
col=""
ind=0
stepgrad=0
rest=0
@bot.message_handler(commands=['start','restart'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Фото")
    # item2=types.KeyboardButton("Отчет")
    # item3=types.KeyboardButton("Help")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите',reply_markup=markup)
    
    
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Фото":
        bot.send_message(message.chat.id,'Введите цвет ( формат # FFF0F5 )')
        bot.register_next_step_handler(message,cl)
    elif message.text=="старт" or message.text=="Старт" or message.text=="start" or message.text=="go" or message.text=="GO" or message.text=="Start" or message.text=="z":
        button_message(message)
    
def cl(message):
    global col
    if '#' in message.text:
        col=message.text
    else:
        col="#"+message.text
        
    bot.send_message(message.chat.id,'Пришлите logo (Документом, не сжимать, формат не svg)')
    bot.register_next_step_handler(message,loggo)
    
def loggo(message):
    try:
        chat_id = message.chat.id
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        # downloaded_file = downloaded_file.resize((90,90),Image.ANTIALIAS)
        src = 'C:\\Users\\kryue\\Desktop\\PyScript\\photobotalco\\logo'+'.png'
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Далее")
        markup.add(item1)
        bot.send_message(message.chat.id,':)',reply_markup=markup)
    except Exception:
        bot.send_message(message.chat.id,'Ты сделал что-то не так :/ ')
        pass
    
        
    # file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    # downloaded_file = bot.download_file(file_info.file_path)
    # src = 'C:\\Users\\kryue\\Desktop\\PyScript\\photobotalco\\logo'+'.png'
    # with open(src, 'wb') as new_file:
    #     new_file.write(downloaded_file)
    
    # bot.send_message(message.chat.id,'Выбор градиента')
    
    bot.register_next_step_handler(message,grad)
    
def grad(message):
    # global col
    # global ind
    # global stepgrad
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item10=types.KeyboardButton("Нет")
    item1=types.KeyboardButton("10%")
    item2=types.KeyboardButton("20%")
    item4=types.KeyboardButton("40%")
    item5=types.KeyboardButton("50%")
    item6=types.KeyboardButton("60%")
    item7=types.KeyboardButton("70%")
    item8=types.KeyboardButton("80%")
    item3=types.KeyboardButton("30%")
    item9=types.KeyboardButton("90%")
    item11=types.KeyboardButton("Фильтр")

    markup.row(item1,item2,item3)
    markup.row(item4,item5,item6)
    markup.row(item7,item8,item9)
    markup.row(item10,item11)
    bot.send_message(message.chat.id,'Выбор градиента',reply_markup=markup)
    bot.register_next_step_handler(message,gr)
    
def gr(message):
    global stepgrad
    global ind
    global rest
    if message.text=="10%":
        stepgrad=2.1
        bot.send_message(message.chat.id,'Пришлите фото')
        ind=1
    elif message.text=="20%":
        stepgrad=1.9
        bot.send_message(message.chat.id,'Пришлите фото')
        ind=1
    elif message.text=="Нет":
        # stepgrad=10.0
        bot.send_message(message.chat.id,'Пришлите фото')
        ind=3
    elif message.text=="30%":
        stepgrad=1.7
        bot.send_message(message.chat.id,'Пришлите фото')
        ind=1
    elif message.text=="40%":
        stepgrad=1.5
        bot.send_message(message.chat.id,'Пришлите фото')
        ind=1
    elif message.text=="50%":
        stepgrad=1.3
        bot.send_message(message.chat.id,'Пришлите фото')
        ind=1
    elif message.text=="60%":
        stepgrad=1.1
        bot.send_message(message.chat.id,'Пришлите фото')
        ind=1
    elif message.text=="70%":
        stepgrad=0.9
        bot.send_message(message.chat.id,'Пришлите фото')
        ind=1
    elif message.text=="80%":
        stepgrad=0.7
        bot.send_message(message.chat.id,'Пришлите фото')
        ind=1
    elif message.text=="90%":
        stepgrad=0.5
        bot.send_message(message.chat.id,'Пришлите фото')
        ind=1
    elif message.text=="Фильтр":
        # stepgrad=0.5
        bot.send_message(message.chat.id,'Пришлите фото')
        ind=2
    elif rest==1:
        bot.send_message(message.chat.id,'Пришлите фото')
        ind=1
    else:
        bot.send_message(message.chat.id,'Таких параметров нет')
        ind=0
    
    
    # bot.send_message(message.chat.id,'',reply_markup=markup)
    
    # bot.register_next_step_handler(message,loggo)
    # markup=types.InlineKeyboardMarkup()
    #         # btn1=types.InlineKeyboardButton('2gis',callback_data='2gisDetox')
    # btn1=types.InlineKeyboardButton('10%',callback_data='10%')
    # btn2=types.InlineKeyboardButton('20%',callback_data='20%')
    # btn3=types.InlineKeyboardButton('30%',callback_data='30%')
    # btn4=types.InlineKeyboardButton('40%',callback_data='40%')
    # btn5=types.InlineKeyboardButton('50%',callback_data='50%')
    # btn6=types.InlineKeyboardButton('60%',callback_data='60%')
    # btn7=types.InlineKeyboardButton('70%',callback_data='70%')
    # btn8=types.InlineKeyboardButton('80%',callback_data='80%')
    # btn9=types.InlineKeyboardButton('90%',callback_data='90%')
    #         # markup.row(btn1)
    # markup.row(btn1,btn2,btn3)
    # markup.row(btn4,btn5,btn6)
    # markup.row(btn7,btn8,btn9)
    # bot.send_message(message.chat.id,f'Размер градиента', parse_mode='Markdown',reply_markup=markup)

# @bot.callback_query_handler(func=lambda call:True)
# def callback(call):
# def loggo(message):
#     global ind
#     global stepgrad
#     if message.text=="10%":
#         stepgrad=2.1
        
#     elif message.text=="20%":
#         stepgrad=1.9
#     elif message.text=="30%":
#         stepgrad=1.7
#     elif message.text=="40%":
#         stepgrad=1.5
#     elif message.text=="50%":
#         stepgrad=1.3
#     elif message.text=="60%":
#         stepgrad=1.1
#     elif message.text=="70%":
#         stepgrad=0.9
#     elif message.text=="80%":
#         stepgrad=0.7
#     elif message.text=="90%":
#         stepgrad=0.5
#     ind=1
#     bot.send_message(message.chat.id,'Пришлите фото')
    
@bot.message_handler(content_types=['photo'])
def handle_docs_document(message):
    global ind
    # if ind==0:
    #     file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    #     downloaded_file = bot.download_file(file_info.file_path)
    #     src = 'C:\\Users\\kryue\\Desktop\\PyScript\\photobotalco\\logo'+'.png'
    #     with open(src, 'wb') as new_file:
    #         new_file.write(downloaded_file)
    #     bot.send_message(message.chat.id,'Пришлите фото')
    #     ind=1
    
    if ind==1 or ind==2 or ind==3:
        global col
        global stepgrad
        col=col.strip()
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'C:\\Users\\kryue\\Desktop\\PyScript\\photobotalco\\www'+'.png'
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        # sleep(2)
        # bot.reply_to(message, "Фото добавлено")
        image=Image.open("www.png")
        
        if image.mode != 'RGBA':
                image = image.convert('RGBA')
        s1=str(image.size)
        h1=float(((s1.partition(f',')[0])[1:]))
        w1=float(((s1.partition(f',')[2])[:-1]))
        d=h1*h1+w1*w1
        d=(d ** 0.5)/10
        logo=Image.open("logo.png")
        print(str(logo.size))
        logo = logo.resize((int(d),int(d)),Image.ANTIALIAS)
        print(str(logo.size))
        width, height = image.size
        s1=str(image.size)
        h1=((s1.partition(f',')[0])[1:])
        w1=((s1.partition(f',')[2])[:-1])
        # logo = logo.convert("L")
        # threshold = 50
        # logo = logo.point(lambda x: 255 if x > threshold else 0)
        # logo = logo.resize(
        #     (logo.width // 2, logo.height // 2)
        # )
        # logo = logo.filter(ImageFilter.CONTOUR)
        # logo = logo.point(lambda x: 0 if x == 255 else 255)
        # logo=logo.paste(logo, (480, 160), logo)
        # img_logo.show()
        # logo.show()
        if ind==1:
            gradient = Image.new('L', (width, 1), color=0xFF000)
            print(type(image.size))
            gradient_magnitude=stepgrad
            # for x in range(width):
            for x in range(width):
                gradient.putpixel((x, 0), int(255 * (1 - gradient_magnitude * float(x)/width)))
                # gradient.putpixel((0, x), int(255 * (1 - gradient_magnitude * float(x)/height)))
                # gradient.putpixel( (x, 0), int(255-x))
                # r = 154 ; v = 152 ; b = 100
                # gradient.putpixel( (x, 0), (r, v, b))
                
                # gradient.putpixel((x, 0), 255 -x)
            alpha = gradient.resize(image.size)
            black_im = Image.new('RGBA', (width, height), color=f'{col}')
            sleep(0.2)
            black_im.putalpha(alpha)
            gradient_im = Image.alpha_composite(image, black_im)
            sleep(0.2)
            pos=(gradient_im.width-logo.width-17,gradient_im.height-logo.height-12)
            copied_image = gradient_im
        elif ind==2:
            gradient = Image.new('L', (width, 1), color=0xFF000)
            print(type(image.size))
            gradient_magnitude=stepgrad
            # for x in range(width):
            for x in range(width):
                # print(x)
                # sleep(0.0001)
                gradient.putpixel( (x, 0), int(255-140))
                # gradient.putpixel((x, 0), int(255 * (1 - 0.5 * float(10)/width)))
                # gradient.putpixel((0, x), int(255 * (1 - gradient_magnitude * float(x)/height)))
                # gradient.putpixel( (x, 0), int(255-x))
                # r = 154 ; v = 152 ; b = 100
                # gradient.putpixel( (x, 0), (r, v, b))
                
                # gradient.putpixel((x, 0), 255 -x)
            alpha = gradient.resize(image.size)
            black_im = Image.new('RGBA', (width, height), color=f'{col}')
            sleep(0.2)
            black_im.putalpha(alpha)
            gradient_im = Image.alpha_composite(image, black_im)
            sleep(0.2)
            pos=(gradient_im.width-logo.width-17,gradient_im.height-logo.height-12)
            copied_image = gradient_im
        elif ind==3:
            sleep(0.2)
            gradient_im=image
            pos=(gradient_im.width-logo.width-17,gradient_im.height-logo.height-12)
            copied_image = gradient_im
        
        sleep(0.2)
        copied_image.paste(logo, pos,logo)
        sleep(0.2)
        print(str(copied_image.size))
        s=str(copied_image.size)
        h=((s.partition(f',')[0])[1:])
        w=((s.partition(f',')[2])[:-1])
        if int(h)>1000 and int(w)>700 or int(w)>1000 and int(h)>700:
            h=float(h)/1.5
            w=float(w)/1.5
        else:
            h=float(h)/1.1
            w=float(w)/1.1
        # print(h+" "+w)
        copied_image = copied_image.resize((int(h),int(w)),Image.ANTIALIAS)
        copied_image.save('out.png', 'PNG')
        # sleep(3)
        image=open(f'{os.getcwd()}\\out.png', 'rb')
        # ind=0
        # markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        # item1=types.KeyboardButton("Ещё")
        # ind=0
        # markup.row(item1)
        bot.send_photo(message.chat.id,image, caption = 'Готово. Можете выслать еще фото.')
        # bot.send_photo(message.chat.id,image, caption = 'Готово',reply_markup=markup)
        # bot.register_next_step_handler(message,rest)
        
    # def rest(message):
    #     global ind
    #     global rest
    #     ind=1
    #     rest=1
    #     gr(message)
        
        
        
        
        
        
        
        
        
        
    # bot.register_next_step_handler(message,cl)
    
# def cl(message):
#     # bot.send_message(message.chat.id,'Выберите цвет')
#     col=message.text
    # image=Image.open("www.png")
    # if image.mode != 'RGBA':
    #         image = image.convert('RGBA')
    # logo=Image.open("logo.png")
    # width, height = image.size
    # gradient = Image.new('L', (width, 1), color=0xFF000)

    # gradient_magnitude=1
    # for x in range(width):
    #     gradient.putpixel((x, 0), int(255 * (1 - gradient_magnitude * float(x)/width)))
    #     # gradient.putpixel((x, 0), 255 -x)
    # alpha = gradient.resize(image.size)
    # black_im = Image.new('RGBA', (width, height), color=100) 
    # black_im.putalpha(alpha)
    # gradient_im = Image.alpha_composite(image, black_im)

    # pos=(gradient_im.width-logo.width-5,gradient_im.height-logo.height)
    # copied_image = gradient_im
    # copied_image.paste(logo, pos,logo)
    # bot.send_media_group(message.chat.id, copied_image)
# img = ImageOps.mirror(copied_image)


    # copied_image.save('out.png', 'PNG')
    # copied_image.show()

    
    
bot.polling(none_stop=True)
# @bot.message_handler(content_types='text')
# def message_reply(message):
#     if message.text=="Сделать фото":
#         print(message.from_user.id)
#         markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#         # item1=types.KeyboardButton("Гармония")
#         # item2=types.KeyboardButton("Детокс")
#         # item4=types.KeyboardButton("Наше здоровье")
#         # item5=types.KeyboardButton("Кристал")
#         item=types.KeyboardButton("Назад")
#         markup.row(item)
#         # markup.row(item1,item2)
#         # markup.row(item4,item5)
#         bot.send_message(message.chat.id,'Выберите фото',reply_markup=markup)
        # bot.register_next_step_handler(message,"Пришлите фото")
    # elif message.text=="Help":
    #     markup=types.InlineKeyboardMarkup()
    #     btn1=types.InlineKeyboardButton('Перейти',url='https://www.youtube.com/')
    #     markup.row(btn1)
    #     bot.send_message(message.chat.id,'https://www.youtube.com/',reply_markup=markup)


     
# image=Image.open("001.jpg")
# if image.mode != 'RGBA':
#         image = image.convert('RGBA')
# logo=Image.open("logo.png")
# width, height = image.size
# gradient = Image.new('L', (width, 1), color=0xFF000)

# gradient_magnitude=1
# for x in range(width):
#     gradient.putpixel((x, 0), int(255 * (1 - gradient_magnitude * float(x)/width)))
#     # gradient.putpixel((x, 0), 255 -x)
# alpha = gradient.resize(image.size)
# black_im = Image.new('RGBA', (width, height), color=100) 
# black_im.putalpha(alpha)
# gradient_im = Image.alpha_composite(image, black_im)

# pos=(gradient_im.width-logo.width-5,gradient_im.height-logo.height)
# copied_image = gradient_im
# copied_image.paste(logo, pos,logo)
# # img = ImageOps.mirror(copied_image)


# copied_image.save('out.png', 'PNG')
# copied_image.show()
