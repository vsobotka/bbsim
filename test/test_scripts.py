import os
import subprocess
import unittest

from test.original_outputs import BB1HanderBattery_original_output, BB2HanderBattery_original_stdout, \
    BBAttackerVsEnemies_original_stdout, BBCalc_original_stdout, BBEnemiesVsDefender_original_stdout, \
    BBHitChance_original_stdout, BBNimbleBattery_original_stdout, BBRaisingHp_original_stdout


class TestBBCalc(unittest.TestCase):
    def run_script_test(self, original_stdout, script):
        with subprocess.Popen(
                ['python', '-c',
                 'from python.{script} import {script}; {script}(random_seed="battlebrothers")'.format(script=script)],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
        ) as p:
            stdout = p.stdout.read().decode('utf-8')
            self.maxDiff = None
            self.assertEqual(original_stdout, stdout)

    def run_direct_test(self, original_stdout, script):
        with subprocess.Popen(
                ['python', '../python/{script}.py'.format(script=script)],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                env={**os.environ, 'TEST': ''}
        ) as p:
            stdout = p.stdout.read().decode('utf-8')
            self.maxDiff = None
            self.assertEqual(original_stdout, stdout)

    def test_BB1HanderBattery(self):
        self.run_script_test(BB1HanderBattery_original_output, 'BB1HanderBattery')

    def test_BB2HanderBattery(self):
        self.run_script_test(BB2HanderBattery_original_stdout, 'BB2HanderBattery')

    def test_BBAttackerVsEnemies(self):
        self.run_script_test(BBAttackerVsEnemies_original_stdout, 'BBAttackerVsEnemies')

    def test_BBCalc(self):
        self.run_script_test(BBCalc_original_stdout, 'BBCalc')

    def test_BBEnemiesVsDefender(self):
        self.run_direct_test(BBEnemiesVsDefender_original_stdout, 'BBEnemiesVsDefender')

    def test_BBHitChance(self):
        self.run_direct_test(BBHitChance_original_stdout, 'BBHitChance')

    def test_NimbleBattery(self):
        self.run_direct_test(BBNimbleBattery_original_stdout, 'BBNimbleBattery')

    def test_BBRaisingHp(self):
        self.run_direct_test(BBRaisingHp_original_stdout, 'BBRaisingHp')
