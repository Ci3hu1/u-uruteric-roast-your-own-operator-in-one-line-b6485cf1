"""Tests for the roast entry: gate shape (1 line, <=140 chars) and determinism."""

import hashlib
import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = os.path.join(REPO, "main.py")

sys.path.insert(0, REPO)
import main as entry  # noqa: E402


class TestRoastLine(unittest.TestCase):
    def test_line_is_one_line(self):
        self.assertNotIn("\n", entry.LINE)
        self.assertNotIn("\r", entry.LINE)

    def test_line_within_140_chars(self):
        self.assertGreater(len(entry.LINE), 0)
        self.assertLessEqual(len(entry.LINE), 140)

    def test_line_not_only_whitespace(self):
        self.assertTrue(entry.LINE.strip())

    def test_line_roasts_the_operator(self):
        self.assertIn("operator", entry.LINE.lower())
        self.assertIn("2am", entry.LINE)

    def test_program_writes_entry_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "entry.txt")
            rc = subprocess.run(
                [sys.executable, MAIN, out],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(rc.returncode, 0, rc.stderr)
            with open(out, "rb") as f:
                data = f.read()
            self.assertEqual(data, entry.LINE.encode("utf-8"))
            self.assertFalse(data.endswith(b"\n"), "no trailing blank line")
            self.assertEqual(oct(os.stat(out).st_mode & 0o777), "0o644")

    def test_byte_identical_across_two_runs(self):
        with tempfile.TemporaryDirectory() as tmp:
            hashes = []
            for name in ("run1.txt", "run2.txt"):
                out = os.path.join(tmp, name)
                subprocess.run(
                    [sys.executable, MAIN, out],
                    capture_output=True, check=True,
                )
                with open(out, "rb") as f:
                    hashes.append(hashlib.sha256(f.read()).hexdigest())
            self.assertEqual(hashes[0], hashes[1])

    def test_no_third_party_imports(self):
        with open(MAIN, encoding="utf-8") as f:
            src = f.read()
        for line in src.splitlines():
            stripped = line.strip()
            if stripped.startswith("import ") or stripped.startswith("from "):
                module = stripped.split()[1].split(".")[0]
                self.assertIn(module, {"os", "sys"},
                              "only stdlib imports allowed: %s" % stripped)


if __name__ == "__main__":
    unittest.main()
