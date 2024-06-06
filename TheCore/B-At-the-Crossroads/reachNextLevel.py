def solution(experience, threshold, reward):
    return experience + reward >= threshold


assert solution(10, 15, 5) == True
assert solution(10, 15, 4) == False
