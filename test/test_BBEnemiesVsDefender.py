import os
import subprocess
import unittest


class TestBBCalc(unittest.TestCase):
    def test_happy_case(self):
        original_stdout = """-----
Ancient Dead - Ancient Sword:
HP = 100, Helmet = 120, Armor = 95
Death in 7.1877 hits on average.
StDev: 0.9925559060942977
% Hits to die: [(5, 4.6899999999999995), (6, 19.650000000000002), (7, 35.77), (8, 31.979999999999997), (9, 7.91)]
First injury in 5.2708 hits on average.
Chance of first heavy injury in 8.053892215568862 hits on average.
3.8025 Fearsome procs on average.
-----
Ancient Dead - Bladed Pike:
HP = 100, Helmet = 120, Armor = 95
Death in 3.3399 hits on average.
StDev: 0.5033818921384968
% Hits to die: [(2, 1.34), (3, 63.44), (4, 35.11), (5, 0.11)]
First injury in 2.4696 hits on average.
Chance of first heavy injury in 2.8268647007805723 hits on average.
0.0318 Fearsome procs on average.
-----
Ancient Dead - Warscythe AoE:
HP = 100, Helmet = 120, Armor = 95
Death in 3.6654 hits on average.
StDev: 0.6326791195280816
% Hits to die: [(3, 42.34), (4, 48.78), (5, 8.88)]
First injury in 2.5736 hits on average.
Chance of first heavy injury in 3.352485474499677 hits on average.
0.7112 Fearsome procs on average.
-----
Ancient Dead - Crypt Cleaver:
HP = 100, Helmet = 120, Armor = 95
Death in 2.8751 hits on average.
StDev: 0.5150985562513889
% Hits to die: [(2, 20.29), (3, 71.91), (4, 7.8)]
First injury in 2.393 hits on average.
Chance of first heavy injury in 2.533524027459954 hits on average.
0.2239 Fearsome procs on average.
-----
Necrosavant - Khopesh:
HP = 100, Helmet = 120, Armor = 95
Death in 3.8299 hits on average.
StDev: 0.6457613264737033
% Hits to die: [(3, 30.8), (4, 55.410000000000004), (5, 13.79)]
First injury in 2.7394 hits on average.
Chance of first heavy injury in 3.420128148475475 hits on average.
-----
Fallen Hero - Greataxe:
HP = 100, Helmet = 120, Armor = 95
Death in 2 hits on average.
StDev: 0.0
% Hits to die: [(2, 100.0)]
First injury in 1 hits on average.
Chance of first heavy injury in 2 hits on average.
0 Fearsome procs on average.
-----
Orc Berserker - Berserk Chain:
HP = 100, Helmet = 120, Armor = 95
Death in 1.7848 hits on average.
StDev: 0.410981569641582
% Hits to die: [(1, 21.52), (2, 78.48)]
First injury in 1 hits on average.
Chance of first heavy injury in 1.4161 hits on average.
-----
Orc Young/Warrior - Head Splitter:
HP = 100, Helmet = 120, Armor = 95
Death in 3.7047 hits on average.
StDev: 0.610520420230439
% Hits to die: [(2, 0.63), (3, 35.870000000000005), (4, 55.900000000000006), (5, 7.6)]
First injury in 2.56 hits on average.
Chance of first heavy injury in 3.3018673535093366 hits on average.
-----
Orc Young/Warrior - Head Chopper:
HP = 100, Helmet = 120, Armor = 95
Death in 3.4513 hits on average.
StDev: 0.5324064759801167
% Hits to die: [(2, 1.79), (3, 51.29), (4, 46.92)]
First injury in 2.6911292826829523 hits on average.
Chance of first heavy injury in 3.1832759077657036 hits on average.
-----
Orc Warlord - Mansplitter:
HP = 100, Helmet = 120, Armor = 95
Death in 1.8255 hits on average.
StDev: 0.3795578433067107
% Hits to die: [(1, 17.45), (2, 82.55)]
First injury in 1 hits on average.
Chance of first heavy injury in 1.0723 hits on average.
0 Fearsome procs on average.
-----
Goblin Ambusher - Reinforced Boondock Bow:
HP = 100, Helmet = 120, Armor = 95
Death in 6.6552 hits on average.
StDev: 0.7897944906959996
% Hits to die: [(5, 6.49), (6, 34.63), (7, 46.02), (8, 12.590000000000002), (9, 0.27)]
First injury in 6.039519104868468 hits on average.
Chance of first heavy injury in 6.322033898305085 hits on average.
First poison in 1.0405 hits on average.
-----
Goblin Overseer - Spiked Impaler:
HP = 100, Helmet = 120, Armor = 95
Death in 2.7566 hits on average.
StDev: 0.42915598269830585
% Hits to die: [(2, 24.34), (3, 75.66000000000001)]
First injury in 1 hits on average.
Chance of first heavy injury in 2.3938015832912245 hits on average.
-----
Chosen - 2H Spiked Mace:
HP = 100, Helmet = 120, Armor = 95
Death in 2 hits on average.
StDev: 0.0
% Hits to die: [(2, 100.0)]
First injury in 1 hits on average.
Chance of first heavy injury in 1 hits on average.
-----
Chosen - 2H Skull Hammer:
HP = 100, Helmet = 120, Armor = 95
Death in 2 hits on average.
StDev: 0.0
% Hits to die: [(2, 100.0)]
First injury in 1 hits on average.
Chance of first heavy injury in 1 hits on average.
-----
Chosen - Heavy Rusty Axe:
HP = 100, Helmet = 120, Armor = 95
Death in 2 hits on average.
StDev: 0.0
% Hits to die: [(2, 100.0)]
First injury in 1 hits on average.
Chance of first heavy injury in 1 hits on average.
-----
Chosen - Rusty Warblade:
HP = 100, Helmet = 120, Armor = 95
Death in 2.524 hits on average.
StDev: 0.4994486408976297
% Hits to die: [(2, 47.599999999999994), (3, 52.400000000000006)]
First injury in 1 hits on average.
Chance of first heavy injury in 2.3115729996973062 hits on average.
-----
Billman - Billhook:
HP = 100, Helmet = 120, Armor = 95
Death in 3.0013 hits on average.
StDev: 0.46034715373313106
% Hits to die: [(2, 10.52), (3, 78.84), (4, 10.63), (5, 0.01)]
First injury in 2.2305 hits on average.
Chance of first heavy injury in 2.562047569803516 hits on average.
-----
Arbalester - Heavy Xbow:
HP = 100, Helmet = 120, Armor = 95
Death in 2.9206 hits on average.
StDev: 0.2711143491204955
% Hits to die: [(2, 7.960000000000001), (3, 92.02), (4, 0.02)]
First injury in 1 hits on average.
Chance of first heavy injury in 2.925176056338028 hits on average.
-----
Knight - Fighting Axe:
HP = 100, Helmet = 120, Armor = 95
Death in 4.5662 hits on average.
StDev: 0.5634263970834993
% Hits to die: [(3, 1.78), (4, 41.63), (5, 54.779999999999994), (6, 1.81)]
First injury in 3.1616 hits on average.
Chance of first heavy injury in 3.7684221065278334 hits on average.
-----
Sergeant - Winged Mace:
HP = 100, Helmet = 120, Armor = 95
Death in 3.0013 hits on average.
StDev: 0.25437134366521674
% Hits to die: [(2, 3.17), (3, 93.53), (4, 3.3000000000000003)]
First injury in 1.0219 hits on average.
Chance of first heavy injury in 3.025268817204301 hits on average.
-----
Zweihander - Greatsword:
HP = 100, Helmet = 120, Armor = 95
Death in 2.4223 hits on average.
StDev: 0.493950512410779
% Hits to die: [(2, 57.769999999999996), (3, 42.230000000000004)]
First injury in 1 hits on average.
Chance of first heavy injury in 2.4223 hits on average.
-----
Raider - Flail (Double Grip):
HP = 100, Helmet = 120, Armor = 95
Death in 4.9378 hits on average.
StDev: 0.7943514709660595
% Hits to die: [(3, 2.25), (4, 26.85), (5, 47.02), (6, 22.63), (7, 1.25)]
First injury in 4.065291407971159 hits on average.
Chance of first heavy injury in 4.542224080267559 hits on average.
-----
Raider - Longaxe:
HP = 100, Helmet = 120, Armor = 95
Death in 2.6249 hits on average.
StDev: 0.4893096487841205
% Hits to die: [(2, 37.76), (3, 61.99), (4, 0.25)]
First injury in 1.6644 hits on average.
Chance of first heavy injury in 2.4287014563106797 hits on average.
-----
Marksman - Xbow:
HP = 100, Helmet = 120, Armor = 95
Death in 3.5258 hits on average.
StDev: 0.5043409521143389
% Hits to die: [(2, 0.25), (3, 46.92), (4, 52.83)]
First injury in 1.2242 hits on average.
Chance of first heavy injury in 4 hits on average.
-----
Swordmaster - Noble Sword:
HP = 100, Helmet = 120, Armor = 95
Death in 3.4211 hits on average.
StDev: 0.4937602352528925
% Hits to die: [(3, 57.89), (4, 42.11)]
First injury in 1 hits on average.
Chance of first heavy injury in 3.2503 hits on average.
-----
Master Archer - Warbow:
HP = 100, Helmet = 120, Armor = 95
Death in 3.5113 hits on average.
StDev: 0.5018939128441139
% Hits to die: [(3, 48.97), (4, 50.93), (5, 0.1)]
First injury in 1.0848 hits on average.
Chance of first heavy injury in 2.9359777313848294 hits on average.
-----
Conscript - PoleMace:
HP = 100, Helmet = 120, Armor = 95
Death in 3.097 hits on average.
StDev: 0.30033318165331013
% Hits to die: [(2, 0.13), (3, 90.03999999999999), (4, 9.83)]
First injury in 1.3962 hits on average.
Chance of first heavy injury in 2.643010176754151 hits on average.
-----
Gunner - Handgonne:
HP = 100, Helmet = 120, Armor = 95
Death in 4.7379 hits on average.
StDev: 0.8077554313551153
% Hits to die: [(3, 3.8899999999999997), (4, 36.63), (5, 42.14), (6, 16.48), (7, 0.86)]
First injury in 3.6654 hits on average.
Chance of first heavy injury in 4.209050911376493 hits on average.
2.2001 Fearsome procs on average.
-----
Officer - 2H Scimitar:
HP = 100, Helmet = 120, Armor = 95
Death in 2.5725 hits on average.
StDev: 0.5116345639152023
% Hits to die: [(2, 43.6), (3, 55.55), (4, 0.8500000000000001)]
First injury in 1.4295 hits on average.
Chance of first heavy injury in 2.390973681577104 hits on average.
-----
Assassin - Qatal:
HP = 100, Helmet = 120, Armor = 95
Death in 5.0934 hits on average.
StDev: 0.6295363941879458
% Hits to die: [(4, 15.509999999999998), (5, 59.709999999999994), (6, 24.709999999999997), (7, 0.06999999999999999)]
First injury in 4.634979233964006 hits on average.
Chance of first heavy injury in 4.828190158465388 hits on average.
-----
Frenzied Direwolf:
HP = 100, Helmet = 120, Armor = 95
Death in 6.2031 hits on average.
StDev: 1.1030739173812065
% Hits to die: [(4, 4.3), (5, 25.16), (6, 30.64), (7, 26.240000000000002), (8, 13.15), (9, 0.51)]
First injury in 4.8444 hits on average.
Chance of first heavy injury in 5.746413752222881 hits on average.
-----
Nachzehrer - Tier 3:
HP = 100, Helmet = 120, Armor = 95
Death in 4.6491 hits on average.
StDev: 0.9132648001864114
% Hits to die: [(3, 10.91), (4, 32.65), (5, 37.08), (6, 19.34), (7, 0.02)]
First injury in 3.3297 hits on average.
Chance of first heavy injury in 3.8244664863240154 hits on average.
-----
Lindwurm - Head:
HP = 100, Helmet = 120, Armor = 95
Death in 2.2377 hits on average.
StDev: 0.4256957031532833
% Hits to die: [(2, 76.23), (3, 23.77)]
First injury in 1 hits on average.
Chance of first heavy injury in 2.1362598588625987 hits on average.
0 Fearsome procs on average.
-----
Unhold:
HP = 100, Helmet = 120, Armor = 95
Death in 3.9568 hits on average.
StDev: 0.6103859574905948
% Hits to die: [(3, 20.8), (4, 62.8), (5, 16.32), (6, 0.08)]
First injury in 1.428 hits on average.
Chance of first heavy injury in 3.5444656274531794 hits on average.
-----
Schrat:
HP = 100, Helmet = 120, Armor = 95
Death in 2.5904 hits on average.
StDev: 0.491784531276168
% Hits to die: [(2, 40.96), (3, 59.040000000000006)]
First injury in 1 hits on average.
Chance of first heavy injury in 1.0944 hits on average.
-----
120.67060000000001 hits to die total against this test group.
3.4477314285714287 hits to die on average against this test group.
"""
        with subprocess.Popen(
                ['python', '../BBEnemiesVsDefender.py'],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                env={**os.environ, 'TEST': ''}
        ) as p:
            stdout = p.stdout.read().decode('utf-8')
            self.maxDiff = None
            self.assertEqual(original_stdout, stdout)
