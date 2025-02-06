numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num >= 0]
negitive_nums = [num for num in numbers if num <= 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 != 0]


print(positive_nums)
print(negitive_nums)
print(even_nums)
print(odd_nums)