class Node:
    def __init__(self, data):
        self.data = data
        self.color = 'red'  # Novo nó é vermelho
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(None)  # Folha NIL
        self.NIL_LEAF.color = 'black'
        self.root = self.NIL_LEAF

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF

        parent = None
        current = self.root

        while current != self.NIL_LEAF:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'red'
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)

        self.root.color = 'black'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL_LEAF:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL_LEAF:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def search(self, data):
        current = self.root
        while current != self.NIL_LEAF:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, data):
        node_to_delete = self.search(data)
        if node_to_delete is None:
            print(f"Nó {data} não encontrado.")
            return

        original_color = node_to_delete.color
        if node_to_delete.left == self.NIL_LEAF:
            successor = node_to_delete.right
            self.transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == self.NIL_LEAF:
            successor = node_to_delete.left
            self.transplant(node_to_delete, node_to_delete.left)
        else:
            successor = self.minimum(node_to_delete.right)
            original_color = successor.color
            successor_left = successor.left
            if successor.parent == node_to_delete:
                successor_left.parent = successor
            else:
                self.transplant(successor, successor.right)
                successor.right = node_to_delete.right
                successor.right.parent = successor
            self.transplant(node_to_delete, successor)
            successor.left = node_to_delete.left
            successor.left.parent = successor
            successor.color = node_to_delete.color

        if original_color == 'black':
            self.fix_delete(successor_left)

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL_LEAF:
            node = node.left
        return node

    def fix_delete(self, node):
        while node != self.root and node.color == 'black':
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.left_rotate(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == 'black' and sibling.right.color == 'black':
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.right.color == 'black':
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self.right_rotate(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    sibling.right.color = 'black'
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.right_rotate(node.parent)
                    sibling = node.parent.left
                if sibling.right.color == 'black' and sibling.left.color == 'black':
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.left.color == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.left_rotate(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    sibling.left.color = 'black'
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = 'black'

    def inorder(self, node):
        if node != self.NIL_LEAF:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def display(self):
        self.inorder(self.root)
        print()
