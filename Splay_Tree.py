class Node:

    '''
    Class Node :
    Data Members :
        - key (Item)
        - left (Left item or Left Subtree)
        - right (Right item or Right Subtree)
        - parent (Parent of a Node)
    '''

    def __init__(self, key):

        '''
        Initialising values of the data members
        '''

        self.key = key
        self.parent = None
        self.left = None
        self.right = None


class SplayTree:

    '''
    Class SplayTree :
    Data Members :
        - root (Root Node of a Splay Tree)
    Member Functions :
        - left_rotate
        - right_rotate
        - splay
        - insert
        - delete
        - search
        - inorder
        - preorder
        - postorder
    '''

    def __init__(self):

        '''
        Initialising values of the data members
        '''

        self.root = None


    def left_rotate(self, x):

        '''
        Performs left rotation
        given the address of a Node
        '''

        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None: # x is root
            self.root = y

        elif x == x.parent.left: # x is left child
            x.parent.left = y

        else: # x is right child
            x.parent.right = y

        y.left = x
        x.parent = y


    def right_rotate(self, x):

        '''
        Performs right rotation
        given the address of a Node
        '''

        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None: # x is root
            self.root = y

        elif x == x.parent.right: # x is right child
            x.parent.right = y

        else: # x is left child
            x.parent.left = y

        y.right = x
        x.parent = y


    def splay(self, node):

        '''
        Performs the splaying operation given
        the address of a Node
        '''

        while node.parent != None: # node is not root
            if node.parent == self.root: # node is child of root, one rotation
                if node == node.parent.left:
                    self.right_rotate(node.parent)
                else:
                    self.left_rotate(node.parent)

            else:
                p = node.parent
                g = p.parent # grandparent

                if node.parent.left == node and p.parent.left == p: # both are left children
                    self.right_rotate(g)
                    self.right_rotate(p)

                elif node.parent.right == node and p.parent.right == p: # both are right children
                    self.left_rotate(g)
                    self.left_rotate(p)

                elif node.parent.right == node and p.parent.left == p:
                    self.left_rotate(p)
                    self.right_rotate(g)

                elif node.parent.left == node and p.parent.right == p:
                    self.right_rotate(p)
                    self.left_rotate(g)


    def insert(self, key):

        '''
        Adds a node into a empty Splay Tree
        and adds new nodes into an existing
        Splay Tree
        '''

        y = None
        node = Node(key)
        temp = self.root
        while temp != None:
            y = temp
            if node.key < temp.key:
                temp = temp.left
            else:
                temp = temp.right

        node.parent = y

        if y == None: # newly added node is root
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        self.splay(node)


    def search(self, root, key):

        '''
        Returns the address of the node
        if the node exists in the Splay Tree
        None otherwise
        '''

        if key == root.key:
            self.splay(root)
            return root
        elif key < root.key:
            return self.search(root.left, key)
        elif key > root.key:
            return self.search(root.right, key)
        else:
            return None


    def find_max(self, root):

        '''
        Returns the maximum value
        in a Splay Tree or a
        Sub-splay tree
        '''
        while root.right != None:
            root = root.right
        return root


    def delete(self, key):

        '''
        Performs the Splay operation and
        deletes the node having the key
        from a Splay Tree
        '''
        node = self.search(self.root, key)
        self.splay(node)

        left_subtree = SplayTree()
        left_subtree.root = self.root.left
        if left_subtree.root != None:
            left_subtree.root.parent = None

        right_subtree = SplayTree()
        right_subtree.root = self.root.right
        if right_subtree.root != None:
            right_subtree.root.parent = None

        if left_subtree.root != None:
            m = left_subtree.find_max(left_subtree.root)
            left_subtree.splay(m)
            left_subtree.root.right = right_subtree.root
            self.root = left_subtree.root

        else:
            self.root = right_subtree.root


    def inorder(self, root):

        '''
        Returns the inorder traversal
        of a Splay Tree
        Left - Root - Right
        '''

        res = ""
        if root is not None:
            if root.left is not None:
                res = self.inorder(root.left)
            if root is not None:
                res += f"{root.key} "
            if root.right is not None:
                res += self.inorder(root.right)
        return res


    def preorder(self, root):

        '''
        Returns the preorder traversal
        of a Splay Tree
        Root - Left - Right
        '''

        res = ""
        if root is not None:
            if root is not None:
                res = f"{root.key} "
            if root.left is not None:
                res += self.preorder(root.left)
            if root.right is not None:
                res += self.preorder(root.right)
        return res


    def postorder(self, root):

        '''
        Returns the postorder traversal
        of a Splay Tree
        Left - Right - Root
        '''

        res = ""
        if root is not None:
            if root.left is not None:
                res = self.postorder(root.left)
            if root.right is not None:
                res += self.postorder(root.right)
            if root is not None:
                res += f"{root.key} "
        return res


if __name__ == '__main__':

    t = SplayTree()

    wish = ''

    while wish == '':

        choice = int(input("INSERT & DISPLAY - 1 SEARCH - 2 DELETE & DISPLAY - 3\n -> Choice : "))
        print()

        if choice == 1:

            element = int(input("Element to insert : "))
            t.insert(element)
            print()
            print("INORDER : ", t.inorder(t.root))
            print()
            print("PREORDER : ", t.preorder(t.root))
            print()
            print("POSTORDER : ", t.postorder(t.root))
            print()

        elif choice == 2:

            try:
                element = int(input("Element to search : "))
                if t.search(t.root, element).key == element:
                    print('Present')
            except AttributeError:
                print('Not Present')
            print()

        elif choice == 3:

            try:
                element = int(input("Element to delete : "))
                t.delete(element)
                print()
                print("INORDER : ", t.inorder(t.root))
                print()
                print("PREORDER : ", t.preorder(t.root))
                print()
                print("POSTORDER : ", t.postorder(t.root))
            except AttributeError:
                print('Not Present')
            print()

        wish = input("Press Enter to continue : ")
        print()