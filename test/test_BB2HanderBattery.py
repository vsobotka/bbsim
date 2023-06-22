import os
import subprocess
import unittest


class TestBB2HanderBattery(unittest.TestCase):
    def test_happy_case(self):
        original_stdout = """-----
2H Flanged Mace - Cudgel:
HP = 100, Helmet = 120, Armor = 95
Death in 2 hits on average.
StDev: 0.0
% Hits to die: [(2, 100.0)]
First injury in 1 hits on average.
Chance of first heavy injury in 1.18295 hits on average.
-----
2H Flail - Pound:
HP = 100, Helmet = 120, Armor = 95
Death in 2.1766 hits on average.
StDev: 0.38133936458953366
% Hits to die: [(2, 82.34), (3, 17.66)]
First injury in 1.0055 hits on average.
Chance of first heavy injury in 1.7558854934662125 hits on average.
-----
Berserk Chain - Pound:
HP = 100, Helmet = 120, Armor = 95
Death in 1.9769 hits on average.
StDev: 0.3096307212780701
% Hits to die: [(1, 5.975), (2, 90.36), (3, 3.665)]
First injury in 1 hits on average.
Chance of first heavy injury in 1.6167094727300197 hits on average.
-----
2H Hammer - Smite:
HP = 100, Helmet = 120, Armor = 95
Death in 2 hits on average.
StDev: 0.0
% Hits to die: [(2, 100.0)]
First injury in 1 hits on average.
Chance of first heavy injury in 1.4969831365066268 hits on average.
-----
2H Hammer - AoE:
HP = 100, Helmet = 120, Armor = 95
Death in 2.35445 hits on average.
StDev: 0.4783582745515558
% Hits to die: [(2, 64.55499999999999), (3, 35.445)]
First injury in 1 hits on average.
Chance of first heavy injury in 2.213954447078223 hits on average.
-----
Bardiche - Split Man
HP = 100, Helmet = 120, Armor = 95
Death in 2 hits on average.
StDev: 0.0
% Hits to die: [(2, 100.0)]
First injury in 1 hits on average.
Chance of first heavy injury in 2 hits on average.
-----
Greataxe - Split Man
HP = 100, Helmet = 120, Armor = 95
Death in 2 hits on average.
StDev: 0.0
% Hits to die: [(2, 100.0)]
First injury in 1 hits on average.
Chance of first heavy injury in 2 hits on average.
-----
Mansplitter - Split Man:
HP = 100, Helmet = 120, Armor = 95
Death in 2 hits on average.
StDev: 0.0
% Hits to die: [(2, 100.0)]
First injury in 1 hits on average.
Chance of first heavy injury in 1.87815 hits on average.
-----
2H Scimitar:
HP = 100, Helmet = 120, Armor = 95
Death in 2.7287 hits on average.
StDev: 0.5019052753710328
% Hits to die: [(2, 29.84), (3, 67.45), (4, 2.71)]
First injury in 2.38625 hits on average.
Chance of first heavy injury in 2.4351820538834406 hits on average.
-----
2H Scimitar - Decap at 50%:
HP = 100, Helmet = 120, Armor = 95
Death in 2.703 hits on average.
StDev: 0.45924018234171743
% Hits to die: [(2, 29.805), (3, 70.09), (4, 0.105)]
First injury in 2.3807 hits on average.
Chance of first heavy injury in 2.4481458202388433 hits on average.
-----
Rusty Warblade:
HP = 100, Helmet = 120, Armor = 95
Death in 2.8291 hits on average.
StDev: 0.39357456097511223
% Hits to die: [(2, 17.75), (3, 81.58999999999999), (4, 0.66)]
First injury in 1.9721540541894125 hits on average.
Chance of first heavy injury in 2.528946990374946 hits on average.
-----
Rusty Warblade - Decap at 50%:
HP = 100, Helmet = 120, Armor = 95
Death in 2.8212 hits on average.
StDev: 0.3831943395916682
% Hits to die: [(2, 17.88), (3, 82.12)]
First injury in 1.98135 hits on average.
Chance of first heavy injury in 2.638285155401 hits on average.
-----
Greatsword - Overhead
HP = 100, Helmet = 120, Armor = 95
Death in 2.41575 hits on average.
StDev: 0.4928631485556211
% Hits to die: [(2, 58.425000000000004), (3, 41.575)]
First injury in 1 hits on average.
Chance of first heavy injury in 2.41575 hits on average.
-----
Greatsword - AoE:
HP = 100, Helmet = 120, Armor = 95
Death in 2.43305 hits on average.
StDev: 0.4955098122123314
% Hits to die: [(2, 56.69499999999999), (3, 43.305)]
First injury in 2.2114 hits on average.
Chance of first heavy injury in 2.41975 hits on average.
-----
Polehammer:
HP = 100, Helmet = 120, Armor = 95
Death in 2.78775 hits on average.
StDev: 0.4090333762850481
% Hits to die: [(2, 21.23), (3, 78.765), (4, 0.005)]
First injury in 1.00205 hits on average.
Chance of first heavy injury in 2.4122816139767056 hits on average.
-----
Longaxe:
HP = 100, Helmet = 120, Armor = 95
Death in 2.6826 hits on average.
StDev: 0.4730416772562657
% Hits to die: [(2, 32.095), (3, 67.55), (4, 0.35500000000000004)]
First injury in 1.6611 hits on average.
Chance of first heavy injury in 2.4206185567010308 hits on average.
-----
Spetum:
HP = 100, Helmet = 120, Armor = 95
Death in 3.88215 hits on average.
StDev: 0.7314971851665564
% Hits to die: [(3, 33.339999999999996), (4, 45.105000000000004), (5, 21.555)]
First injury in 2.81005 hits on average.
Chance of first heavy injury in 3.785813773536239 hits on average.
-----
Pike:
HP = 100, Helmet = 120, Armor = 95
Death in 3.59445 hits on average.
StDev: 0.506746521548846
% Hits to die: [(3, 41.339999999999996), (4, 57.875), (5, 0.7849999999999999)]
First injury in 2.548 hits on average.
Chance of first heavy injury in 3.221122913505311 hits on average.
-----
Ancient Bladed Pike:
HP = 100, Helmet = 120, Armor = 95
Death in 3.34395 hits on average.
StDev: 0.5011596108504529
% Hits to die: [(2, 1.17), (3, 63.370000000000005), (4, 35.355), (5, 0.105)]
First injury in 2.47145 hits on average.
Chance of first heavy injury in 2.836859477301012 hits on average.
-----
Billhook:
HP = 100, Helmet = 120, Armor = 95
Death in 2.99615 hits on average.
StDev: 0.46340685665594095
% Hits to die: [(2, 10.93), (3, 78.525), (4, 10.545)]
First injury in 2.2227 hits on average.
Chance of first heavy injury in 2.5424430641821947 hits on average.
-----
Warscythe:
HP = 100, Helmet = 120, Armor = 95
Death in 3.56225 hits on average.
StDev: 0.5580685527114714
% Hits to die: [(3, 47.04), (4, 49.695), (5, 3.2649999999999997)]
First injury in 2.5477 hits on average.
Chance of first heavy injury in 3.2368045649072754 hits on average.
-----
Warscythe - AoE:
HP = 100, Helmet = 120, Armor = 95
Death in 3.6598 hits on average.
StDev: 0.6304631901956763
% Hits to die: [(3, 42.67), (4, 48.68), (5, 8.649999999999999)]
First injury in 2.5633 hits on average.
Chance of first heavy injury in 3.347872797593468 hits on average.
-----
Warbow - Quick Shot:
HP = 100, Helmet = 120, Armor = 95
Death in 4.6931 hits on average.
StDev: 0.5769133656378335
% Hits to die: [(4, 36.695), (5, 57.3), (6, 6.005)]
First injury in 3.8676057829793993 hits on average.
Chance of first heavy injury in 4.504234084379253 hits on average.
-----
Heavy Xbow - Mastery:
HP = 100, Helmet = 120, Armor = 95
Death in 2.92025 hits on average.
StDev: 0.2714656924569089
% Hits to die: [(2, 7.99), (3, 91.995), (4, 0.015)]
First injury in 1 hits on average.
Chance of first heavy injury in 2.928831320040751 hits on average.
-----
Handgonne
HP = 100, Helmet = 120, Armor = 95
Death in 5.12285 hits on average.
StDev: 0.901054089621495
% Hits to die: [(3, 0.735), (4, 26.634999999999998), (5, 38.49), (6, 28.005000000000003), (7, 6.02), (8, 0.11499999999999999)]
First injury in 4.053563390847712 hits on average.
Chance of first heavy injury in 4.60414501039501 hits on average.
-----
"""
        with subprocess.Popen(
                ['python', '../web/python/BB2HanderBattery.py'],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                env={**os.environ, 'TEST': ''}
        ) as p:
            stdout = p.stdout.read().decode('utf-8')
            self.maxDiff = None
            self.assertEqual(original_stdout, stdout)
