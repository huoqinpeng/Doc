# days = int(input("Enter Days:"))
# months = days //30
# days = days % 30
# print("Months = {} Days = {}".format(months,days))
#
# days = int(input("Enter days: "))
#
# print(5 and 4)


# sum = 0
# for i  in range(1,11):
#     sum += 1.0/i
#     print("{:2d} {:6.4f}".format(i ,sum) )

# basic_salary = 1500
# bonus_rate = 200
# commission_rate = 0.02
# numberofcamera = int(input("Enter the number of inputs sold: "))
# price = float(input("Enter the price of camera: "))
# bonus = (bonus_rate * numberofcamera)
# commission = (commission_rate * price * numberofcamera)
# print("Bonus        = {:6.2f}".format(bonus))
# print("Commission   = {:6.2f}".format(commission))
# print("Gross salary = {:6.2f}".format(basic_salary + bonus + commission))


# import  math
# area = 2* 2*math.pi
# print("{:.10f}".format(area))

# number = int(input("Enter a number："))
# if number < 100:
#     print("The number is less then 100")

#
# n = 0
# while n < 10000000000:
#     print(n)
#     n += 1

# a,b = 0,1
# while b < 1000000:
#     print(b)
#     a,b = b,a+b

#
# a, b = 0, 1
# while b < 100:
#     print(b, end=' ')
#     a, b = b, a + b
# print()


# x = float(input("Enter the value of x: "))
# n = term = num = 1
# result = 1.0
# while n <= 100:
#     term *= x / n
#     result += term
#     n += 1
#     if term < 0.0001:
#         break
# print("No of Times= {} and Sum= {}".format(n, result))

# i = 1
# print("-" * 50)
# while i < 11:
#     n = 1
#     while n <= 10:
#         print("{:5d}".format(i * n), end=' ')
#         n += 1
#     print()
#     i += 1
# print("-" * 50)

#

#
# a = [1,"dsad",'dsdsd',2324]
# print(a)
#


# a = ['Shiyanlou','is','powerful']
# # for x in a:
# #     print(x)
# # a = [1,2,3,4,5,6,78,9,0]
# # for x in a:
# #     print(x)
# #
# # for i in range(5):
# #     print(i)
# # for x in range(1,10):
# #     print(x)
# # print(list(range(1, 15, 3)))

# while True:
#     n = int(input("Please enter en Integer:"))
#     if n < 0:
#         continue
#     elif n == 0:
#         break
#     print("Square is",n**2)
# print("Goodby")


# for i  in range(0,5):
# #     print(i)
# # else:
# #     print("Bye bye")


#
# squares = list(map(lambda x: x**2, range(110000)))
# print(squares)

# n = int(input("Enter the number of students:"))
# data = {} #用来存储数据的字典变量
# Subjects = ('Physices','Maths','History') #所有科目
# for i in range(0,n):
#     name = input('Enter the name of the student {}'.format(i+1)) #获得学生名称
#     marks = []
#     for x in Subjects:
#         marks.append(int(input('Enter marks of {}'.format(x)))) # 获得每一科的分数
#     data[name] = marks
# print(data)
# for x,y in data.items():
#     total = sum(y)
#     print("{}'s total marks {}".format(x,total))
#     if total < 120:
#         print(x,"failed :(")
#     else:
#         print(x,"passed :)")

# n = int(input("Enter the value of n: "))
# print("Enter values for the Matrix A")
# a = []
# for i in range(n):
#     a.append([int(x) for x in input().split()])
# print("Enter values for the Matrix B")
# b = []
# for i in range(n):
#     b.append([int(x) for x in input().split()])
# c = []
# for i in range(n):
#     c.append([a[i][j] * b[i][j] for j in range(n)])
# print("After matrix multiplication")
# print("-" * 7 * n)
# for x in c:
#     for y in x:
#         print(str(y).rjust(5), end=' ')
#     print()
# print("-" * 7 * n)

# s = input("Please enter a string: ")
# z = s[::-1]  #把输入的字符串s 进行倒序处理形成新的字符串z
# if s == z:
#     print("The string is a palindrome")
# else:
#     print("The string is not a palindrome")



# def palindrome(s):
#     return s == s[::-1]
# if __name__ == '__main__':
#     s = input("Enter a string: ")
#     if palindrome(s):
#         print("Yay a palindrome")
#     else:
#         print("Oh no, not a palindrome")


import math

def longest_side(a, b):
    """
    Function to find the length of the longest side of a right triangle.

    :arg a: Side a of the triangle
    :arg b: Side b of the triangle

    :return: Length of the longest side c as float
    """
    return math.sqrt(a*a + b*b)

if __name__ == '__main__':
    print(longest_side.__doc__)
    print(longest_side(4,5))