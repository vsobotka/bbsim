import os
import subprocess
import unittest


class TestBBNimbleBattery(unittest.TestCase):
    def test_happy_case(self):
        original_stdout = """-----
HP = 100, Helmet = 40, Armor = 160
Nimble%: 0.4
Death in 6.09925 hits on average.
StDev: 0.6360186030952036
% Hits to die: [(3, 0.40499999999999997), (4, 1.675), (5, 8.175), (6, 67.205), (7, 22.415), (8, 0.125)]
First injury in 3.7923856340288924 hits on average.
No chance of heavy injury.
-----
HP = 100, Helmet = 120, Armor = 95
Nimble%: 0.4
Death in 6.1869 hits on average.
StDev: 0.6766027487115155
% Hits to die: [(4, 0.415), (5, 13.835), (6, 52.605000000000004), (7, 32.934999999999995), (8, 0.21)]
First injury in 3.9929153382925966 hits on average.
No chance of heavy injury.
-----
HP = 100, Helmet = 160, Armor = 80
Nimble%: 0.4
Death in 6.07945 hits on average.
StDev: 0.6634453296883431
% Hits to die: [(4, 0.3), (5, 17.28), (6, 56.765), (7, 25.485000000000003), (8, 0.16999999999999998)]
First injury in 3.507672892478546 hits on average.
No chance of heavy injury.
-----
HP = 100, Helmet = 190, Armor = 65
Nimble%: 0.4
Death in 6.2632 hits on average.
StDev: 0.7667171269494623
% Hits to die: [(4, 0.255), (5, 17.1), (6, 40.544999999999995), (7, 40.27), (8, 1.83)]
First injury in 3.304494778792312 hits on average.
No chance of heavy injury.
-----
HP = 100, Helmet = 140, Armor = 120
Nimble%: 0.4
Death in 6.74575 hits on average.
StDev: 0.5841438167950894
% Hits to die: [(4, 0.215), (5, 2.4899999999999998), (6, 24.245), (7, 68.605), (8, 4.445)]
First injury in 4.313279678068411 hits on average.
No chance of heavy injury.
-----
HP = 100, Helmet = 90, Armor = 115
Nimble%: 0.41000000000000003
Death in 6.0022 hits on average.
StDev: 0.6054861605970311
% Hits to die: [(3, 0.18), (4, 1.8499999999999999), (5, 11.575000000000001), (6, 70.375), (7, 16.005), (8, 0.015)]
First injury in 3.8674329886557572 hits on average.
No chance of heavy injury.
-----
HP = 100, Helmet = 120, Armor = 115
Nimble%: 0.4234566989846376
Death in 6.3308 hits on average.
StDev: 0.6608276588186461
% Hits to die: [(4, 0.605), (5, 8.905000000000001), (6, 47.339999999999996), (7, 43.105), (8, 0.045)]
First injury in 4.123909337077524 hits on average.
No chance of heavy injury.
-----
HP = 100, Helmet = 160, Armor = 95
Nimble%: 0.4234566989846376
Death in 6.16475 hits on average.
StDev: 0.7288580103147388
% Hits to die: [(4, 0.9450000000000001), (5, 16.23), (6, 48.845), (7, 33.365), (8, 0.615)]
First injury in 3.8164001804420833 hits on average.
No chance of heavy injury.
-----
HP = 100, Helmet = 225, Armor = 60
Nimble%: 0.4234566989846376
Death in 6.24325 hits on average.
StDev: 0.854468222520396
% Hits to die: [(4, 2.385), (5, 18.415), (6, 33.42), (7, 44.05), (8, 1.73)]
First injury in 3.102778473091364 hits on average.
No chance of heavy injury.
-----
HP = 100, Helmet = 160, Armor = 115
Nimble%: 0.4550216727255898
Death in 6.2128 hits on average.
StDev: 0.7313295441489475
% Hits to die: [(4, 0.67), (5, 16.04), (6, 44.945), (7, 38.03), (8, 0.315)]
First injury in 3.9103 hits on average.
No chance of heavy injury.
-----
HP = 100, Helmet = 120, Armor = 160
Nimble%: 0.47239908964061694
Death in 6.15985 hits on average.
StDev: 0.6751449981584896
% Hits to die: [(4, 0.8), (5, 13.34), (6, 55.269999999999996), (7, 30.255), (8, 0.335)]
First injury in 4.0565 hits on average.
No chance of heavy injury.
-----
HP = 100, Helmet = 190, Armor = 115
Nimble%: 0.49059954945598344
Death in 6.2881 hits on average.
StDev: 0.7912835752654191
% Hits to die: [(4, 0.36), (5, 17.825), (6, 36.605), (7, 43.065), (8, 2.145)]
First injury in 4.0692 hits on average.
No chance of heavy injury.
-----
HP = 100, Helmet = 160, Armor = 160
Nimble%: 0.5095142388904706
Death in 6.07295 hits on average.
StDev: 0.6882964369363356
% Hits to die: [(4, 0.75), (5, 17.84), (6, 54.99000000000001), (7, 26.205000000000002), (8, 0.215)]
First injury in 4.03185 hits on average.
No chance of heavy injury.
-----
HP = 100, Helmet = 225, Armor = 120
Nimble%: 0.5095142388904706
Death in 6.4001 hits on average.
StDev: 0.8186290354457774
% Hits to die: [(4, 0.19), (5, 16.84), (6, 29.835), (7, 49.04), (8, 4.095)]
First injury in 4.13675 hits on average.
No chance of heavy injury.
-----
HP = 100, Helmet = 190, Armor = 160
Nimble%: 0.5491826394040114
Death in 6.1423 hits on average.
StDev: 0.7382939549381364
% Hits to die: [(4, 0.59), (5, 18.395), (6, 48.195), (7, 31.835), (8, 0.985)]
First injury in 4.1423 hits on average.
Chance of first heavy injury in 6.018433179723503 hits on average.
-----
"""
        with subprocess.Popen(
                ['python', '../web/python/BBNimbleBattery.py'],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                env={**os.environ, 'TEST': ''}
        ) as p:
            stdout = p.stdout.read().decode('utf-8')
            self.maxDiff = None
            self.assertEqual(original_stdout, stdout)
