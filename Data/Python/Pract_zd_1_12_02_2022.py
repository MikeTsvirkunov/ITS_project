# Найти все натуральные числа, принадлежащие
# отрезку [150 000 000; 300 000 000], которые
# можно представить в виде N = 2m • 3n,
# где m – нечётное число,
# n – чётное число.
# В ответе записать все найденные числа и справа от каждого числа – сумму m+n.
while 1:
    x = 2**int(input("n=")) * 3**int(input("m="))
    print(x, (300000000 >= x >= 150000000))

