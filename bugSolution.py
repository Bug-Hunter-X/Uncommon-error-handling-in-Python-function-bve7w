from typing import Union

class InvalidInputError(Exception):
    """Custom exception for invalid input type"""
    pass

class DivisionByZeroError(Exception):
    """Custom exception for division by zero"""
    pass


def improved_function(x: Union[int, float]) -> Union[float, tuple[str, int]]:
    try:
        if not isinstance(x, (int, float)):
            raise InvalidInputError("Invalid input type")
        if x == 0:
            raise DivisionByZeroError("Cannot divide by zero")
        return 1 / x
    except InvalidInputError as e:
        return str(e), 1
    except DivisionByZeroError as e:
        return str(e), 2
    except Exception as e:  #Handle other unexpected errors
        return str(e), 3

# Example usage of the improved function:
print(improved_function(2))  # Output: 0.5
print(improved_function(0))  # Output: ("Cannot divide by zero", 2)
print(improved_function("a"))  # Output: ("Invalid input type", 1) 
print(improved_function(-1)) # Output: -1.0