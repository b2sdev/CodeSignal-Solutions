def solution(votes, k):
    max_votes = max(votes)
    max_count = votes.count(max_votes)

    if k == 0:
        return 1 if max_count == 1 else 0

    winners = 0
    for v in votes:
        if v + k > max_votes:
            winners += 1

    return winners


assert solution([2, 3, 5, 2], 3) == 2
assert solution([5, 1, 3, 4, 1], 0) == 1
