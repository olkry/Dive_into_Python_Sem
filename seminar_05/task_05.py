# ✔ Напишите программу, которая выводит на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print('FizzBuzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else:
#         print(num)


print(*('FizzBuzz' if num % 3 == 0 and num % 5 == 0 else 'Buzz' if num % 5 == 0 else 'Fizz' if num % 3 == 0
        else num for num in range(1, 101)))

# ==============================
fizz_buzz = ('FizzBuzz' if not i % 3 and not i % 5 else ('Fizz' if not i % 3 else ('Buzz' if not i % 5 else i)) for i in
             range(1, 101))

print(*fizz_buzz)
