# Hands skyline.py a clean list of building triplets,
# and takes the driver's final skyline result and writes it to disk.
#
# Input file format (comma-delimited, one building per line):
#     H1, Lx1, Rx1
#     H2, Lx2, Rx2
#     ...
#
# Output file format (comma-delimited, one strip per line):
#     h1, x1
#     h2, x2
#     ...


from typing import List, Tuple

Building = Tuple[int, int, int]   # (H, Lx, Rx)
Strip = Tuple[int, int]           # (h, x)


def read_buildings(input_path: str) -> List[Building]:
    """
    Parse the comma-delimited input file into a list of (H, Lx, Rx)
    building triplets, sorted left to right by Lx.

    Raises:
        FileNotFoundError: if input_path does not exist.
        ValueError: if a line is malformed, has non-integer values,
                    or has Lx >= Rx (invalid rectangle).
    """
    buildings: List[Building] = []

    with open(input_path, "r", encoding="utf-8") as f:
        for line_num, raw_line in enumerate(f, start=1):
            line = raw_line.strip()
            if not line:
                continue  # skip blank lines

            parts = [p.strip() for p in line.split(",")]
            if len(parts) != 3:
                raise ValueError(
                    f"Line {line_num} in {input_path} is malformed "
                    f"(expected 'H, Lx, Rx', got: '{line}')"
                )

            try:
                h, lx, rx = int(parts[0]), int(parts[1]), int(parts[2])
            except ValueError:
                raise ValueError(
                    f"Line {line_num} in {input_path} has non-integer "
                    f"values: '{line}'"
                ) from None

            if lx >= rx:
                raise ValueError(
                    f"Line {line_num} in {input_path}: Lx ({lx}) must be "
                    f"< Rx ({rx})"
                )
            if h < 0 or lx < 0 or rx < 0:
                raise ValueError(
                    f"Line {line_num} in {input_path}: values must be "
                    f"non-negative integers"
                )

            buildings.append((h, lx, rx))

    if not buildings:
        raise ValueError(f"{input_path} contains no valid building entries.")

    buildings.sort(key=lambda b: b[1])
    return buildings


def write_skyline(output_path: str, skyline: List[Strip]) -> None:
    """Writes the final (h, x) skyline strips to output_path."""
    with open(output_path, "w", encoding="utf-8") as f:
        for height, x in skyline:
            f.write(f"{height}, {x}\n")