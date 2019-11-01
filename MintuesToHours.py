import sys

#转换函数
def Houres(minute):
    if minute < 0:
        range ValueError("Input number cannot be negative")
    else:
        print("{}H,{}M".format(int(minute / 60),minute %60))

try:
    Houres(int(sys.argv[1]))
except:
    print("Parameter Error")