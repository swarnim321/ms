class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

class Solution:
    def kthsmallest(self,root,k):
        self.k =k
        self.result = None
        self.helper(root)
        return self.result

    def helper(self,node):
        if not node:
            return 0
        self.helper(node.left)
        self.k-=1
        if self.k==0:
            self.result=node.key
            return
        self.helper(node.right)



def insert(node, key):
    # If the tree is empty,
    # return a new node
    if node == None:
        return Node(key)

        # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

        # return the (unchanged) node pointer
    return node


if __name__ == '__main__':

    # Let us create following BST
    #         50
    #       /    \
    #      30    70
    #    /  \  /  \
    #   20 40 60 80
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    k=5
    print(Solution.kthsmallest(root, k))