def solution(score1, score2):
    A = [max(score1, score2), min(score1, score2)]
    if A[0] == 6 and A[1] < 5:
        return True
    elif A[0] == 7 and 5 <= A[1] < 7:
        return True
    return False


assert solution(3, 6) == True
assert solution(8, 5) == False
assert solution(6, 5) == False
assert solution(7, 7) == False
assert solution(7, 6) == True
assert solution(7, 5) == True
assert solution(7, 2) == False
assert solution(4, 10) == False
