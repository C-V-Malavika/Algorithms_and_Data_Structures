class BinaryTree:

    '''
    Class BinaryTree :
    Data Members :
        - root
    Member functions :
        - inorder
        - preorder
        - postorder
        - leaf_nodes
        - inner_nodes
        - huffman_code
    '''

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


    def __init__(self):

        '''
        Initialising values of the data members
        '''

        self.root = None


    def inorder(self, root):

        '''
        Returns the inorder traversal
        of a Binary Tree
        Left - Root - Right
        '''

        res = ""
        if root is not None:
            if root.left is not None:
                res = self.inorder(root.left)
            if root is not None:
                res += f"{root.key}" + "\n"
            if root.right is not None:
                res += self.inorder(root.right)
        return res


    def preorder(self, root):

        '''
        Returns the preorder traversal
        of a Binary Tree
        Root - Left - Right
        '''

        res = ""
        if root is not None:
            if root is not None:
                res = f"{root.key}" + "\n"
            if root.left is not None:
                res += self.preorder(root.left)
            if root.right is not None:
                res += self.preorder(root.right)
        return res


    def postorder(self, root):

        '''
        Returns the postorder traversal
        of a Binary Tree
        Left - Right - Root
        '''

        res = ""
        if root is not None:
            if root.left is not None:
                res = self.postorder(root.left)
            if root.right is not None:
                res += self.postorder(root.right)
            if root is not None:
                res += f"{root.key}" + "\n"
        return res


    def leaf_nodes(self, root, res = []):

        '''
        Returns the leaf nodes of the
        binary tree
        '''

        if root is not None:
            if root.left is not None:
                self.leaf_nodes(root.left, res)
            if root.left is None and root.right is None:
                res.append(root.key)
            if root.right is not None:
                self.leaf_nodes(root.right, res)
        return res
    

    def inner_nodes(self, node):

        '''
        Returns the inner nodes of the
        binary tree
        '''

        list_full_nodes = [item for item in self.inorder(self.root).split('\n') if item != ''] # All nodes
        list_leaf_nodes = [item for item in self.leaf_nodes(self.root).split('\n') if item != ''] # Leaf nodes
        res_list = [item for item in list_full_nodes if item not in list_leaf_nodes] # Nodes which are not leaf nodes

        return res_list


    def huffman_code(self, root, string = '', d = {}):

        '''
        Return the huffman coded dictionary
        '''

        if root is None:
            return
        elif root.key in self.leaf_nodes(self.root):
            d[root.key[0]] = string

        self.huffman_code(root.left, string + '0', d)
        self.huffman_code(root.right, string + '1', d)

        return d


    def decode(self, root, string):

        '''
        Decodes a huffman coded string
        using the tree constructed
        '''

        res = ''
        curr = root

        for item in string:
            if item == '0':
                curr = curr.left
            elif item == '1':
                curr = curr.right

            if curr.left is None and curr.right is None:
                res += str(curr.key[0])
                curr = root
        return res


class BinaryHeap:

    '''
    Class BinaryHeap:
    Data Members :
        - heap
    Member functions :
        - insert
        - isempty
        - min_element
    '''

    def __init__(self):

        '''
        Initialising values of the data members
        '''

        self.heap = []


    def insert(self, node):

        '''
        Inserts a node into the binary heap
        '''

        self.heap.append(node)


    def isempty(self):

        '''
        Returns True if the heap has
        only one element
        '''

        return len(self.heap) == 1


    def min_element(self):

        '''
        Returns the minimum element
        from the binary heap
        '''

        lst_nodes = [] # List of nodes of the binary tree
        lst_tree = [] # List of binary trees created by combining the nodes

        # Creating the list of nodes and list of binary trees
        for item in self.heap:
            try:
                if item.left is None and item.right is None:
                    lst_nodes.append(item)
            except AttributeError:
                lst_tree.append(item)

        # Sorting the list of nodes and list of trees based
        # on the key or the frequency of characters so that
        # the element at 0th index will be the minimum element
        lst_nodes.sort(key = lambda item : item.key[1])
        lst_tree.sort(key = lambda item : item.root.key)

        if (len(lst_tree) != 0 and len(lst_nodes) != 0) and (lst_nodes[0].key[1] <= lst_tree[0].root.key):
            self.heap.remove(lst_nodes[0])
            item = lst_nodes.pop(0)
            return item

        elif len(lst_tree) == 0:
            self.heap.remove(lst_nodes[0])
            item = lst_nodes.pop(0)
            return item

        else:
            self.heap.remove(lst_tree[0])
            item = lst_tree.pop(0)
            return item.root


def frequency(string):

    '''
    This function gives the frequency
    of the characters as a dictionary with
    Key - Character
    Value - Frequency of the character
    '''

    d = {}

    for item in string:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1

    return d


def encoding(string, dict):

    '''
    Returns the encoded version of the string
    with the help of the Huffman code
    '''

    encode = ''
    for char in string:
        encode += dict[char]
    return encode


def main(string):

    d = frequency(string) # Compute the frequency dictionary

    d = dict(sorted(d.items(), key = lambda item: item[1])) # Sort based on frequency
    d = dict(sorted(d.items(), key = lambda item: item[0])) # Sort based on character

    b = BinaryTree()
    B = BinaryHeap()

    for item in d:
        B.insert(b.Node((item, d[item])))

    while not(B.isempty()):

        # Finding two minimum elements from the heap
        left = B.min_element()
        right = B.min_element()

        b1 = BinaryTree()
        try:
            key = left.key[1] + right.key[1] # If both left and right are nodes
        except TypeError:
            try:
                key = left.key + right.key # If both left and right are binary trees
            except TypeError:
                try:
                    key = left.key + right.key[1] # If left is a binary tree and right is a node
                except TypeError:
                    key = left.key[1] + right.key # If left is a node and right is a binary tree

        # Creating the binary tree
        b1.root = b1.Node(key)
        b1.root.left = left
        b1.root.right = right

        B.insert(b1) # Inserting the tree to the heap

    b = B.heap[0] # Take the element if 0th index - Complete binary tree
    dic = b.huffman_code(b.root) # Find the huffman code for that tree

    dict_char_code = {}

    for item in dic:
        dict_char_code[item] = dic[item]

    print("Original string is :", string)
    print()
    
    print("Huffman Code Dictionary : ", dict_char_code)
    print()

    print("Encoding of the string is :", encoding(string, dict_char_code))
    print()

    print("Decoded string is :", b.decode(b.root, encoding(string, dict_char_code)))


if __name__ == '__main__':

    print("CASE - 1")
    print("--------")
    print()

    string = "MMNNNOOOOOO"
    main(string)
    print()

    print("CASE - 2")
    print("--------")
    print()

    string = "BCAADDDCCACACAC"
    main(string)
    print()

    print("CASE - 3")
    print("--------")
    print()

    string = "this is an example of a huffman tree"
    main(string)
    print()

    print("CASE - 4")
    print("--------")
    print()

    string = 'a' * 5 + 'b' * 9 + 'c' * 12 + 'd' * 13 + 'e' * 16 + 'f' * 45
    main(string)
    print()

    print("CASE - 5")
    print("--------")
    print()

    string = "THIS IS COMMUNICATION ENGINEERING"
    main(string)
    print()