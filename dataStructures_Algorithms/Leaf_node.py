def lefttoright(root):
    s1=[]
    s2=[]
    s1.append(root)
    while len(s1)!=0:
        curr = s1.pop()
        if curr.left:
            s1.append(curr.left)
        if curr.right:
            s1.append(curr.right)
        elif not curr.left and not curr.right:
            s2.append(curr)

    while len(s2)!=0:
        curr=s2.pop()
        print(curr.data)