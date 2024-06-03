# # Декоратор дополняет работу функций без изменения кода самих функций
# from time import time

# def decor(func):
#     def wrapper(*args, **kwargs):
#         sum_time = 0
#         for _ in range(1000000):
#             t1 = time()
#             res = func(*args, **kwargs)
#             t2 = time()
#             sum_time += t2 - t1
#         return res, sum_time
#     return wrapper

# # @decor           # Называется "Синтаксический сахар"
# def power_i(i, j):
#     return i ** j
# print(power_i(2, 3))

# # @decor
# # def get_sum(a, b):
# #     return a + b
# # print(get_sum(2, 3))

# print (decor(power_i)(3, 3))