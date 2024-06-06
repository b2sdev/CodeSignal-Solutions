def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    return min(yourLeft, yourRight) == min(friendsLeft, friendsRight) and max(
        yourLeft, yourRight
    ) == max(friendsLeft, friendsRight)


assert solution(10, 15, 15, 10) == True
assert solution(15, 10, 15, 10) == True
assert solution(15, 10, 15, 9) == False
