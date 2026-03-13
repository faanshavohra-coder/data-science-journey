def calculate_check_digit_10(isbn):
    total = 0
    for i in range(9):
        total += (i + 1) * int(isbn[i])
    check = total % 11
    return "X" if check == 10 else str(check)

def calculate_check_digit_13(isbn):
    total = 0
    for i in range(12):
        factor = 1 if i % 2 == 0 else 3
        total += factor * int(isbn[i])
    check = (10 - (total % 10)) % 10
    return str(check)

def validate_isbn(isbn, length):
    if length == 10:
        if len(isbn) != 10:
            return "ISBN-10 code should be 10 digits long."
        try:
            check_digit = calculate_check_digit_10(isbn)
        except ValueError:
            return "Invalid character was found."
        return "Valid ISBN Code." if isbn[-1] == check_digit else "Invalid ISBN Code."
    elif length == 13:
        if len(isbn) != 13:
            return "ISBN-13 code should be 13 digits long."
        try:
            check_digit = calculate_check_digit_13(isbn)
        except ValueError:
            return "Invalid character was found."
        return "Valid ISBN Code." if isbn[-1] == check_digit else "Invalid ISBN Code."
    else:
        return "Length should be 10 or 13."

def main():
    try:
        user_input = input("Enter ISBN and length: ")
        isbn, length = user_input.split(",")
    except ValueError:
        print("Enter comma-separated values.")
        return

    try:
        length = int(length)
    except ValueError:
        print("Length must be a number.")
        return

    if not isbn[:-1].isdigit() and length == 10:
        print("Invalid character was found.")
        return
    if not isbn[:-1].isdigit() and length == 13:
        print("Invalid character was found.")
        return

    print(validate_isbn(isbn, length))

# Comment out the following line when running tests:
# main()
