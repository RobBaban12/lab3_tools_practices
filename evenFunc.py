def findEven(numbers:list[int]) -> list[int]:
    return [num for num in numbers if num % 2 == 0]

print(findEven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))