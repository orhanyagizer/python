numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
#I use max method in list structure.
numbers_m = max(set(numbers), key = numbers.count)

frequent = numbers.count(numbers_m)

print(numbers,f"The most frequent number is {numbers_m} and it was {frequent} times repeated",sep="\n")