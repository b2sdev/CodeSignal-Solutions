def solution(upSpeed, downSpeed, desiredHeight):
    dayHeight = 0
    nightHeight = 0
    days = 0
    while True:
        dayHeight = nightHeight + upSpeed
        nightHeight = dayHeight - downSpeed
        days += 1
        if dayHeight >= desiredHeight:
            break
    return days


assert solution(100, 10, 910) == 10
assert solution(10, 9, 4) == 1
