def safe_divide(a, b):
    try:
        num1 = int(a)
        num2 = int(b)
    except (ValueError, TypeError):
        return "Error: Please enter valid numbers."

    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except OverflowError:
        return "Error: Number is too large."
    except Exception as exc:
        return f"Unexpected error: {exc}"

    return result


if __name__ == "__main__":
    try:
        first_value = input("Enter Number 1: ")
        second_value = input("Enter Number 2: ")
        result = safe_divide(first_value, second_value)
        print(f"Division result: {result}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
    except Exception as exc:
        print(f"Unexpected error: {exc}")
