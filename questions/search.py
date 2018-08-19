def search(li, item):
    if len(li) == 0:
        return False
    # 从一半的位置找
    mid_index = len(li)//2

    if item == li[mid_index]:
        return True
    # 如果item>mid,往右找
    elif item > li[mid_index]:
        return search(li[mid_index+1:], item)
    # 如果item<mid,往左找
    else:
        return search(li[:mid_index], item)

if __name__ == '__main__':
    l = [1,2,3,4,5]
    print(search(l, 1))
    print(search(l, 3))
    print(search(l, 5))
    print(search(l, 6))

    # 最优时间复杂度：O(1)
    # 最坏时间复杂度：O(logn)
