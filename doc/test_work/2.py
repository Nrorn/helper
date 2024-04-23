#Написать скрипт, который принимает список чисел и выводит только те числа, которые больше 13.
def numbers_greater_than_13(numbers):
    for num in numbers:
        if num > 13:
            print(num)


numbers = [10, 15, 20, 8, 25]
numbers_greater_than_13(numbers)
