def solution(inputArray):
    operations = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i - 1]:
            diff = inputArray[i - 1] - inputArray[i] + 1
            inputArray[i] += diff
            operations += diff
    return operations


assert solution([1, 1, 1]) == 3
