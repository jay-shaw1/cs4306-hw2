# Time Complexity: O(n log n)
# The building list is recursively divided in half, creating log(n) levels
# of recursion. At each level, every building (or skyline point) is processed
# once during the merge step, resulting in O(n) work per level.
# Therefore, the overall time complexity is O(n log n).

def find_skyline(buildings):

    # This will recursively find the syline produced by a list of buildings

    # Base case

    if not buildings:
        return []

    # Base case number 2

    if len(buildings) == 1:
        height, left_x, right_x = buildings[0]

        return [
            (height, left_x),
            (0, right_x)
        ]
    
     # Find the middle index of the building list.

    midpoint = len(buildings) // 2

    # Divide the buildings into two smaller groups.

    left_buildings = buildings[:midpoint]
    right_buildings = buildings[midpoint:]

    # Recursively find the skyline of each half.

    left_skyline = find_skyline(left_buildings)
    right_skyline = find_skyline(right_buildings)

    # Combine both completed skylines.

    return merge_skylines(left_skyline, right_skyline)