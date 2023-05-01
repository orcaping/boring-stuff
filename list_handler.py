"""Prints all values in spam seperated by commas and adds an "and" before last value."""

spam = ['apples', 'bananas', 'tofu', 'cats', 'fish', 'blob']

def list_handler(lst):
    """list handler."""
    if len(lst) == 0:
        print("sorry this list doesn't contain any values")
        return None

    return ', '.join(lst[:-1]) + ' and ' + lst[-1]

print(list_handler(spam))
