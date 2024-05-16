def countWord(string):

  # Разбить строку на слова
  words = string.split()

  # Инициализировать счетчик
  count = 0

  # Проверить каждое слово в списке и обновить счетчик, если слово входит в слово "Tinkioff"
  for word in words:
    if word in {"t", "i", "n", "k", "o", "f"}: 
      count += 1

  # Вернуть количество совпадений
  return count


# Получить ввод от пользователя
string = input()

# Вычислить и вывести количество совпадений
result = countWord(string)
print(result)