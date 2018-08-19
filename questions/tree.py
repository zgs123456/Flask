class Node(object):
    """节点"""

    def __init__(self, item):
        # 记录元素内容
        self.item = item
        # 记录左孩子
        self.lChild = None
        # 记录右孩子
        self.rChild = None


class Tree(object):
    """完全二叉树"""

    def __init__(self):
        # 记录根节点
        self.__root = None

    def add(self, item):
        """添加孩子节点"""

        node = Node(item)
        if self.__root is None:
            self.__root = node
            return

        # 添加节点，从上到下，从左到右
        # 用队列
        queue = []
        queue.append(self.__root)

        while queue:

            child = queue.pop(0)
            if child.lChild is None:
                child.lChild = node
                return
            if child.rChild is None:
                child.rChild = node
                return
            queue.append(child.lChild)
            queue.append(child.rChild)

    def detpth_travel(self):
        """深度优先遍历  用递归"""
        self.post_order(self.__root)
        print()

    def pre_order(self, node):
        """先序 根 左 右"""
        if node is None:
            return
        print(node.item,end=" ")
        self.pre_order(node.lChild)
        self.pre_order(node.rChild)

    def in_order(self, node):
        """中序 左 根 右"""
        if node is None:
            return
        self.in_order(node.lChild)
        print(node.item,end=" ")
        self.in_order(node.rChild)

    def post_order(self, node):
        """后序 左  右 根"""
        if node is None:
            return
        self.post_order(node.lChild)
        self.post_order(node.rChild)
        print(node.item,end=" ")

    def breath_travel(self):
        """广度优先遍历 层次遍历"""

        if self.__root is None:
            return

        queue = []
        queue.append(self.__root)

        while queue:

            node = queue.pop(0)
            print(node.item)

            if node.lChild is not None:
                queue.append(node.lChild)
            if node.rChild is not None:
                queue.append(node.rChild)

if __name__ == '__main__':

    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    # tree.breath_travel()
    tree.detpth_travel()

