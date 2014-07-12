'''
Created on Jun 24, 2014

@author: kashifu
'''
import unittest
from businessobjects.ItemOrigin import ItemOrigin

class ItemOriginTest(unittest.TestCase):


    def testImportedIsDutyTaxable(self):     
        self.assertEqual(ItemOrigin.IMPORTED.getIsImportDutyTaxable, True)
    
    def testLocalIsNotDutyTaxable(self):
        self.assertEqual(ItemOrigin.NON_IMPORTED.getIsImportDutyTaxable, False)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()