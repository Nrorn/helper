#!/usr/bin/env python3
import subprocess

pkg_name = input("Введите название пакета для удаления: ")
version_pakg = input ("Введите версию пакета: ")

#osnames = ["ubuntu-18.04-devel", "ubuntu-20.04-devel", "ubuntu-22.04-devel"]
Oosnames = ["ubuntu-20.04-tested", "ubuntu-22.04-tested"]
for osname in Oosnames:
    aptly_test_comamand = ["aptly", "-config=/REPO/aptly/ntrepo_git/ntrepo/aptly/etc/aptly-ntrepo.conf", "repo", "remove", osname,  f"{pkg_name} (={version_pakg})"]
    try:
      aptly = subprocess.run(aptly_test_comamand, capture_output=True, text=True, check=True)
      print ("результат:\n", aptly.stdout)
    except subprocess.CalledProcessError as e:
#обрабатываем ошибку CalledProcessError, которая возникает, когда команда, запущенная с помощью subprocess, возвращает код ошибки (не равный 0)
        print(f"Ошибка выполнения команды aptly: {e}").
        print(f"Вывод ошибок:\n{e.stderr}")
    except PermissionError as e:
#обрабатываем ошибки связанные с правами доступа
        print(f"Ошибка прав доступа: {e}")
    except Exception as e:
#выводим все остальные ошибки, которые не были обработаны предыдущим блоком except
        print(f"Ошибка: {e}")
