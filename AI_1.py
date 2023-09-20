# 1.3
# x = 5 >= 2
# A = {1, 3, 7, 8}
# B = {2, 4, 5, 10, "apple"}
# C = A and B
# d = "Антонина Антоновна", 34, "ж"
# z = "type"
# D = [1, "title", 2, "content"]
# print(x, "|", type(x), "\n", A, "|", type(A), "\n", B, "|", type(B), "\n",
#       C, "|", type(C), "\n", d, "|", type(d), "\n", z, "|", type(z), "\n", D, "|", type(D), "\n")

# 2.3
# x = int(input())
# if (x < -5):
#   print("x : (-infinity; -5)")
# elif ((x >= -5) and (x <= 5)):
#   print("x : [-5; 5]")
# else:
#   print("x : (5; +infinity)")

# 3.3.1
# x = 10
# while (x > 0):
#   print(x)
#   x -=  3

# 3.3.2
# human = ["two arms", "two legs", "one head", "one brain in head",
#         "one heart", "two eyes", "one mouth", "one nose", "two ears"]
# print(human)

# 3.3.3
# i = 2
# c = list()
# for i in range(2, 16):
#   c.append(i)
# print(c)

# 3.3.4
# i = 105
# for i in range(105, 1, -25):
#   print(i)

# 3.3.5
# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# x[::2] = reversed(x[::2])
# print(x)

# 4.3.1
# import numpy
# import matplotlib
# import statistics
# import matplotlib.pyplot as plt
# x = []
# for i in numpy.arange(0.0, 1.0, 0.1):
#     x.append(i)
# mid = sum(x) / len(x)
# median = statistics.median(x)
# print("middle =", mid, "\n", "median =", median)
# plt.figure(figsize = (7, 5))
# plt.plot(x, "ro")
# plt.show()

#4.3.2
# import numpy
# import matplotlib.pyplot as plt
# import math
# mass = list()
# first_mass = list()
# for x in range(1, 11):
#     func = math.sqrt(((1 + ((math.e)**math.sqrt(x)) + (math.cos(x)**2)) / (abs(1 - math.sin(x)**3))) * (math.log(abs(x * 2))))
#     mass.append(func)
# first_mass = mass[:5]
# fig, axs = plt.subplots(nrows = 1, ncols = 2, figsize = (10, 5))
# axs[0].plot(first_mass, "ro")
# axs[0].set_title("Точечный график среза")
# axs[1].plot(mass)
# axs[1].set_title("Линейный график массива")
# plt.show()

# 4.3.3
# import math
# import numpy
# import matplotlib.pyplot as plt
# from scipy.integrate import simps
# from numpy import trapz
# fg = list()
# for x in range(0, 10 + 1):
#     func = abs(math.cos(x * (math.e**(math.cos(x) + math.log(x + 1)))))
#     fg.append(func)
# S = trapz(fg)
# print(S)
# plt.figure(figsize = (7, 5))
# plt.fill(fg, "r")
# plt.show()

# 4.3.4
# import numpy
# import matplotlib.pyplot as plt
# Apple = [131.96, 121.26, 122.15, 131.46, 124.61, 136.96, 145.86, 151.83, 141.50, 149.80, 165.30, 177.57]
# Microsoft = [231.96, 232.38, 235.77, 252.18, 249.68, 270.90, 284.91, 301.88, 281.92, 331.62, 330.59, 336.52]
# Google = [91.37, 101.10, 103.13, 117.68, 117.84, 122.09, 134.73, 144.70, 133.68, 148.05, 141.90, 144.85]
# fig, axs = plt.subplots(nrows = 1, ncols = 3, figsize = (12, 6))
# axs[0].plot(Apple)
# axs[0].set_title("Apple")
# axs[1].plot(Microsoft)
# axs[1].set_title("Microsoft")
# axs[2].plot(Google)
# axs[2].set_title("Google")
# plt.show()

# 4.3.5
# import math
# import numpy
# print("Choose your numbers:")
# x = float(input())
# y = float(input())
# print("x =", x)
# print("y =", y)
# print("Choose the number of opertion that you need:", "\n" "1) +", "\n", "2) -", "\n", "3) *", "\n", 
#       "4) /", "\n", "5) e**x+y", "\n", "6) sin(x+y)", "\n", "7) cos(x+y)", "\n", "8) x**y")
# num_of_op = int(input()) 

# if (num_of_op == 1):
#     print(x + y)

# elif (num_of_op == 2):
#     print(x - y)

# elif (num_of_op == 3):
#     print(x * y)

# elif (num_of_op == 4):
#     print(x / y)

# elif (num_of_op == 5):
#     print(math.e**(x + y))

# elif (num_of_op == 6):
#     print(math.sin(x+y))

# elif (num_of_op == 7):
#     print(math.cos(x+y))

# elif (num_of_op == 8):
#     print(x**y)