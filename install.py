#coding: utf-8
from datetime import datetime
import os, time
now = datetime.now()
install = True
print ('\033[1m\033[32mСейчас - %s/%s %s:%s:%s\033[0m' % (now.day, now.month, now.hour, now.minute, now.second))
def one():
    log = open('log_p.txt', 'a')
    log.write('➣ %s/%s %s:%s:%s (Полная установка)\n' % (now.day, now.month, now.hour, now.minute, now.second))
    log.close
    os.system("apt-get update")
    os.system("clear")
    print('\033[1m\033[32mОбновление завершено. Начинаю скачивание утилиты  - \033[1m\033[36mhtop\033[0m')
    time.sleep(2.6)
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
    while install:
        b = int(input('\033[1m\033[31mКакую версию Java установить \033[1m\033[32m8 \033[1m\033[31mили \033[1m\033[32m7\033[1m\033[31m?: \033[0m'))
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
    global install
    install = False
def seven():
    print('\033[1m\033[32mНачинаю устанвку \033[1m\033[36mJava 7\033[0m')
    time.sleep(2.6)
    os.system("apt-get install oracle-java7-installer")
    os.system("clear")
    print('\033[1m\033[32mУстоновка завершена.\033[0m')
    global install
    install = False
if __name__ == '__main__':
    one()
