def lca(root,x,y):
    if root is None:
        return None
    if root.val == x or root.val==y:
        return root
    left = lca(root.left,x,y)
    right = lca(root.right,x,y)

    if not left:
        return right
    elif not right:
        return left
    elif left and right:
        return root