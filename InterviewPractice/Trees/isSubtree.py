#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t1, t2):
    def isEqual(left, right):
        if left == None and right == None:
            return True
        if right == None and left != None:
            return False
        if left == None and right != None:
            return False
        return (
            left.value == right.value
            and isEqual(left.right, right.right)
            and isEqual(left.left, right.left)
        )

    if t2 is None:
        return True
    if t1 is None:
        return False
    if isEqual(t1, t2):
        return True
    return solution(t1.left, t2) or solution(t1.right, t2)
