import os
import subprocess
import unittest


class TestBBCalc(unittest.TestCase):
    def test_happy_case(self):
        original_stdout = """-----
HP = 100, Helmet = 120, Armor = 95
Death in 3.33949 hits on average.
StDev: 0.5017958328748644
% Hits to die: [(2, 1.2309999999999999), (3, 63.736000000000004), (4, 34.886), (5, 0.147)]
First injury in 2.47364 hits on average.
Chance of first heavy injury in 2.8984 hits on average.
-----
"""
        with subprocess.Popen(
                ['python', '../web/python/BBCalc.py'],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                env={**os.environ, 'TEST': ''}
        ) as p:
            stdout = p.stdout.read().decode('utf-8')
            self.maxDiff = None
            self.assertEqual(original_stdout, stdout)
