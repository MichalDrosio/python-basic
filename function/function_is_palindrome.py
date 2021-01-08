def is_palindrome(words):
    words = words.lower()
    inverse = words[::-1]
    if words == inverse:
        return True
    else:
        return False

print(is_palindrome('kAjak'))