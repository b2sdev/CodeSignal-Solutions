def solution(address):
    return address.split("@")[-1]


assert solution("prettyandsimple@example.com") == "example.com"
assert solution("fully-qualified-domain@codesignal.com") == "codesignal.com"
assert (
    solution('"very.(),:;<>[]".VERY."very@\\ "very".unusual"@strange.example.com')
    == "strange.example.com"
)
