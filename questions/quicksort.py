def quick_sort(li, start, end):
    if start >= end:
        return

    # 定义两个游标
    left = start
    right = end

    # 拿0位置的数据作为参照，让所有的数据都跟它比较
    mid = li[left]

    while left < right:

        # 让右边游标往左移动，找到小于mid的数据，放到左边游标位置
        while left < right and li[right] >= mid:
            right -= 1
        # 循环结束，right指向的数据时小于mid
        li[left] = li[right]

        # 让左边游标往右移动，找到大于mid的数据，放到右边游标位置
        while left < right and li[left] < mid:
            left += 1
        # 循环结束，left指向的数据时大于mid
        li[right] = li[left]
    # while循环结束，left=right，把mid值放到此位置
    li[left] = mid

    # 递归把左边的数据和右边的数据继续排序
    quick_sort(li, start, left-1)
    quick_sort(li, left+1, end)

if __name__ == '__main__':
    l = [5,4,3,1,1]
    # l = 3  [2,1,1,4,5]
    quick_sort(l, 0, len(l)-1)
    print(l)

    # 稳定性：不稳定
    # 最优时间复杂度：O(nlogn)
    # 最坏时间复杂度：O(n^2)
