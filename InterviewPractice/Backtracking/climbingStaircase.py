def solution(n, k):
  def dfs(n, k, s, res):
    if n == 0:
      res.append(s)
      return
    for i in range(1, k + 1):
      if n - i >= 0:
        dfs(n - i, k, s + [i], res)
  res = []
  dfs(n, k, [], res)
  return res

assert solution(4, 2) == [[1, 1, 1, 1],
 [1, 1, 2],
 [1, 2, 1],
 [2, 1, 1],
 [2, 2]]

