class Deque(object):
    def __init__(self):
        #创建空的双端队列
        self.data=[]
    def add_front(self,item):
        #从头增加一个元素
        self.data.insert(0,item)
    def add_rear(self,item):
        #从尾部添加元素
        self.data.append(item)
    def re_front(self):
        #从头部删除一个元素
        return self.data.pop(0)
    def re_rear(self):
        #从尾部删除一个元素
        return self.data.pop()

    def is_empty(self):
        #判断双端队列是否为空
        return self.data == []

    def size(self):
        #返回队列的大小
        return len(self.data)

if __name__ == '__main__':
    deque = Deque()
    # 当成栈使用
    # deque.add_rear(1)
    # deque.add_rear(2)
    # deque.add_rear(3)
    #
    # print(deque.re_rear())
    # print(deque.re_rear())
    # print(deque.re_rear())

    # 当成队列使用
    deque.add_front(1)
    deque.add_front(2)
    deque.add_front(3)

    print(deque.re_rear())
    print(deque.re_rear())
    print(deque.re_rear())