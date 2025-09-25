'''
Problem: Balanced Parentheses Checker

Scenario (real-world):
You’re working on a simple text editor. Before saving, it checks that parentheses and brackets are balanced (so the code compiles). Write a function that returns True if all parentheses/brackets are balanced and False otherwise.
'''

def is_balanced(s: str) -> bool:
    """
    Check if the string has balanced (), [], and {} brackets.

    Rules:
    - Every opening bracket must have a matching closing bracket.
    - Brackets must close in the correct order.

    Examples:
    >>> is_balanced("(())[]{}")
    True
    >>> is_balanced("([)]")
    False
    >>> is_balanced("()[]{}")
    True
    >>> is_balanced("(")
    False
    """
    stack = []
    bracket_pairs = {
                        "(": ")",
                        "[": "]",
                        "{": "}"
                    }

    for current_bracket in s:
        print(stack, current_bracket)
        # Check if its an open bracket (if yes, append)
        if current_bracket in bracket_pairs:
            stack.append(current_bracket)
        # Must be a closed bracket, remove last if it matches
        elif stack and current_bracket == bracket_pairs[stack[-1]]:
            stack.pop()
        else:
            print("COMPLETE\n")
            return False
    print("COMPLETE\n")
    return not stack




def test_is_balanced():
    assert is_balanced("(())[]{}") == True
    assert is_balanced("([)]") == False
    assert is_balanced("()[]{}") == True
    assert is_balanced("(") == False
    assert is_balanced("") == True
    assert is_balanced("{[()]}") == True
    assert is_balanced("{[(])}") == False

    print("✅ all tests passed!")

print(1%2)
test_is_balanced()
