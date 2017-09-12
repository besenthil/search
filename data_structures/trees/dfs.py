class Node(object):
    def __init__(self,data,left_node=None,right_node=None):
        self.data = data
        self.left_node =left_node
        self.right_node=right_node

TRAVERSAL = 'INORDER'

class BST(object):
    def __init__(self,root=None):
        self.root=root

    def __inorder_traversal(self,root,node):
        pointer = root
        if node.data < pointer.data and pointer.left_node is None:
            pointer.left_node = node
            return True

        if node.data > pointer.data and pointer.right_node is None:
            pointer.right_node = node

        if node.data < pointer.data and pointer.left_node is not None:
            self.__inorder_traversal(pointer.left_node,node)

        if node.data > pointer.data  and pointer.right_node is not None:
                self.__inorder_traversal(pointer.right_node,node)

    def __preorder_traversal(self,root,node):
        pointer = root
        if root:
            print (pointer.data)
            self.__preorder_traversal(pointer.left_node,node)
            self.__preorder_traversal(pointer.right_node,node)

    def __postorder_traversal(self,root,node):
        pointer = root
        if pointer:
            self.__postorder_traversal(pointer.left_node,node)
            self.__postorder_traversal(pointer.right_node,node)
            print (pointer.data)


    def traverse(self,node,traversal):
        if node is None:
            return False

        if traversal == 'INORDER':
            self.__inorder_traversal(self.root,node)
        if traversal == 'PREORDER':
            self.__preorder_traversal(node,node)
        if traversal == 'POSTORDER':
            self.__postorder_traversal(node,node)

    def add_node(self,node):
        self.traverse(node,'INORDER')

    def list(self,traversal):
        self.traverse(self.root,traversal)

    def find_common_ancestor(self,root,node1,node2):
        print (root.data,node1.data,node2.data)
        if node1.data < root.data and node2.data < root.data:
            return self.find_common_ancestor(root.left_node,node1,node2)
        if node1.data > root.data and node2.data > root.data:
            return self.find_common_ancestor(root.right_node,node1,node2)
        else:
            return root.data




if __name__ == "__main__":
    n1 = Node(20)
    n2 = Node(8)
    n3 = Node(22)
    n4 = Node(4)
    n5 = Node(12)
    n6 = Node(10)
    n7 = Node(14)
    n8 = Node(24)
    g = BST(n1)
    g.add_node(n1)
    g.add_node(n2)
    g.add_node(n3)
    g.add_node(n4)
    g.add_node(n5)
    g.add_node(n6)
    g.add_node(n7)
    g.add_node(n8)
    #g.list('PREORDER')
    #g.list('POSTORDER')
    print (g.find_common_ancestor(n1,n7,n8))


