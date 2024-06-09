def solution(names):
    seen = {}
    result = []

    for name in names:
        if name not in seen:
            seen[name] = 1
            result.append(name)
        else:
            new_name = name
            k = seen[name]
            while new_name in seen:
                new_name = f"{name}({k})"
                k += 1
            seen[name] = k
            seen[new_name] = 1
            result.append(new_name)

    return result


assert solution(["doc", "doc", "image", "doc(1)", "doc"]) == [
    "doc",
    "doc(1)",
    "image",
    "doc(1)(1)",
    "doc(2)",
]
assert solution(["a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]) == [
    "a(1)",
    "a(6)",
    "a",
    "a(2)",
    "a(3)",
    "a(4)",
    "a(5)",
    "a(7)",
    "a(8)",
    "a(9)",
    "a(10)",
    "a(11)",
]
