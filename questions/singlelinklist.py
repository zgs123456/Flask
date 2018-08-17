class Node(object):
    """节点类"""

    def __init__(self, item):
        # 记录元素
        self.item = item
        # 记录下一个节点
        self.next = None


class SingleLinklist(object):
    """链表类"""

    def __init__(self):
        # 记录首节点
        self.__head = None

    def is_empty(self):
        # 判断链表是否为空
        return self.__head is None

    def length(self):
        # 链表长度
        count = 0
        cur = self.__head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def add(self, item):
        # 链表头部加元素
        # 创建节点
        node = Node(item)
        # 新元素记录旧元素的头节点
        node.next = self.__head
        self.__head = node

    def append(self, item):
        # 尾部增加元素
        # 判断链表是否为空
        if self.is_empty():
            self.add(item)
            return
        # 不为空遍历找到尾节点
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        node = Node(item)
        cur.next = node

    def travel(self):
        # 遍历链表
        # 从首节点开始，创建游标
        cur = self.__head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print()

    def insert(self, pos, item):
        # 从指定位置添加
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            # 遍历找到当前位置节点
            cur = self.__head
            index = 0
            while index < (pos - 1):
                index += 1
                cur = cur.next
            # cur指向的是pos前一个节点
            node = Node(item)
            # 让新节点指向pos的节点
            node.next = cur.next
            # 让pos前一个节点指向新节点
            cur.next = node

    def remove(self, item):
        # 删除节点
        cur = self.__head
        # pro记录当前节点的前一个节点
        pro = None
        while cur is not None:
            # 判断当前节点是不是要删除的节点
            if cur.item == item:
                # 如果pro为空，说明删除的是首节点
                if pro is None:
                    self.__head = cur.next
                else:
                    pro.next = cur.next
            pro = cur
            cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        # 遍历，查找每一个节点
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':
    sss = SingleLinklist()
    print(sss.is_empty())
    print(sss.length())
    sss.add(1)
    print(sss.is_empty())
    print(sss.length())
    sss.append(22)
    print(sss.travel())
    sss.insert(1, 222)
    sss.insert(4, 333)
    sss.insert(0, 5)
    print(sss.travel())
    sss.remove(22)
    print(sss.travel())
    print(sss.search(1))
    print(sss.search(99))
