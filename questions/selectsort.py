def select_sort(li):

    n = len(li)

    # 选择的次数，n-1次，每一次选择一个最小的数，依次放到0~n-1 位置
    for j in range(n-1):

        # 选择一次，把最小的数放到0位置
        # 认为0位置的数据最小，记录0位置
        min_index = j
        # 那最小的数，跟后面所有的数据进行比较
        for i in range(1+j, n):
            # 拿最小的数跟当前位置的数比较，让min_index 记录最小的数的位置
            if li[i] < li[min_index]:
                min_index = i
        # for循环结束，min_index指向最小的数
        li[min_index], li[j] = li[j], li[min_index]

if __name__ == '__main__':
    l = [1,2,3,4,5]

    select_sort(l)
    print(l)

    # 稳定性 ： 不稳定
    # 最优时间复杂度 ：O(n^2)
    # 最坏时间复杂度 ：O(n^2)
