from typing import Set

IGNORE = {" ", "-"}

def is_isogram(string: str) -> bool:
    """
    Check if string is an isogram (ie: no repeats except " " and "-").
    """
    seen: Set[str] = set()
    add = seen.add
    for char in (c.lower() for c in string if c not in IGNORE):
        if char in seen:
            return False
        add(char)
    return True