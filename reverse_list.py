# Author: Lily Timmermans
# GitHub username: LilyTimmermans
# Date: 07/31/2023
# Description: This code reverses the order of the list.

def reverse_list(lst):
    """
    Reverse the order of elements in the given list.

    Args:
        lst (list): Reverse the elements of this list. The original list will be modified in-place.

    Returns:
        None
    """
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
