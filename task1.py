numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers_a = numbers[:4]
numbers_b = numbers[5:]
summa = sum(numbers_a) + sum(numbers_b)
fourth = summa / len(numbers)
numbers[4] = fourth
print("Измененный список:", numbers)
