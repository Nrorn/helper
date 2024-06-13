#!/usr/bin/env python3

#Модуль sys,позволяет работать с аргументами командной строки
import sys
#Linux команды в Python можно использовать при помощи subprocess. Этот модуль предоставляет мощные возможности для запуска новых процессов, получения их вывода и взаимодействия с ними.
import subprocess


dmesg = subprocess.Popen(['dmesg'], stdout=subprocess.PIPE)
grep = subprocess.Popen(['grep', 'sda'], stdin=dmesg.stdout)
dmesg.stdout.close()
output = grep.comunicate()[0]