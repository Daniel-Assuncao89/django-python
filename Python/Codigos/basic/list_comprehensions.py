from functools import reduce

numbers = []
for i in range(30):
    numbers.append(i)

squared_numbers = []
for number in numbers:
    if number % 2 == 0:
        squared = number ** 2
        squared_numbers.append(squared)

squared_numbers = [i ** 2 for i in numbers if i % 2 == 0]
squared_filter = list(filter(lambda x: x % 2 == 0, numbers))
squared_map = list(map(lambda x: x % 2 == 0, numbers))
squared_reduce = reduce(lambda x, y: x + y, numbers)
print("List comprehensions: ", squared_numbers)
print("Filter: ", squared_filter)
print("Map:", squared_map)
print("Reduce: ", squared_reduce)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# with if and else condition
e = [x if x > 4 else 'less than 4' for x in lst]
print(e)

# with more than one if and else condition
f = ['Two' if x % 2 == 0 else "Three" if x % 3 == 0 else 'not 2 & 3' for x in lst]
print(f)

# nums = [1, 2, 3, 4]
# fruit = ["Apples", "Peaches", "Pears", "Bananas"]
# print([(i, f) for i in nums for f in fruit])
#
# for i in range(4):
#     print(i)
#     for y in range(4):
#         print(y)
#
# print([(i, y) for i in range(1, 5) for y in range(1, 5)])
