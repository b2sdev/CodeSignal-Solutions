def solution(inputArray, elemToReplace, substitutionElem):
    result = []
    for k in inputArray:
        if k == elemToReplace:
            result.append(substitutionElem)
        else:
            result.append(k)
    return result


assert solution([1, 2, 1], 1, 3) == [3, 2, 3]
