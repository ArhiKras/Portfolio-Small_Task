# list

numbers = [1, 2, 3, 4, 5]
numbers_2 = [1, 2, 3, 4, 5, 6, 7]
numbers_3 = [1, 2, 3, 4, 5, 6, 7, 8]  
names = ["Alice", "Bob", "Charlie", "David"]
names_2 = ["Alice", "Bob", "Charlie", "David"]
names_3 = ["Alice", "Bob", "Bob", "Bob"]
a = [1, 56, -90, 6.7, True, None, "text"]

print(numbers)
print(names[2])
print(a[1:5])
print('\n')

# append
print(names)
print(names_2)
print(names_3)
print(numbers)
print(numbers_2)
print(numbers_3)
names.append("John")
names_2.insert(2,"Anna")
# remove удаляет только первое вхождение
names_3.remove("Bob")
numbers.extend([6, 7, 8])
# можно сохранить удаленное значение в переменную delete_save
delete_save = numbers_2.pop(2)
numbers_3.clear()
b = a.index(None)

print('\n')
print(names)
print(names_2)
print(names_3)
print(numbers)
print(numbers_2)
print(delete_save)
print(numbers_3)
print(b)
print('\n')
nums = [10, 20, 30, 40, 30, 50]

print(nums.index(30))            # 2
print(nums.index(30, 3))         # 4
print(nums.index(30, 4, 6))      # 4
