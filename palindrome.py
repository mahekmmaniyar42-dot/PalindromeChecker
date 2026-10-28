import sys

def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        string = " ".join(sys.argv[1:])
    else:
        string = input("Enter a string: ")

    if is_palindrome(string):
        print(f"'{string}' is a palindrome.")
    else:
        print(f"'{string}' is not a palindrome.")

