class Stack(object):
    def __init__(self):
        # 创建新的空栈
        self.data = []

    def push(self, item):
        # 添加新元素到栈顶
        self.data.append(item)

    def pop(self):
        # 弹出栈顶元素
        return self.data.pop()

    def peek(self):
        # 返回栈顶元素
        return self.data[-1]

    def is_empty(self):
        # 判断栈是否为空
        return self.data == []

    def size(self):
        # 返回栈里元素的个数
        return len(self.data)


if __name__ == '__main__':
    sss = Stack()
    print(sss.is_empty())
    sss.push(1)
    sss.push(2)
    sss.push(333)
    print(sss.pop())
    print(sss.pop())
    print(sss.peek())
    print(sss.size())
