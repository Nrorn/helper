def countWord(string):
  """
  Counts the number of times the word "Tinkoff" can be formed from the letters in the given string.

  Args:
    string (str): The input string.

  Returns:
    int: The number of times the word "Tinkoff" can be formed.
  """

  # Преобразовать строку в нижний регистр
  string = string.lower()

  # Создать словарь для хранения количества каждого символа в строке
  char_count = {}
  for char in string:
    if char.isalpha():  # Проверить, является ли символ буквой
      if char not in char_count:
        char_count[char] = 0
      char_count[char] += 1

  # Инициализировать счетчик
  count = 0

  # Проверить, достаточно ли символов для формирования слова "Tinkoff"
  for char in "tinkoff":
    if char not in char_count or char_count[char] == 0:
      return 0

  # Вычислить количество раз, когда слово "Tinkoff" может быть сформировано
  min_count = min(char_count["t"], char_count["i"], char_count["n"], char_count["k"], char_count["o"], char_count["f"])
  count += min_count

  # Вернуть количество совпадений
  return count


# Пример использования
string = input()

# Вычислить и вывести количество совпадений
print(countWord(string))