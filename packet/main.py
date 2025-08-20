# Для теста вытащи в корень и запусти

from packet import python, test

python.hello("Alex")
print(test.division(10, 2))

#или

import packet

packet.python.hello("Alex")
print(packet.test.division(10, 2))