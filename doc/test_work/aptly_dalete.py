#!/usr/bin/env python3


import sys
import subprocess

#name = input("Введите название пакета для удаления: ")
#result = subprocess.run(name, shell=True, capture_output=True, text=True, check=True)

def run_bash_command(repo_name, package_path):
    # Формируем команду со встроенной частью и аргументами
    command = ["aptly", "repo", "add", repo_name, package_path]
    
# Выполняем команду
    result = subprocess.run(command, capture_output=True, text=True)





# Читаем аргументы командной строки
    repo_name = sys.argv[1]
    package_path = sys.argv[2]


    print(f"stdout:\n{result.stdout}")
    print(f"stderr:\n{result.stderr}")

#print("Output:\n", result.stdout)
#print("Error:\n", result.stderr)


# Выполняем команду bash
    #run_bash_command(repo_name, package_path)
    
    
    
    
    
    
    
    
    
    
    
    
    
    import subprocess
import sys

def run_bash_command(repo_name, package_path):
    # Формируем команду со встроенной частью и аргументами
    command = ["aptly", "repo", "add", repo_name, package_path]
    
    # Выполняем команду
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Выводим результат
    print(f"stdout:\n{result.stdout}")
    print(f"stderr:\n{result.stderr}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python run_command.py <repo_name> <package_path>")
        sys.exit(1)
    
    # Читаем аргументы командной строки
    repo_name = sys.argv[1]
    package_path = sys.argv[2]
    
    # Выполняем команду bash
    run_bash_command(repo_name, package_path)
