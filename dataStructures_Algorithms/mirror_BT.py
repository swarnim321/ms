def mirror(root):
    if root == None:
        return
    else:

        mirror(root.right)
        mirror(root.left)
        temp = root.left
        root.left = root.right
        root.right=temp
