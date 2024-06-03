# # Декоратор дополняет работу функций без изменения кода самих функций
# # Декоратор с параметтром
# from time import time
# def outar(param):
#     def decor(func):
#         def wrapper(*args, **kwargs):
#             sum_time = 0
#             for _ in range(param):
#                 t1 = time()
#                 res = func(*args, **kwargs)
#                 t2 = time()
#                 sum_time += t2 - t1
#             return res, sum_time
#         return wrapper
#     return decor


# # @outar(1000000)          # Называется "Синтаксический сахар"
# def power_i(i, j):
#     return i ** j
# print(power_i(2, 3))

# print(outar(1000000)(power_i)(2, 3)) # Без сахара