def function_with_uncommon_bug(x):
    try:
        result = 1 / x
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid input type")
        return None
    return result

# Example usage demonstrating the bug:
print(function_with_uncommon_bug(2))  # Output: 0.5
print(function_with_uncommon_bug(0))  # Output: Error: Cannot divide by zero, None
print(function_with_uncommon_bug("a")) # Output: Error: Invalid input type, None