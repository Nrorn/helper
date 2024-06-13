#!/usr/bin/env python3

import sys
import subprocess

def main()
    #проверяем что аргументы переданы
    if len(sys.argv) < 2:
        print("Usage: python run_command.py '<command>'")
        sys.exit(1)

command = sys.argv[1]


# Вывод результата
print("Output:\n", result.stdout)
#print("Error:\n", result.stderr)

