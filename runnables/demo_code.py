**Task: Palindrome of a String**
================================

### Problem Statement

A palindrome is a string that reads the same backward as forward. Write a function to check if a given string is a palindrome.

### Approach

We will use a simple approach to solve this problem. We will compare the input string with its reverse. If they are the same, then the string is a palindrome.

### Code

```python
def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove any leading or trailing whitespace
    s = s.strip()
    
    # Convert the string to lowercase to make the comparison case-insensitive
    s = s.lower()
    
    # Compare the string with its reverse
    return s == s[::-1]

# Example usage:
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("radar", True),
        ("hello", False),
        ("level", True),
        ("python", False),
        ("Madam", True)
    ]

    for test_case in test_cases:
        string, expected_result = test_case
        result = is_palindrome(string)
        print(f"Input: {string}, Expected: {expected_result}, Actual: {result}")
```

### Explanation

*   The `is_palindrome` function takes a string `s` as input and returns a boolean indicating whether the string is a palindrome or not.
*   The function first removes any leading or trailing whitespace from the input string using the `strip` method.
*   It then converts the string to lowercase using the `lower` method to make the comparison case-insensitive.
*   The function uses slicing (`s[::-1]`) to get the characters of the string in reverse order and compares them with the original string.
*   If the string is the same when reversed, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`.
*   In the example usage section, we test the function with several test cases and print the results.