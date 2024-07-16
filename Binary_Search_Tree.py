class Node:

    '''
    Class Node :
    Data Members :
        - key (Item)
        - left (Left item or Left Subtree)
        - right (Right item or Right Subtree)
    '''

    def __init__(self, key):

        '''
        Initialising values of the data members
        '''

        self.key = key
        self.left = None
        self.right = None


class BST:

    '''
    Class BST :
    Data Members :
        - root (Root Node with BST)
    Member Functions :
        - insert
        - delete
        - findmin
        - parent
        - delete
        - search
        - inorder
        - preorder
        - postorder
    '''

    def __init__(self, root):

        '''
        Initialising values of the data members
        '''

        self.root = root


    def insert(self, root, key):

        '''
        Adds a node into a empty BST 
        and adds new nodes into an existing
        BST'''

        # Creating a new node for an empty BST
        if self.root is None:
            self.root = Node(key)

        # Adding a new node into an empty BST's left position
        elif key < root.key:

            # If left position of a node is empty - 
            # Create and insert a new node

            if root.left is None:
                root.left = Node(key)

            # To find an empty left position

            else:
                return self.insert(root.left, key)
        
        # Adding a new node into an empty BST's right position
        elif key > self.root.key:

            # If right position of a node is empty - 
            # Create and insert a new node

            if root.right is None:
                root.right = Node(key)

            # To find an empty right position

            else:
                return self.insert(root.right, key)

        return self.root
    

    def inorder(self, root):

        '''
        Returns the inorder traversal
        of a BST
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
        of a BST
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
        of a BST
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
    

    def search(self, root, key):

        '''
        Returns the address of the node
        if the node exists in the BST 
        None otherwise
        '''

        # If the root is None or the root
        # matches with the key - the address
        # of that node is returned
        if root is None or key == root.key:
            return root
        
        # To search the element in the left subtree
        elif key < root.key:
            return self.search(root.left, key)
        
        # To search the element in the right subtree
        elif key > root.key:
            return self.search(root.right, key)
        

    def parent(self, root, key):

        '''
        Returns the address of the parent of a node
        '''
            
        if root is not None:
            if key < root.key and root.left is not None:
                if root.left.key == key:
                    return root
                else:
                    return self.parent(root.left, key)
            if key > root.key and root.right is not None:
                if root.right.key == key:
                    return root
                else:
                    return self.parent(root.right, key)


    def findmin(self, root):

        '''
        Returns the minimum element in the given
        position of the BST - root
        '''

        if root is not None and root.left is not None:
            # Minimum element can be found in the
            # left subtree of a BST
            return self.findmin(root.left)
        return root


    def delete(self, root, key):

        '''
        Deletes the node from a BST
        '''

        # Address of the node to be deleted
        pos = self.search(root, key) 

        # Address of the parent of the node to be deleted
        par = self.parent(root, key) 
        
        if pos is not None:
            
            # Deleting the root node
            if par is None and pos.left is None and pos.right is None:
                self.root = None

            # Deleting a node with - No Child
            if pos.left is None and pos.right is None and par is not None:
                if par.left == pos:
                    par.left = None
                elif par.right == pos:
                    par.right = None

            # Deleting a node with - One Child 
            elif pos.left is not None and pos.right is None and par is not None:
                if par.left == pos:
                    par.left = pos.left
                else:
                    par.right = pos.left
            elif pos.right is not None and pos.left is None and par is not None:
                if par.left == pos:    
                    par.left = pos.right
                else:
                    par.right = pos.right
            # For the root node with only one child
            elif pos.left is not None and pos.right is None and par is None:
                self.root = pos.left
            elif pos.right is not None and pos.left is None and par is None:
                self.root = pos.right

            # Deleting a node with - Two Children
            elif pos.left is not None and pos.right is not None:
                min_element = self.findmin(pos.right)
                deleted_element = self.delete(root, min_element.key)
                pos.key = min_element.key

        return root

if __name__ == '__main__':

    b = BST(None)

    wish = ''

    while wish == '':

        choice = int(input("INSERT - 1 DELETE - 2 SEARCH - 3 PARENT - 4 INORDER - 5 PREORDER - 6 POSTORDER - 7\n -> Choice : "))
        print()

        if choice == 1:

            element = int(input("Element to insert : "))
            b.insert(b.root, element)
            print()
        
        elif choice == 2:

            element = int(input("Element to delete : "))
            b.delete(b.root, element)
            print()

        elif choice == 3:

            try:
                element = int(input("Element to search : "))
                if b.search(b.root, element).key == element:
                    print('Not Present')
            except AttributeError:
                print('Not Present')
            print()

        elif choice == 4:

            try:
                element = int(input("Parent of an element : "))
                print(b.parent(b.root, element).key)
            except AttributeError:
                print('Not Present')
            print()

        elif choice == 5:

            print(b.inorder(b.root))
            print()

        elif choice == 6:

            print(b.preorder(b.root))
            print()

        elif choice == 7:

            print(b.postorder(b.root))
            print()

        wish = input("Press Enter to continue : ")
        print()
