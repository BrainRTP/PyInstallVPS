#coding: utf-8
from datetime import datetime  #Импортируем библиотеку времени
import os, time #Импортируем библиотеки
now = datetime.now() #Присваиваем "now" значение datetime.now(), что бы сокращать
install = True #Присваиваем значение True (позже понадобится)
print ('\033[1m\033[32mСейчас - %s/%s %s:%s:%s\033[0m' % (now.day, now.month, now.hour, now.minute, now.second))
#Создаем переменные  one, eight и seven.
def one():
    log = open('log_p.txt', 'a') #9,10 и 11 строка - запись в log_p.txt даты Полной установки)
    log.write('➣ %s/%s %s:%s:%s (Полная установка)\n' % (now.day, now.month, now.hour, now.minute, now.second))
    log.close
    os.system("apt-get update") #Тут выполняются различные действия от консоли
    os.system("clear")
    print('\033[1m\033[32mОбновление завершено. Начинаю скачивание утилиты  - \033[1m\033[36mhtop\033[0m')
    time.sleep(2.6) #Это действие фризит на 2.6 сек. Типа Please Wait
    os.system("apt-get install htop")
    os.system("clear")
    print('\033[1m\033[32mУтилита \033[1m\033[36mhtop \033[1m\033[32mустановлена. Начинаю скачивание утилиты  - \033[1m\033[36mscreen\033[0m')
    time.sleep(2.6)
    os.system("apt-get install screen")
    os.system("clear")
    print('\033[1m\033[32mУтилита \033[1m\033[36mscreen \033[1m\033[32mустановлена. Начинаю установку  - \033[1m\033[36mJava\033[0m')
    time.sleep(2.6)
    os.system("echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >>  /etc/apt/sources.list")
    os.system("echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >> /etc/apt/sources.list")
    os.system("apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886")
    os.system("apt-get update")
    os.system("clear")
    while install: #Тут нам и понадобился наш "install = True", который был в начале) (Переменная "while" может иметь 2 значение: False & True)
        b = int(input('\033[1m\033[31mКакую версию Java установить \033[1m\033[32m8 \033[1m\033[31mили \033[1m\033[32m7\033[1m\033[31m?: \033[0m')) #Тут ты должен будешь ввести цифру
        if b == 8:
            eight()
        elif b == 7:
            seven()
        else:
            print("\033[1m\033[31mОшибка.\033[0m")
            time.sleep(0.6)
            os.system("clear")
            continue
def eight():
    print('\033[1m\033[32mНачинаю устанвку \033[1m\033[36mJava 8\033[0m')
    time.sleep(2.6)
    os.system("apt-get install oracle-java8-installer")
    os.system("clear")
    print('\033[1m\033[32mУстоновка завершена.\033[0m')
    global install #Это нужно, что бы install поменял значение вначале кода, что бы отменить последущие "while", т.к они запрашивают у "install" значение, а если оно = False, то действие пропускается/завершается
    install = False
def seven():
    print('\033[1m\033[32mНачинаю устанвку \033[1m\033[36mJava 7\033[0m')
    time.sleep(2.6)
    os.system("apt-get install oracle-java7-installer")
    os.system("clear")
    print('\033[1m\033[32mУстоновка завершена.\033[0m')
    global install
    install = False
"""
while install:
    a = int(input("\033[1m\033[30mВыберите деятельность работы: \033[2m(выход: close/exit | c/e)\033[0m\n\033[1m\033[32m1) Полная установка \033[2m(Java, htop, screen, apt-get update)\033[1m\033[32m\n -> \033[0m"))
    if a == 1:
        one()
    else:
        print('что?')
        time.sleep(0.5)
        continue
    break
"""