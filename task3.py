from time import time

class Decor:
     def __call__(self, func):
        def wrapper(*args, **kwargs):
            sum_time = 0
            for _ in range(1000000):
                t1 = time()
                res = func(*args, **kwargs)
                t2 = time()
                sum_time += t2 - t1
            return res, sum_time
        return wrapper

# @Decor()        # С сахаром
def power_i(i, j):
    return i ** j
print(power_i(2, 3))

print(Decor()(power_i)(2, 3))  # Без сахара 
# a = 3 
# print (type(a))
# print(a.__class__)

# class Car:
#     def __call__(self): # Пререгрузка метода соответсвующего операции вызова экземпляра класса, как функции
#         print('Привет')
# c1 = Car()
# print (c1)
# c2 = Car()
# print (c2)
# print(type(c1))
# c1()