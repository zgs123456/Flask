
def insert_sort(li):

    n = len(li)
    # 每次把一个数插入到前面有序序列，从1位置到n位置
    for j in range(1, n):
        # 认为第一个数据有序，从后面拿一个数据，跟前面有序序列再组成有序
        # 把指定位置的数据插入到前面有序序列中
        for i in range(j, 0, -1):  # 2 1
            if li[i] < li[i-1]:
                li[i], li[i-1] = li[i-1], li[i]
            else:
                # 当前位置的数据已经大于前面有序序列的最后一个数，终止循环
                break

if __name__ == '__main__':
    l = [1,2,3,4,5]
    insert_sort(l)
    print(l)

    # 稳定性 ： 稳定
    # 最坏时间复杂度：O(n^2)
    # 最优时间复杂度：O(n)
