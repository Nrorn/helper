#Написать скрипт, который принимает список чисел и возвращает новый список, содержащий только уникальные элементы из исходного списка.
def unique_elements(input_list):
    # Создаем пустой список для хранения уникальных элементов
    unique_list = []
    
    # Проходим по каждому элементу в исходном списке
    for num in input_list:
        # Если элемент еще не содержится в уникальном списке, добавляем его
        if num not in unique_list:
            unique_list.append(num)
    
    return unique_list

# Пример использования
input_list = [1, 2, 3, 4, 2, 3, 5]
result = unique_elements(input_list)
print(result)