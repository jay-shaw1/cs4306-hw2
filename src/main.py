import sys
import os
from io_utils import read_buildings, write_skyline
from skyline import find_skyline


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <absolute_input_path> <absolute_output_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.isabs(input_path) or not os.path.isabs(output_path):
        print("Error: both input and output paths must be absolute paths.")
        sys.exit(1)

    buildings = read_buildings(input_path)
    skyline = find_skyline(buildings)
    write_skyline(output_path, skyline)

    print(f"Skyline written to {output_path} ({len(skyline)} strips).")


if __name__ == "__main__":
    main()