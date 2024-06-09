def solution(text):
    longest = ""
    left = 0
    while left < len(text):
        while left < len(text) and not text[left].isalpha():
            left += 1
        right = left
        while right < len(text) and text[right].isalpha():
            right += 1
        if right - left > len(longest):
            longest = text[left:right]
        left += 1
    return longest


assert solution("Ready, steady, go!") == "steady"
