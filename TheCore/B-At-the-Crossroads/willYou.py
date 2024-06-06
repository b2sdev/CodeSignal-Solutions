def solution(young, beautiful, loved):
    if young and beautiful and not loved:
        return True
    if loved and (not young or not beautiful):
        return True
    return False


assert solution(true, false, true) == true
assert solution(false, false, false) == false
