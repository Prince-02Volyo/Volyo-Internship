def solution(s):
    # Check if each character is strictly less than the next one
    for i in range(len(s) - 1):
        if s[i] >= s[i + 1]:
            return False
    return True


# Example tests
print(solution("effg"))  # False
print(solution("cdce"))  # False
print(solution("ace"))   # True
print(solution("bxz"))   # True