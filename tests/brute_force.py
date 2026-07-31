# Used to cross-check the real O(n log n)
# divide-and-conquer solution in src/skyline.py + src/merge.py.
#
# Approach:
#     For every x-coordinate where a building starts or ends, the
#     skyline's height at that x is the tallest building that covers it.
#     We scan all such x-coordinates left to right, and only emit a new
#     strip when the tallest-covering-height actually changes.
#
# Time complexity: O(n^2)
# For each of the up to 2n candidate x-coordinates, we scan all n buildings 
# to find the max height covering that point.

import os
import random
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

Building = Tuple[int, int, int]  # (H, Lx, Rx)
Strip = Tuple[int, int]          # (h, x)


def brute_force_skyline(buildings: List[Building]) -> List[Strip]:

    if not buildings:
        return []

    candidate_xs = sorted(set(
        [b[1] for b in buildings] + [b[2] for b in buildings]
    ))

    strips: List[Strip] = []
    for x in candidate_xs:
        # A building covers x if its left edge is <= x and its right edge is > x
        height = max(
            (h for h, lx, rx in buildings if lx <= x < rx),
            default=0
        )

        if not strips or strips[-1][0] != height:
            strips.append((height, x))

    return strips



def random_buildings(n: int, max_coord: int = 100, max_height: int = 50,
                      seed: int = None) -> List[Building]:

# Generates n random, left-to-right, non-degenerate buildings for stress testing.
    if seed is not None:
        random.seed(seed)

    buildings = []
    for _ in range(n):
        lx = random.randint(0, max_coord - 1)
        rx = random.randint(lx + 1, max_coord)  # guarantees Lx < Rx
        h = random.randint(1, max_height)
        buildings.append((h, lx, rx))

    buildings.sort(key=lambda b: b[1])  # left to right
    return buildings


def _run_against_saved_inputs():

# Compares the real algorithm against brute force on every InputsOutputs/InputN.txt file
    from io_utils import read_buildings
    from skyline import find_skyline
    import glob

    inputs_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "InputsOutputs"
    )
    input_files = sorted(glob.glob(os.path.join(inputs_dir, "Input*.txt")))

    if not input_files:
        print("No InputsOutputs/Input*.txt files found.")
        return

    failures = 0
    for path in input_files:
        buildings = read_buildings(path)
        real = find_skyline(buildings)
        brute = brute_force_skyline(buildings)
        ok = real == brute
        status = "MATCH" if ok else "MISMATCH"
        print(f"[{status}] {os.path.basename(path)}")
        if not ok:
            failures += 1
            print(f"    real:  {real}")
            print(f"    brute: {brute}")

    print(f"\n{len(input_files) - failures}/{len(input_files)} matched brute force.")


def _run_random_stress_test(trials: int = 200, max_buildings: int = 12):

# Generates random building sets and checks the real algorithm against brute force on each one.
    from skyline import find_skyline

    for trial in range(trials):
        n = random.randint(1, max_buildings)
        buildings = random_buildings(n, seed=trial)
        real = find_skyline(buildings)
        brute = brute_force_skyline(buildings)
        if real != brute:
            print(f"MISMATCH on trial {trial} with buildings={buildings}")
            print(f"  real:  {real}")
            print(f"  brute: {brute}")
            return
    print(f"All {trials} random trials matched brute force. "
          f"(up to {max_buildings} buildings each)")


if __name__ == "__main__":
    print("\nComparing against saved InputsOutputs test cases: ")
    _run_against_saved_inputs()
    print("\nStress test: ")
    _run_random_stress_test()