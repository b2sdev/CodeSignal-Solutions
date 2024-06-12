def solution(queries):
    items = []
    result = []
    for query, value in queries:
        if query == "ADD":
            items.append(value)
            result.append("")
        elif query == "EXISTS":
            try:
                index = items.index(value)
                result.append("true")
            except:
                result.append("false")
        elif query == "REMOVE":
            try:
                index = items.index(value)
                del items[index]
                result.append("true")
            except:
                result.append("false")
    return result


queries = [
    ["ADD", "1"],
    ["ADD", "2"],
    ["ADD", "5"],
    ["ADD", "2"],
    ["EXISTS", "2"],
    ["EXISTS", "5"],
    ["EXISTS", "1"],
    ["EXISTS", "4"],
    ["EXISTS", "3"],
    ["EXISTS", "0"],
]
assert solution(queries) == [
    "",
    "",
    "",
    "",
    "true",
    "true",
    "true",
    "false",
    "false",
    "false",
]
queries = [
    ["ADD", "1"],
    ["ADD", "2"],
    ["ADD", "2"],
    ["ADD", "3"],
    ["EXISTS", "1"],
    ["EXISTS", "2"],
    ["EXISTS", "3"],
    ["REMOVE", "2"],
    ["REMOVE", "1"],
    ["EXISTS", "2"],
    ["EXISTS", "1"],
]
assert solution(queries) == [
    "",
    "",
    "",
    "",
    "true",
    "true",
    "true",
    "true",
    "true",
    "true",
    "false",
]
