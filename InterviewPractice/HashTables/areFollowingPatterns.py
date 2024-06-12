def solution(strings, patterns):
    table1 = {}
    table2 = {}
    N = len(strings)
    for i in range(N):
        if strings[i] not in table1:
            table1[strings[i]] = patterns[i]
        if patterns[i] not in table2:
            table2[patterns[i]] = strings[i]
        if table1[strings[i]] != patterns[i]:
            return False
        if table2[patterns[i]] != strings[i]:
            return False
    return True


assert solution(["cat", "dog", "dog"], ["a", "b", "b"]) == True
assert solution(["cat", "dog", "doggy"], ["a", "b", "b"]) == False
assert solution(["cat", "dog", "dog"], ["a", "b", "c"]) == False
