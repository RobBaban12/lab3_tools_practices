def find_odd(numbers:list) -> list[int]:
    return [num for num in numbers if num % 2 == 1]

print(find_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))