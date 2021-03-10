class longest_binary:
    def function(node):
        max = 1
        longest_common_binary(self,node,0,0,max)
        return max

    def longest_common_binary(self,node, count, target, max ):
        if node is None:
            return
        elif node.val == target:
            count+=1
        else:
            count = 1
        max = max(max, count)
        longest_common_binary(self, node.right, count, node.val +1, max)
        longest_common_binary(self, node.left, count, node.val + 1, max)

