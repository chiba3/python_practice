# coding:utf-8
def judge_odd():
    x = input("Please type number:")
    x = int(x)
    if x % 2 == 0:
        print("偶数")
    elif x % 3 == 0:
        print("奇数")

judge_odd()
