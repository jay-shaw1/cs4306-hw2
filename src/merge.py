# Given two already-correct skylines (each covering a left/right half of
# the building list), combines them into one skyline covering the whole
# range, but instead of merging two sorted lists of values, we're merging 
# two sorted lists of (height, x) strips and tracking the max height 
# contributed by each side at every x-coordinate where either skyline changes.

from typing import List, Tuple

Strip = Tuple[int, int]  # (h, x)


def merge_skylines(left: List[Strip], right: List[Strip]) -> List[Strip]:

    i = j = 0
    left_h = right_h = 0
    merged: List[Strip] = []

    while i < len(left) and j < len(right):
        lh, lx = left[i]
        rh, rx = right[j]

        if lx < rx:
            # Left skyline changes first; only its height updates.
            x = lx
            left_h = lh
            i += 1
        elif rx < lx:
            # Right skyline changes first; only its height updates.
            x = rx
            right_h = rh
            j += 1
        else:
            # Both skylines change at the same x — advance both pointers.
            x = lx
            left_h = lh
            right_h = rh
            i += 1
            j += 1

        h = max(left_h, right_h)

        # Only emit a new strip if the combined height actually changed;

        if not merged or merged[-1][0] != h:
            merged.append((h, x))

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged