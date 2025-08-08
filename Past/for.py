my_list = [1, 2, 3, 4, 5]
for i in my_list:
  print(i * 2)

print('\n')

for i in range(2):
  print("Hello")
  print("World")

print('\n')

for i in range(8, 15):
  print(i)
  
print('\n')

for i in range(8, 15, 2): # шаг 2
  print(i)

print('\n')

# Пример использования цикла for

a = []
for i in range(11):
  number = i ** 2
  a.append(number)

print(a)