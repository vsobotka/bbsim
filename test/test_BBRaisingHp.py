import os
import subprocess
import unittest


class TestBBRaisingHp(unittest.TestCase):
    def test_happy_case(self):
        original_stdout = """-----
HP = 60, Helmet = 120, Armor = 95
Death in 2.5128 hits on average.
StDev: 0.5012471670105695
% Hits to die: [(2, 48.79), (3, 51.13999999999999), (4, 0.06999999999999999)]
First injury in 1.0378 hits on average.
Chance of first heavy injury in 2.418055038058232 hits on average.
-----
HP = 70, Helmet = 120, Armor = 95
Death in 2.66275 hits on average.
StDev: 0.5240478688139476
% Hits to die: [(2, 36.28), (3, 61.165000000000006), (4, 2.555)]
First injury in 1.35055 hits on average.
Chance of first heavy injury in 2.4615093318907224 hits on average.
-----
HP = 80, Helmet = 120, Armor = 95
Death in 2.8867 hits on average.
StDev: 0.5314858736238368
% Hits to die: [(2, 20.43), (3, 70.47), (4, 9.1)]
First injury in 1.69125 hits on average.
Chance of first heavy injury in 2.5613591082871143 hits on average.
-----
HP = 90, Helmet = 120, Armor = 95
Death in 3.11785 hits on average.
StDev: 0.5173729421201517
% Hits to die: [(2, 8.18), (3, 71.86), (4, 19.955000000000002), (5, 0.005)]
First injury in 2.28455 hits on average.
Chance of first heavy injury in 2.688155277165439 hits on average.
-----
HP = 100, Helmet = 120, Armor = 95
Death in 3.33745 hits on average.
StDev: 0.5008892512343422
% Hits to die: [(2, 1.195), (3, 64.035), (4, 34.599999999999994), (5, 0.16999999999999998)]
First injury in 2.46585 hits on average.
Chance of first heavy injury in 2.823867331454585 hits on average.
-----
HP = 110, Helmet = 120, Armor = 95
Death in 3.50475 hits on average.
StDev: 0.5220067643748524
% Hits to die: [(2, 0.185), (3, 50.095), (4, 48.78), (5, 0.9400000000000001)]
First injury in 2.49575 hits on average.
Chance of first heavy injury in 2.9836366672232426 hits on average.
-----
HP = 120, Helmet = 120, Armor = 95
Death in 3.63655 hits on average.
StDev: 0.5340115690860975
% Hits to die: [(2, 0.005), (3, 39.019999999999996), (4, 58.29), (5, 2.685)]
First injury in 2.51225 hits on average.
Chance of first heavy injury in 3.144514438969625 hits on average.
-----
HP = 130, Helmet = 120, Armor = 95
Death in 3.75845 hits on average.
StDev: 0.5516509887969675
% Hits to die: [(3, 30.209999999999997), (4, 63.735), (5, 6.055)]
First injury in 2.54715 hits on average.
Chance of first heavy injury in 3.3091664237831537 hits on average.
-----
HP = 140, Helmet = 120, Armor = 95
Death in 3.9003 hits on average.
StDev: 0.5753924433142924
% Hits to die: [(3, 22.035), (4, 65.9), (5, 12.065)]
First injury in 2.57575 hits on average.
Chance of first heavy injury in 3.4988801791713326 hits on average.
-----
"""
        with subprocess.Popen(
                ['python', '../BBRaisingHp.py'],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                env={**os.environ, 'TEST': ''}
        ) as p:
            stdout = p.stdout.read().decode('utf-8')
            self.maxDiff = None
            self.assertEqual(original_stdout, stdout)
