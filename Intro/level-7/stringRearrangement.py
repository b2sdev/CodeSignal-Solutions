from itertools import permutations


def solution(inputArray):
    def differ_by_one_char(str1, str2):
        diff_count = sum(c1 != c2 for c1, c2 in zip(str1, str2))
        return diff_count == 1

    for perm in permutations(inputArray):
        if all(differ_by_one_char(perm[i], perm[i + 1]) for i in range(len(perm) - 1)):
            return True
    return False


assert solution(["aba", "bbb", "bab"]) == False
assert solution(["ab", "bb", "aa"]) == True
