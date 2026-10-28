
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


if __name__ == "__main__":
    string = input("Enter a string: ")

    if is_palindrome(string):
        print("The given string is a palindrome.")
    else:
        print("The given string is not a palindrome.")
