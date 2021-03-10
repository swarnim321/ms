def height(root):
    if root is None:
        return 0
    return 1+ max(height(root.left) , height(root.right))

def diameter(root):
    if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)
    return max(lheight + rheight +1 , max(ldiameter , rdiameter))