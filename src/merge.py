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