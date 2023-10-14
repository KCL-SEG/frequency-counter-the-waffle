"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items : list[str]):
    frequencies : dict[str, int] = dict()
    for item in items:
        item = str(item)
        if item not in frequencies.keys():
            frequencies[item] = 1
        else:
            frequencies[item] += 1
    return frequencies
