def solution(commands):
    count = 0
    status = 0
    for command in commands:
        if command == "L" or command == "R":
            status += 1
        if status % 2 == 0:
            count += 1
    return count


assert solution("LLARL") == 3
