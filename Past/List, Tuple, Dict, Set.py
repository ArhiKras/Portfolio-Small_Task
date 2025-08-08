print("# Методы_Работы_со_Списками:")
print('\n')

# append

print("append")
names = ["Alice", "Bob", "Charlie", "David"]
print(names)
names.append("John")
print(names)
print('\n')

# extend

print("extend")
numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.extend([6, 7, 8])
print(numbers)
print('\n')

# insert

print("insert")
names_2 = ["Alice", "Bob", "Charlie", "David"]
names_2.insert(2, "Anna")
print(names_2)
print('\n')

# remove

print("remove")
names_3 = ["Alice", "Bob", "Charlie", "David"]
print(names_3)
names_3.remove("Bob")
print(names_3)
print('\n')

# pop - может вернуть значение

print("pop")
numbers_2 = [1, 2, 3, 4, 5, 6, 7]
print(numbers_2)
delete_save = numbers_2.pop(2)
print(numbers_2)
print(delete_save)
print('\n')

# clear

print("clear")
numbers_3 = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers_3)
numbers_3.clear()
print(numbers_3)
print('\n')

# index_1 - может вернуть значение

print("index_1")
a = [1, 56, -90, 6.7, True, None, "text"]
print(a)
b = a.index(None)
print(b)
print('\n')

# index_2 - может вернуть значение

print("index_2")
nums = [10, 20, 30, 40, 30, 50]
print(nums)
c = nums.index(30, 3, 5)
print(c)
print('\n')

# count - может вернуть значение

print("count")
numbers_count = ["Alice", "Bob", "Bob", "Bob"]
print(numbers_count)
d = numbers_count.count("Bob")
print(d)
print('\n')

# sort_1

print("sort_1")
numbers_4 = [5, 2, 9, 1, 6]
print(numbers_4)
numbers_4.sort()
print(numbers_4)
print('\n')

# sort_1

print("sort_2")
numbers_4 = [5, 2, 9, 1, 6]
print(numbers_4)
numbers_4.sort(reverse=True)
print(numbers_4)
print('\n')

# reverse

print("reverse")
numbers_5 = [1, 2, 3, 4, 5]
print(numbers_5)
numbers_5.reverse()
print(numbers_5)
print('\n')

# max

print("max")
numbers_6 = [1, 40, 29, 100, 50]
print(numbers_6)
print(max(numbers_6))
print('\n')

# len - может вернуть значение

print("len")
numbers_7 = [1, 40, 29, 100, 50]
print(numbers_7)
e = len(numbers_7)
print(e)
print('\n')

# Кортеж(Tuple) - аналог списка, но неизменяемый ()

print("# КОРТЕЖ(Tuple)")
print('\n')
my_tuple = (1, 2, 3, 4, 5)
my_list = [1, 2, 3, 4, 5]
print("my_tuple.append(6) # Ошибка, так как кортеж неизменяемый")
my_list.append(6)
print("Первый элемент:", my_tuple[0])
print("Последний элемент:", my_tuple[4])
print('\n')

# Словари(Dictionary) - {}

print("# СЛОВАРИ(Dictionary)")
print('\n')
my_dict = {
  "name": "Имя",
  "car": "Машина", # ключ|индекс: значение
  "apple": "Яблоко",
  "book": "Книга"
}

# get - может вернуть значение

print("get")
print(my_dict.get("car"))
# or
element = my_dict.get("car")
print(element)
print('\n')

# items - может вернуть значение

print("items")
print(my_dict.items())
print('\n')

# keys - может вернуть значение
print("keys")
element_2 = my_dict.keys()
print(element_2)
print('\n')

# values - может вернуть значение

print("values")
print(my_dict.values())
print('\n')

# pop - может вернуть значение

print("pop")
a = my_dict.pop("car")
print(my_dict)
print(a)
print('\n')

# popitem - может вернуть значение

print("popitem")
b = my_dict.popitem()
print(my_dict)
print(b)
print('\n')

# update - может вернуть значение

print("update")
my_dict.update({"apple": "Ранетка", "cat": "Кот"})
print(my_dict)
print('\n')

# Множества (Set)

print("# МНОЖЕСТВА(Set)")
print('\n')
my_set = {1, 2, 3, 4, 5}

# add

my_set.add(9)
print(my_set)
print('\n')

# remove

my_set.remove(1)
print(my_set)
print('\n')

# discard

my_set.discard(10)
print(my_set)
print('\n')

# pop - может вернуть значение

a = my_set.pop()
print(my_set)
print(a)
print('\n')

# clear

my_set.clear()
print(my_set)
print('\n')

my_set2 = {1, 2, 3, 4, 5}
my_set3 = {5, 6, 7, 8, 9, 10}

# union - может вернуть значение

set_union = my_set2.union(my_set3)
print(set_union)
print('\n')

# intersection - может вернуть значение

set_intersection = my_set2.intersection(my_set3)
print(set_intersection)
print('\n')

# difference - может вернуть значение

set_difference1 = my_set2.difference(my_set3)
set_difference2 = my_set3.difference(my_set2)
print(set_difference1)
print(set_difference2)
print('\n')
