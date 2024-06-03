from time import time

class Decor:
     def __init__(self, param):
         self.param = param
     def __call__(self, func):
        def wrapper(*args, **kwargs):
            sum_time = 0
            for _ in range(self.param):
                t1 = time()
                res = func(*args, **kwargs)
                t2 = time()
                sum_time += t2 - t1
            return res, sum_time
        return wrapper

# @Decor(1000000)
def power_i(i, j):
    return i ** j
print(power_i(2, 3))

print(Decor(1000000)(power_i)(2, 3))
