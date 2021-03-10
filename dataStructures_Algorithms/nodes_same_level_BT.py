#https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/726359/Python-Easy-understanding-solution-with-explaination
def connect(root):
    if not root:
        return None
    if root.right:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
    connect(root.left)
    connect (root.right)
    return root