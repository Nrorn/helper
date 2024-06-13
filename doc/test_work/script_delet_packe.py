#!/usr/bin/env python3

#Модуль sys,позволяет работать с аргументами командной строки
import sys
#Linux команды в Python можно использовать при помощи subprocess. Этот модуль предоставляет мощные возможности для запуска новых процессов, получения их вывода и взаимодействия с ними.
import subprocess

#def main():
#проверяем что аргументы переданы
#    if len(sys.argv) < 2:
#        print("Usage: python run_command.py '<command>'")
#        sys.exit(1)

# Получаем команду из аргументa командной строки под номером [1]
# если хотим выплнить команду с ключами нужно заключить ее в ковычки ./script_delet_packe.py "ls -hl | grep 1.py""
#sys.argv -"считывает" аргумент переданный за вызовом скрипта
command = sys.argv[1]

# Выполняем команду
result = subprocess.run(command, shell=True, capture_output=True, text=True)


# Выводим результат выполнения команды
#как альтернативу можно использовать- print(result.stdout)
print("Output:\n", result.stdout)
#выведет ошибки если они появяться при выполнении скрипта
#./script_delet_packe.py "ls -hl | grep 1231411.py |ышы"  #Error: /bin/sh: 1: ышы: not found
print("Error:\n", result.stderr)

