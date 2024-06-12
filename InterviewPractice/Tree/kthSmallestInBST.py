#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t, k):
    def traverse(n):
        if n is None:
            return []
        return traverse(n.left) + [n.value] + traverse(n.right)

    return traverse(t)[k - 1]
