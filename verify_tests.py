# Test runner; the actual solutions use only the activity syllabus.
import json
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parent
total = 0
for file in sorted(root.glob("*/tests.json")):
    for test in json.loads(file.read_text(encoding="utf-8")):
        result = subprocess.run([sys.executable, str(file.parent / "solution.py")],
                                input=test["input"], text=True, capture_output=True)
        missing = [part for part in test["expected"] if part not in result.stdout]
        if result.returncode != 0 or missing:
            print("FAIL", file.parent.name, test["name"], missing, result.stderr)
            sys.exit(1)
        print("PASS", file.parent.name, test["name"])
        total += 1
print(total, "tests passed")
