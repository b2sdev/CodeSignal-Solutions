def solution(t):
    def traverse(node, prev, res):
        curr = prev + str(node.value)
        if node.left is None and node.right is None:
            res.append(int(curr))
            return
        if node.left:
            traverse(node.left, curr, res)
        if node.right:
            traverse(node.right, curr, res)

    result = []
    traverse(t, "", result)
    return sum(result)
