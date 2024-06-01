from collections import deque
import pytest


def test_checkPalindrom():
    def solution(inputString):
        size = len(inputString)
        i, j = 0, size - 1
        while i < j:
            print(inputString[i], inputString[j])
            if inputString[i] != inputString[j]:
                return False
            i += 1
            j -= 1
        return True

    assert solution("a") == True
    assert solution("aa") == True
    assert solution("aabaa") == True
    assert solution("aaabaaaa") == False


def test_adjacentElementsProduct():
    def solution(inputArray):
        max_product = float("-inf")
        for i in range(1, len(inputArray)):
            max_product = max(max_product, inputArray[i - 1] * inputArray[i])
        return max_product

    assert solution([3, 6, -2, -5, 7, 3]) == 21


def test_shapeArea():
    def solution(n):
        memo = [0] * (n + 1)
        memo[0] = 1
        for k in range(1, n + 1):
            memo[k] = (k - 1) * 4 + memo[k - 1]
        return memo[n]

    assert solution(1) == 1
    assert solution(2) == 5
    assert solution(3) == 13


def test_MakeArrayConsecutive2():
    def solution(statues):
        needed = []
        sorted_statues = sorted(statues)
        for i in range(1, len(sorted_statues)):
            diff = sorted_statues[i] - sorted_statues[i - 1]
            if diff == 1:
                continue
            diff -= 1
            while diff:
                needed.append(sorted_statues[i] - 1)
                diff -= 1
        return len(needed)

    assert solution([6, 2, 3, 8]) == 3  # 4, 5, and 7


def test_almostIncreasingSequence():
    def solution(sequence):
        failed = 0
        for i in range(1, len(sequence)):
            if sequence[i] <= sequence[i - 1]:
                failed += 1
                if failed > 1 or (
                    i > 1
                    and i < len(sequence) - 1
                    and sequence[i] <= sequence[i - 2]
                    and sequence[i + 1] <= sequence[i - 1]
                ):
                    return False
        return True

    assert solution([1, 3, 2, 1]) == False
    assert solution([1, 3, 2]) == True
    assert solution([1, 2, 1, 2]) == False
    assert solution([3, 6, 5, 8, 10, 20, 15]) == False
    assert solution([10, 1, 2, 3, 4, 5]) == True
    assert solution([0, -2, 5, 6]) == True


def test_matrixElementsSum():
    # https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr
    def solution(matrix):
        total_sum = 0
        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                if matrix[row][col] == 0:
                    break
                total_sum += matrix[row][col]
        return total_sum

    assert solution([[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]) == 9
    assert solution([[1, 1, 1, 0], [0, 5, 0, 1], [2, 1, 3, 10]]) == 9


def test_AllLongestString():
    def solution(inputArray):
        max_length = max(map(len, inputArray))
        return list(filter(lambda x: len(x) == max_length, inputArray))

    assert solution(["aba", "aa", "ad", "vcd", "aba"]) == ["aba", "vcd", "aba"]


def test_commonCharacterCount():
    def solution(s1, s2):
        count = 0
        for char in set(s1):
            count += min(s1.count(char), s2.count(char))
        return count

        assert solution("aabcc", "adcaa") == 3


def test_isLucky():
    def solution(n):
        num = str(n)
        mid = len(num) // 2
        left_num = sum(map(int, num[:mid]))
        right_num = sum(map(int, num[mid:]))
        return left_num == right_num

    assert solution(1230) == True
    assert solution(239017) == False
    assert solution(134008) == True


def test_SortByHeight():
    def solution(a):
        people = sorted([x for x in a if x != -1])
        result = []
        i = 0
        for p in a:
            if p == -1:
                result.append(-1)
            else:
                result.append(people[i])
                i += 1
        return result

    assert solution([-1, 150, 190, 170, -1, -1, 160, 180]) == [
        -1,
        150,
        160,
        170,
        -1,
        -1,
        180,
        190,
    ]


def test_reverseInParentheses():
    def solution(inputString):
        while "(" in inputString:
            start = inputString.rfind("(")
            end = inputString.find(")", start)
            reverse_input = inputString[start + 1 : end][::-1]
            inputString = inputString[:start] + reverse_input + inputString[end + 1 :]
        return inputString

    assert solution("(bar)") == "rab"
    assert solution("foo(bar)baz") == "foorabbaz"
    assert solution("foo(bar(baz))blim") == "foobazrabblim"
    assert solution("foo(bar)baz(blim)") == "foorabbazmilb"
