def solution(inputArray, elemToReplace, substitutionElem):
    result = []
    for elem in inputArray:
        if elem == elemToReplace:
            result.append(substitutionElem)
        else:
            result.append(elem)
    return result


assert solution([1, 2, 1], 1, 3) == [3, 2, 3]
