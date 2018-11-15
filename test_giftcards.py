#!/usr/bin/env python
import sys
import subprocess
import unittest

class MainTest(unittest.TestCase):

    def test_find_prices(self):
        '''
        quick tests for finding two items
        :return:
        '''
        result = subprocess.check_output("python find_price.py prices.txt 2500").decode('utf-8').strip('\r\n')
        self.assertEqual('Candy Bar 500, Earmuffs 2000',result)
        result = subprocess.check_output("python find_price.py prices.txt 2300").decode('utf-8').strip('\r\n')
        self.assertEqual(result, 'Paperback Book 700, Headphones 1400')
        result = subprocess.check_output("python find_price.py prices.txt 10000").decode('utf-8').strip('\r\n')
        self.assertEqual(result, 'Earmuffs 2000, Bluetooth Stereo 6000')
        result = subprocess.check_output("python find_price.py prices.txt 1100").decode('utf-8').strip('\r\n')
        self.assertEqual(result, 'Not possible')

    def test_bonus(self):
        '''
        quick tests for finding three items
        :return:
        '''
        result = subprocess.check_output("python bonus.py prices.txt 2500").decode('utf-8').strip('\r\n')
        self.assertEqual('Candy Bar 500, Paperback Book 700, Detergent 1000',result)
        result = subprocess.check_output("python bonus.py prices.txt 2300").decode('utf-8').strip('\r\n')
        self.assertEqual(result, 'Candy Bar 500, Paperback Book 700, Detergent 1000')
        result = subprocess.check_output("python bonus.py prices.txt 10000").decode('utf-8').strip('\r\n')
        self.assertEqual(result, 'Headphones 1400, Earmuffs 2000, Bluetooth Stereo 6000')
        result = subprocess.check_output("python bonus.py prices.txt 1100").decode('utf-8').strip('\r\n')
        self.assertEqual(result, 'Not possible')
