from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

code = """
    def is_palindrome(s: str) -> bool:

    Checks if a given string is a palindrome.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
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
"""
splitter =  RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)
chunks = splitter.split_text(code)

print(chunks[0])