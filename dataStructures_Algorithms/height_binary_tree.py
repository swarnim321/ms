def height(root):
    if root is None:
        return 0
    hleft=height(root.left)
    hright= height(root.right)

    if hleft>hright:
        return hleft+1
    else:
        return hright+1