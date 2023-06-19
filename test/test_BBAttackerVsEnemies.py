import os
import subprocess
import unittest


class TestBBAttackerVsEnemies(unittest.TestCase):
    def test_happy_case(self):
        original_stdout = """-----
Ancient Legion:
HP = 55, Helmet = 130, Armor = 135
Death in 3.5708 hits on average.
StDev: 0.4959959286084107
% Hits to die: [(3, 42.970000000000006), (4, 56.98), (5, 0.05)]
23.471355250000006 bonus armor from Forge on average.
-----
Honor Guard:
HP = 65, Helmet = 180, Armor = 210
Death in 4.9318 hits on average.
StDev: 0.700712394485768
% Hits to die: [(3, 0.44999999999999996), (4, 26.82), (5, 51.849999999999994), (6, 20.86), (7, 0.02)]
49.94961562500001 bonus armor from Forge on average.
-----
Fallen Hero - Heavy:
HP = 180, Helmet = 255, Armor = 260
Death in 8.2861 hits on average.
StDev: 0.9438940001866517
% Hits to die: [(5, 0.09), (6, 3.71), (7, 16.36), (8, 33.46), (9, 40.12), (10, 6.239999999999999), (11, 0.02)]
89.815679125 bonus armor from Forge on average.
-----
Orc Young - Heavy:
HP = 125, Helmet = 120, Armor = 120
Death in 4.0906 hits on average.
StDev: 0.5776028068666651
% Hits to die: [(3, 12.559999999999999), (4, 65.82000000000001), (5, 21.62)]
First injury in 3.0436 hits on average.
Chance of first heavy injury in 3.823369565217391 hits on average.
-----
Orc Berserker - Heavy:
HP = 250, Helmet = 120, Armor = 110
Death in 5.8829 hits on average.
StDev: 0.5576904982776619
% Hits to die: [(4, 0.72), (5, 19.93), (6, 69.69), (7, 9.66)]
First injury in 4.17625383828045 hits on average.
No chance of heavy injury.
-----
Orc Warrior - Light:
HP = 200, Helmet = 240, Armor = 280
Death in 7.8707 hits on average.
StDev: 0.8627026924691724
% Hits to die: [(5, 0.22999999999999998), (6, 7.1), (7, 21.790000000000003), (8, 47.17), (9, 23.669999999999998), (10, 0.04)]
First injury in 6.1914 hits on average.
No chance of heavy injury.
-----
Orc Warrior - Heavy:
HP = 200, Helmet = 360, Armor = 400
Death in 10.2797 hits on average.
StDev: 1.0875597402528572
% Hits to die: [(6, 0.02), (7, 0.62), (8, 6.81), (9, 15.629999999999999), (10, 26.790000000000003), (11, 41.15), (12, 8.93), (13, 0.05)]
First injury in 8.2333 hits on average.
No chance of heavy injury.
-----
Orc Warlord:
HP = 300, Helmet = 500, Armor = 500
Death in 14.1259 hits on average.
StDev: 1.5275085984215686
% Hits to die: [(10, 1.3299999999999998), (11, 5.43), (12, 10.41), (13, 14.2), (14, 18.43), (15, 32.0), (16, 17.380000000000003), (17, 0.8200000000000001)]
First injury in 11.881306503353747 hits on average.
No chance of heavy injury.
-----
Goblin Skirmisher - Heavy:
HP = 40, Helmet = 90, Armor = 90
Death in 2.0081 hits on average.
StDev: 0.08963924095702694
% Hits to die: [(2, 99.19), (3, 0.8099999999999999)]
First injury in 1 hits on average.
Chance of first heavy injury in 1.4266844153184517 hits on average.
-----
Goblin Ambusher:
HP = 40, Helmet = 25, Armor = 35
Death in 1.5426 hits on average.
StDev: 0.4982068456034106
% Hits to die: [(1, 45.739999999999995), (2, 54.26)]
First injury in 1 hits on average.
Chance of first heavy injury in 1 hits on average.
-----
Goblin Shaman:
HP = 70, Helmet = 35, Armor = 45
Death in 2.1861 hits on average.
StDev: 0.38920680645875066
% Hits to die: [(2, 81.39), (3, 18.61)]
First injury in 1.1384 hits on average.
Chance of first heavy injury in 1.9297889610389611 hits on average.
-----
Goblin Overseer:
HP = 70, Helmet = 120, Armor = 180
Death in 3.5367 hits on average.
StDev: 0.5977364292762224
% Hits to die: [(2, 4.54), (3, 38.14), (4, 56.43), (5, 0.89)]
First injury in 2.1112 hits on average.
Chance of first heavy injury in 3.428078524687686 hits on average.
-----
Chosen - Light:
HP = 130, Helmet = 145, Armor = 140
Death in 4.6134 hits on average.
StDev: 0.5622917900927601
% Hits to die: [(3, 2.4699999999999998), (4, 35.199999999999996), (5, 60.85), (6, 1.48)]
First injury in 3.89 hits on average.
Chance of first heavy injury in 4.094403324243605 hits on average.
27.503835250000005 bonus armor from Forge on average.
-----
Chosen - Heavy:
HP = 130, Helmet = 190, Armor = 230
Death in 6.2726 hits on average.
StDev: 0.7785562632112715
% Hits to die: [(4, 0.9199999999999999), (5, 15.14), (6, 42.19), (7, 39.26), (8, 2.4899999999999998)]
First injury in 5.455191749274056 hits on average.
Chance of first heavy injury in 6.001900237529691 hits on average.
60.0952425 bonus armor from Forge on average.
-----
Barbarian King:
HP = 150, Helmet = 250, Armor = 270
Death in 7.8585 hits on average.
StDev: 0.9670425363585166
% Hits to die: [(5, 0.33), (6, 9.84), (7, 22.68), (8, 38.6), (9, 27.900000000000002), (10, 0.65)]
First injury in 6.819563912782557 hits on average.
Chance of first heavy injury in 7.407321994811185 hits on average.
91.59777662500001 bonus armor from Forge on average.
-----
Footman - Heavy:
HP = 70, Helmet = 215, Armor = 150
Death in 4 hits on average.
StDev: 0.7840034860551416
% Hits to die: [(3, 30.599999999999998), (4, 38.93), (5, 30.34), (6, 0.13)]
First injury in 2.982796559311862 hits on average.
Chance of first heavy injury in 3.8359029520736225 hits on average.
41.3396264375 bonus armor from Forge on average.
-----
Billman:
HP = 70, Helmet = 80, Armor = 130
Death in 3.2537 hits on average.
StDev: 0.6064429794372517
% Hits to die: [(2, 8.92), (3, 56.79), (4, 34.29)]
First injury in 1.715 hits on average.
Chance of first heavy injury in 3.2650826672506295 hits on average.
15.8788629375 bonus armor from Forge on average.
-----
Arbalester:
HP = 60, Helmet = 80, Armor = 65
Death in 2.4262 hits on average.
StDev: 0.4945482967332717
% Hits to die: [(2, 57.379999999999995), (3, 42.620000000000005)]
First injury in 1 hits on average.
Chance of first heavy injury in 2.426327898369511 hits on average.
-----
Knight:
HP = 125, Helmet = 300, Armor = 300
Death in 8.5762 hits on average.
StDev: 1.0587283176363314
% Hits to die: [(6, 3.2), (7, 13.34), (8, 26.31), (9, 37.62), (10, 18.85), (11, 0.6799999999999999)]
First injury in 7.705493183640738 hits on average.
Chance of first heavy injury in 8.104616225075116 hits on average.
122.45451306250001 bonus armor from Forge on average.
-----
Sergeant:
HP = 100, Helmet = 0, Armor = 150
Nimble%: 0.43862416852231406
Death in 5.5995 hits on average.
StDev: 0.5152924437930979
% Hits to die: [(3, 0.04), (4, 1.11), (5, 37.75), (6, 61.06), (7, 0.04)]
First injury in 3.380174627632255 hits on average.
No chance of heavy injury.
-----
Zweihander:
HP = 90, Helmet = 160, Armor = 240
Death in 5.6476 hits on average.
StDev: 0.7486456351497034
% Hits to die: [(3, 0.47000000000000003), (4, 5.06), (5, 33.839999999999996), (6, 50.51), (7, 10.11), (8, 0.01)]
First injury in 5.095171308355039 hits on average.
Chance of first heavy injury in 5.459910198845414 hits on average.
54.675364875 bonus armor from Forge on average.
-----
Brigand Raider - Heavy:
HP = 70, Helmet = 140, Armor = 115
Death in 3.2122 hits on average.
StDev: 0.5316008088236832
% Hits to die: [(2, 5.7700000000000005), (3, 67.24), (4, 26.99)]
First injury in 1.7252 hits on average.
Chance of first heavy injury in 2.8887372860332423 hits on average.
-----
Brigand Leader - Heavy:
HP = 100, Helmet = 250, Armor = 230
Death in 6.5369 hits on average.
StDev: 0.8986206885634179
% Hits to die: [(5, 12.98), (6, 35.31), (7, 36.75), (8, 14.96)]
First injury in 5.1149 hits on average.
Chance of first heavy injury in 5.376318168122928 hits on average.
-----
Hedge Knight:
HP = 150, Helmet = 300, Armor = 300
Death in 8.9882 hits on average.
StDev: 1.078877730660788
% Hits to die: [(6, 0.47000000000000003), (7, 10.07), (8, 21.26), (9, 31.069999999999997), (10, 32.629999999999995), (11, 4.5)]
First injury in 7.802521008403361 hits on average.
Chance of first heavy injury in 8.40914318573893 hits on average.
122.8637794375 bonus armor from Forge on average.
-----
Swordmaster:
HP = 70, Helmet = 70, Armor = 115
Nimble%: 0.4
Death in 5.1162 hits on average.
StDev: 0.5029143587980249
% Hits to die: [(3, 0.02), (4, 7.449999999999999), (5, 73.42), (6, 19.11)]
First injury in 3.3558 hits on average.
No chance of heavy injury.
-----
Master Archer:
HP = 80, Helmet = 30, Armor = 115
Nimble%: 0.4
Death in 5.7041 hits on average.
StDev: 0.47219221356207774
% Hits to die: [(4, 0.73), (5, 28.13), (6, 71.14)]
First injury in 3.5430775395712284 hits on average.
No chance of heavy injury.
-----
Nomad Outlaw:
HP = 75, Helmet = 125, Armor = 105
Death in 3.0188 hits on average.
StDev: 0.5277067437893361
% Hits to die: [(2, 13.0), (3, 72.11999999999999), (4, 14.879999999999999)]
First injury in 1.6801 hits on average.
Chance of first heavy injury in 2.6818643493962306 hits on average.
-----
Conscript:
HP = 55, Helmet = 105, Armor = 110
Nimble%: 0.41000000000000003
Death in 4.549 hits on average.
StDev: 0.5822653203569048
% Hits to die: [(3, 2.93), (4, 40.88), (5, 54.55), (6, 1.6400000000000001)]
First injury in 3.5875 hits on average.
Chance of first heavy injury in 4.059981960312688 hits on average.
-----
Officer:
HP = 100, Helmet = 290, Armor = 290
Death in 7.7588 hits on average.
StDev: 1.0411200473986224
% Hits to die: [(5, 0.48), (6, 12.920000000000002), (7, 25.729999999999997), (8, 33.77), (9, 25.31), (10, 1.79)]
First injury in 7.063023936976063 hits on average.
Chance of first heavy injury in 7.479829904608666 hits on average.
113.2720195625 bonus armor from Forge on average.
-----
Assassin - Heavy:
HP = 80, Helmet = 140, Armor = 120
Nimble%: 0.4
Death in 5.9428 hits on average.
StDev: 0.6149520116217686
% Hits to die: [(4, 0.8699999999999999), (5, 19.32), (6, 64.47), (7, 15.340000000000002)]
First injury in 3.8897 hits on average.
No chance of heavy injury.
-----
167.38670000000002 hits to kill total against this test group.
5.579556666666667 hits to kill on average against this test group.
"""
        with subprocess.Popen(
                ['python', '../BBAttackerVsEnemies.py'],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                env={**os.environ, 'TEST': ''}
        ) as p:
            stdout = p.stdout.read().decode('utf-8')
            self.maxDiff = None
            self.assertEqual(original_stdout, stdout)
