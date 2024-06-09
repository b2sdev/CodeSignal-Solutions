def solution(time):
    HH, MM = time.split(":")
    return int(HH) < 24 and int(MM) < 60


assert solution("13:58") == True
assert solution("25:51") == False
assert solution("12:76") == False
