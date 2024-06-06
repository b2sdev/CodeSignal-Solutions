def solution(inputString):
    A = inputString.split(".")
    if len(A) != 4:
        return False
    for i in range(len(A)):
        if len(A[i]) == 0:
            return False
        if not A[i].isnumeric():
            return False
        if len(A[i]) > 1 and A[i][0] == "0":
            return False
        num = int(A[i])
        if num < 0 or num > 255:
            return False
    return True


assert solution("172.16.254.1") == True
assert solution("172.316.254.1") == False
assert solution(".254.255.0") == False
assert solution("1.1.1.1a") == False
assert solution("64.233.161.00") == False
assert solution("01.233.161.131") == False
