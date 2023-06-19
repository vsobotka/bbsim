import os
import subprocess
import unittest


class TestBBHitChance(unittest.TestCase):
    def test_happy_case(self):
        original_stdout = """-----
HP = 100, Helmet = 120, Armor = 95
Hit Chance: 50%
Death in 6.68834 swings on average.
StDev: 2.777020396260284
% Swings to die: [(2, 0.292), (3, 8.225999999999999), (4, 14.414), (5, 16.466), (6, 15.344), (7, 12.856000000000002), (8, 10.17), (9, 7.4079999999999995), (10, 5.322), (11, 3.54), (12, 2.1839999999999997), (13, 1.4040000000000001), (14, 0.9400000000000001), (15, 0.532), (16, 0.382), (17, 0.186), (18, 0.14200000000000002), (19, 0.076), (20, 0.048), (21, 0.03), (22, 0.013999999999999999), (23, 0.018000000000000002), (24, 0.002), (26, 0.004)]
First injury in 4.93902 swings on average.
Chance of first heavy injury in 5.6538995703311485 swings on average.
-----
"""
        with subprocess.Popen(
                ['python', '../BBHitChance.py'],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                env={**os.environ, 'TEST': ''}
        ) as p:
            stdout = p.stdout.read().decode('utf-8')
            self.maxDiff = None
            self.assertEqual(original_stdout, stdout)
