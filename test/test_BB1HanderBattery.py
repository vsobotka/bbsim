import subprocess
import unittest


class TestBB1HanderBattery(unittest.TestCase):
    def test_happy_case(self):
        original_stdout = """-----
Winged Mace:
HP = 100, Helmet = 120, Armor = 95
Death in 3.0005 hits on average.
StDev: 0.2494050122652052
% Hits to die: [(2, 3.085), (3, 93.78), (4, 3.1350000000000002)]
First injury in 1.02565 hits on average.
Chance of first heavy injury in 3.0228070175438595 hits on average.
-----
Flail:
HP = 100, Helmet = 120, Armor = 95
Death in 3.8492 hits on average.
StDev: 0.5489757997593665
% Hits to die: [(2, 0.06), (3, 23.53), (4, 67.875), (5, 8.5), (6, 0.034999999999999996)]
First injury in 1.9280196629213484 hits on average.
Chance of first heavy injury in 3.721495327102804 hits on average.
-----
Flail - Lash Only:
HP = 100, Helmet = 120, Armor = 95
Death in 3.22125 hits on average.
StDev: 0.4233289475926416
% Hits to die: [(2, 0.32), (3, 77.25999999999999), (4, 22.395), (5, 0.025)]
First injury in 1.7359735973597359 hits on average.
Chance of first heavy injury in 3.383882149046794 hits on average.
-----
3H Flail:
HP = 100, Helmet = 120, Armor = 95
Death in 3.43785 hits on average.
StDev: 0.386968816241357
% Hits to die: [(2.0, 0.01), (2.3333333333333335, 0.8049999999999999), (2.6666666666666665, 5.42), (3.0, 16.76), (3.3333333333333335, 32.0), (3.6666666666666665, 30.709999999999997), (4.0, 12.335), (4.333333333333333, 1.815), (4.666666666666667, 0.13999999999999999), (5.0, 0.005)]
First injury in 2.9973714774741733 hits on average.
No chance of heavy injury.
-----
3H Flail - Hail Only:
HP = 100, Helmet = 120, Armor = 95
Death in 2.5539 hits on average.
StDev: 0.23588560054668803
% Hits to die: [(2.0, 2.75), (2.3333333333333335, 38.99), (2.6666666666666665, 48.03), (3.0, 9.805), (3.3333333333333335, 0.42), (3.6666666666666665, 0.005)]
First injury in 2.417744132556218 hits on average.
No chance of heavy injury.
-----
Warhammer:
HP = 100, Helmet = 120, Armor = 95
Death in 2.99315 hits on average.
StDev: 0.16823939112061786
% Hits to die: [(2, 1.76), (3, 97.165), (4, 1.075)]
First injury in 1 hits on average.
Chance of first heavy injury in 2.6483457844183564 hits on average.
-----
Warhammer - Destroy Armor Once:
HP = 100, Helmet = 120, Armor = 95
Death in 3.5967 hits on average.
StDev: 0.49057226079055144
% Hits to die: [(3, 40.33), (4, 59.67)]
First injury in 2 hits on average.
Chance of first heavy injury in 2.876570733684637 hits on average.
-----
Fighting Axe:
HP = 100, Helmet = 120, Armor = 95
Death in 3.00645 hits on average.
StDev: 0.346719495010608
% Hits to die: [(2, 5.6899999999999995), (3, 87.97500000000001), (4, 6.335)]
First injury in 1.18935 hits on average.
Chance of first heavy injury in 2.745717104673065 hits on average.
-----
Head Splitter:
HP = 100, Helmet = 120, Armor = 95
Death in 2.73655 hits on average.
StDev: 0.4651396728357648
% Hits to die: [(2, 27.46), (3, 71.42500000000001), (4, 1.115)]
First injury in 1.1006 hits on average.
Chance of first heavy injury in 2.288879235447437 hits on average.
-----
Military Cleaver:
HP = 100, Helmet = 120, Armor = 95
Death in 2.9739 hits on average.
StDev: 0.22230893158632462
% Hits to die: [(2, 3.81), (3, 94.99), (4, 1.2)]
First injury in 1.3237 hits on average.
Chance of first heavy injury in 3.020916221439127 hits on average.
-----
Military Cleaver - Decap at 50%:
HP = 100, Helmet = 120, Armor = 95
Death in 2.962 hits on average.
StDev: 0.19120101435765074
% Hits to die: [(2, 3.8), (3, 96.2)]
First injury in 1.3211 hits on average.
Chance of first heavy injury in 3 hits on average.
-----
Khopesh:
HP = 100, Helmet = 120, Armor = 95
Death in 3.0349 hits on average.
StDev: 0.3054286403281733
% Hits to die: [(2, 2.98), (3, 90.55), (4, 6.47)]
First injury in 1.5782 hits on average.
Chance of first heavy injury in 3.0497041420118345 hits on average.
-----
Khopesh - Decap at 50%:
HP = 100, Helmet = 120, Armor = 95
Death in 2.97305 hits on average.
StDev: 0.16224984977092438
% Hits to die: [(2, 2.7), (3, 97.295), (4, 0.005)]
First injury in 1.56375 hits on average.
Chance of first heavy injury in 2.980291295803953 hits on average.
-----
Head Chopper:
HP = 100, Helmet = 120, Armor = 95
Death in 2.49695 hits on average.
StDev: 0.5000031976496581
% Hits to die: [(2, 50.305), (3, 49.695)]
First injury in 1.10145 hits on average.
Chance of first heavy injury in 2.5900875722004844 hits on average.
-----
Head Chopper - Decap at 50%:
HP = 100, Helmet = 120, Armor = 95
Death in 2.4951 hits on average.
StDev: 0.4999884892919748
% Hits to die: [(2, 50.49), (3, 49.51)]
First injury in 1.10275 hits on average.
Chance of first heavy injury in 2.5906253900886282 hits on average.
-----
Noble Sword:
HP = 100, Helmet = 120, Armor = 95
Death in 3.55975 hits on average.
StDev: 0.4964295112228731
% Hits to die: [(3, 44.025), (4, 55.974999999999994)]
First injury in 2.35635 hits on average.
Chance of first heavy injury in 3.4309212708098427 hits on average.
-----
Shamshir - Special:
HP = 100, Helmet = 120, Armor = 95
Death in 3.79255 hits on average.
StDev: 0.40549071337816334
% Hits to die: [(3, 20.745), (4, 79.255)]
First injury in 1 hits on average.
Chance of first heavy injury in 2.5458 hits on average.
-----
Rondel Dagger:
HP = 100, Helmet = 120, Armor = 95
Death in 6.6059 hits on average.
StDev: 0.8586163585109214
% Hits to die: [(4, 0.005), (5, 9.26), (6, 35.745), (7, 40.89), (8, 13.334999999999999), (9, 0.76), (10, 0.005)]
First injury in 2.60145 hits on average.
Chance of first heavy injury in 5.828943593274803 hits on average.
-----
Qatal Dagger - Deathblow:
HP = 100, Helmet = 120, Armor = 95
Death in 2.9515 hits on average.
StDev: 0.25209309301600735
% Hits to die: [(2, 5.72), (3, 93.41000000000001), (4, 0.8699999999999999)]
First injury in 1 hits on average.
Chance of first heavy injury in 1 hits on average.
-----
Fighting Spear:
HP = 100, Helmet = 120, Armor = 95
Death in 4.20095 hits on average.
StDev: 0.4008455205644287
% Hits to die: [(3, 0.005), (4, 79.89500000000001), (5, 20.1)]
First injury in 1 hits on average.
Chance of first heavy injury in 3.5550378275464705 hits on average.
-----
Heavy Javelins - 2 Range:
HP = 100, Helmet = 120, Armor = 95
Death in 2.9971 hits on average.
StDev: 0.24019674170091523
% Hits to die: [(2, 3.0300000000000002), (3, 94.23), (4, 2.74)]
First injury in 1 hits on average.
Chance of first heavy injury in 1 hits on average.
-----
Heavy Axes - 2 Range:
HP = 100, Helmet = 120, Armor = 95
Death in 3.7906 hits on average.
StDev: 0.45051280568858915
% Hits to die: [(3, 22.81), (4, 75.32), (5, 1.87)]
First injury in 1 hits on average.
Chance of first heavy injury in 2.0799699172724995 hits on average.
-----
"""
        with subprocess.Popen(
                ['python', '-c', 'from python.BB1HanderBattery import BB1HanderBattery; BB1HanderBattery(random_seed="battlebrothers")'],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
        ) as p:
            stdout = p.stdout.read().decode('utf-8')
            self.maxDiff = None
            self.assertEqual(original_stdout, stdout)
