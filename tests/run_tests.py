import sys
import os
import glob
import subprocess
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
CASES = os.path.join(ROOT, "InputsOutputs")


def main():
    inputs = sorted(glob.glob(os.path.join(CASES, "Input*.txt")))
    if not inputs:
        print("No Input*.txt files found in InputsOutputs/.")
        return

    failures = 0
    for input_path in inputs:
        n = os.path.basename(input_path).replace("Input", "").replace(".txt", "")
        expected_path = os.path.join(CASES, f"Output{n}.txt")

        if not os.path.exists(expected_path):
            print(f"[SKIP] {input_path}: no expected output yet ({expected_path})")
            continue

        # Give a throwaway temp file as main.py requires an output path.
        with tempfile.NamedTemporaryFile(mode="r", suffix=".txt", delete=False) as tmp:
            actual_output_path = tmp.name

        result = subprocess.run(
            [sys.executable, os.path.join(SRC, "main.py"),
             os.path.abspath(input_path), actual_output_path],
            capture_output=True, text=True
        )

        if result.returncode != 0:
            failures += 1
            print(f"[FAIL] {input_path} (main.py crashed)")
            print("  stderr:", result.stderr.strip())
            os.remove(actual_output_path)
            continue

        with open(actual_output_path) as f:
            actual = f.read()
        os.remove(actual_output_path)

        with open(expected_path) as f:
            expected = f.read()

        if actual.strip() == expected.strip():
            print(f"[PASS] {input_path}")
        else:
            failures += 1
            print(f"[FAIL] {input_path}")
            print("  expected:", expected.strip().replace("\n", " | "))
            print("  actual:  ", actual.strip().replace("\n", " | "))

    print(f"\n{len(inputs) - failures}/{len(inputs)} passed.")


if __name__ == "__main__":
    main()