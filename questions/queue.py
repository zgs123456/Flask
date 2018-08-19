class Queue(object):

    def __init__(self):
        #创建一个空的队列
        self.data = []

    def enqueue(self, item):
        #往队列中添加一个item元素
        self.data.insert(0, item)

    def dequeue(self):
        #从队列头部删除一个元素
        return self.data.pop()

    def is_empty(self):
        #判断一个队列是否为空
        return self.data == []

    def size(self):
        #返回队列的大小
        return len(self.data)

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.size())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
