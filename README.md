# Uncommon Error Handling in Python Function

This repository demonstrates a subtle error in exception handling within a Python function.  The function `function_with_uncommon_bug` attempts to divide 1 by an input value, handling both `ZeroDivisionError` and `TypeError`.  However, while it prints error messages, it returns `None` in both cases, making it difficult to distinguish between these types of errors. This lack of granularity in error reporting can complicate debugging and error handling in larger applications.

The `bugSolution.py` file offers an improved version that provides more informative error handling through custom exceptions or by returning a more descriptive error code.