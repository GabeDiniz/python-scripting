'''
Problem: Word Frequency Counter

Scenario (real-world):
You’re writing a feature for a blogging platform. An editor wants to see which words they use most often in their draft so they can avoid repetition. You need to write a function that takes the draft text and returns how many times each word appears. Ignore capitalization ("The" and "the" should count the same).
'''

def word_count(text: str) -> dict:
    """
    Count how many times each word appears in the given text.

    Rules:
    - Ignore capitalization (case-insensitive).
    - Words are separated by whitespace.
    - Punctuation can be left alone for now (e.g., "hat," and "hat" are different).

    Example:
    >>> word_count("The cat in the hat")
    {"the": 2, "cat": 1, "in": 1, "hat": 1}
    """
    word_count = {}
    for word in text.lower().split():
        word_count[word] = word_count.get(word, 0) + 1

    return word_count












# Tests
def test_word_count():
    assert word_count("The cat in the hat") == {
        "the": 2,
        "cat": 1,
        "in": 1,
        "hat": 1,
    }

    assert word_count("hello Hello HELLO") == {"hello": 3}

    assert word_count("one two two three three three") == {
        "one": 1,
        "two": 2,
        "three": 3,
    }

    assert word_count("") == {}

    print("✅ all tests passed!")

test_word_count()
