def solution(fileSystem):
    max_length = 0
    path_length = {0: 0}

    for file in fileSystem.split("\f"):
        depth = file.count("\t")
        name_length = len(file) - depth

        if "." in file:
            # 패스를 다 만듦
            max_length = max(max_length, path_length[depth] + name_length)
        else:
            # 패스를 만드는 중
            path_length[depth + 1] = path_length[depth] + name_length + 1

    return max_length


assert solution("user\f\tpictures\f\tdocuments\f\t\tnotes.txt") == 24
assert (
    solution(
        "user\f\tpictures\f\t\tphoto.png\f\t\tcamera\f\tdocuments\f\t\tlectures\f\t\t\tnotes.txt"
    )
    == 33
)
assert solution("a\f\tb\f\t\tc") == 0
