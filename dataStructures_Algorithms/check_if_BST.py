

def check_BST(root):
    return(helper(root , float("-inf"),float("inf")))

def helper(root , minval , maxval):
    if root is None:
        return True
    if root.val < minval or root.val > maxval:
        return False
    validRight=helper(root.right, root.val , maxval)
    validLeft=helper(root.left, minval, root.val)

    return validLeft and validRight
