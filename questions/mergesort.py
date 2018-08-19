def merge_sort(li):
    if len(li) == 1:
        # print(li)
        return li

    # 把数据拆分成两半
    mid_index = len(li)//2

    left = li[:mid_index]
    right = li[mid_index:]

    # print(left)
    # print(right)

    # 递归继续拆分
    l = merge_sort(left)
    r = merge_sort(right)
    # 把下层方法返回的结果，合并再返回给上层方法
    # res = l + r
    # 把下层方法返回的结果，排序后再返回给上层方法
    res = merge(l, r)
    # print(res)
    return res


def merge(left,right):
    """把两个有序序列再组成有序"""
    # [3,5] [3,4,6]
    left_index = 0
    right_index = 0

    res = []

    while left_index < len(left) and right_index < len(right):

        if left[left_index] <= right[right_index]:
            res.append(left[left_index])
            left_index += 1
        else:
            res.append(right[right_index])
            right_index += 1

    res = res + left[left_index:]
    res = res + right[right_index:]
    return res



if __name__ == '__main__':
    l = [5,4,3,2,1]
    print(merge_sort(l))
    # ll = [3, 5, 6]
    # rl = [1, 2, 4,7]
    # print(merge(ll, rl))
    # 稳定性：稳定
    # 最优时间复杂度：O(nlogn)
    # 最坏时间复杂度：O(nlogn)
