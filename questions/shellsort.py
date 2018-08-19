def shell_sort(li):

    n = len(li)
    # 定义步长
    gap = n//2

    # 让步长由大变小，最后必须按照1步长排序
    while gap >= 1:

        # 从步长位置，往后遍历
        for i in range(gap, n):
            # 那当前位置的数据，与i-gap位置数据比较

            # 插入排序
            while (i-gap) >= 0:
                if li[i] < li[i-gap]:
                    li[i], li[i-gap] = li[i-gap], li[i]
                i -= gap
        gap //= 2

# 5
# *****
# ****
# ***
# **
# *

def t(n):
    if n == 0:
        return
    print("*" * n)
    t(n-1)

# 5   5+4+3+2+1

def t1(n):
    if n == 1:
        return 1
    return n+t1(n-1)

if __name__ == '__main__':
    # l = [3,1,2,4,1]
    # # l = [1,5,     2,4,3]
    # shell_sort(l)
    # print(l)

    # 稳定性 ： 不稳定
    # 时间复杂度 ： 跟步长相关
    # t(5)
    print(t1(5))
