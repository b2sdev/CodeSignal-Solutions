def solution(level, pos):
    if level == 1:
        return "Engineer"
    if solution(level - 1, (pos + 1) // 2) == "Doctor":
        return "Doctor" if pos % 2 else "Engineer"
    return "Engineer" if pos % 2 else "Doctor"
