#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t, s):
    def traverse(node, curr):
        if not node:
            return curr == 0

        if node.left and node.right:
            return any(
                [
                    traverse(node.left, curr - node.value),
                    traverse(node.right, curr - node.value),
                ]
            )
        elif node.left:
            return traverse(node.left, curr - node.value)
        elif node.right:
            return traverse(node.right, curr - node.value)
        else:
            return node.value == curr

    return traverse(t, s)
