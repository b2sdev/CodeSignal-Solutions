from collections import Counter
def solution(inputString):
    sorted_set = sorted(set(inputString))
    counter = Counter(inputString)
    if sorted_set[0] != 'a':
        return False
    for i in range(1, len(sorted_set)):
        if ord(sorted_set[i]) - ord(sorted_set[i - 1]) != 1:
            return False
        if counter.get(sorted_set[i]) > counter.get(sorted_set[i - 1]):
            return False
    return True

assert solution("bbbaacdafe") == True
assert solution("aabbb") == False
assert solution("bbc") == False
assert solution("zaa") == False
