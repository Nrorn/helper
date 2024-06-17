#!/usr/bin/env python3

#import sys
import subprocess

#def run_bash_command ()


repo_name = input("Введите название пакета для удаления: ")
version_pakg = input ("Введите версию пакета: ")
command = ["echo", "aptly", "pkg", "remove", repo_name, version_pakg]
result = subprocess.run(command, capture_output=True, text=True, check=True)


print("Output:\n", result.stdout)
print("Error:\n", result.stderr)