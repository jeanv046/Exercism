from typing import List

def latest(scores: List[int]) -> int:
    """Extract the latest score."""
    return scores[-1]

def personal_best(scores: List[int]) -> int:
    """Extract the best score."""
    return max(scores)
    
def personal_top_three(scores: List[int]) -> List[int]:
    """Extract the top three best scores."""
    return sorted(scores, reverse=True)[:3]