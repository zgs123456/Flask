
def bubble_sort(li):

    n = len(li)
    # 共执行冒泡排序的趟数，n-1趟

    for j in range(n-1):  # 0 1 2 3

        flag = False
        # 遍历列表，从0位置移动到倒数第二个位置
        for i in range(n-1-j):  # n-1 n-2 n-3
            # 判断当前位置与下一个位置的数据，如果大于下一个位置的数据，交换
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
                flag = True

        if flag == False:
            break

if __name__ == '__main__':
    l = [1,20,3,45,5]
    bubble_sort(l)

    print(l)

    # 稳定性：稳定
    # 最优时间复杂度 ：O(n)
    # 最坏时间复杂度 ：O(n^2)
