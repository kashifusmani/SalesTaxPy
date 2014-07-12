'''
Created on Jun 24, 2014

@author: kashifu
'''
import unittest
from businessobjects.ItemType import ItemType

class ItemTypeTest(unittest.TestCase):


    def testFoodNotSalesTaxable(self):
        self.assertEqual(ItemType.FOOD.getIsSalesTaxable, False)
        
    def testMedicineNotSalesTaxable(self):
        self.assertEqual(ItemType.MEDICAL_PRODUCT.getIsSalesTaxable, False)
        
    def testOtherProductsSalesTaxable(self):
        self.assertEqual(ItemType.OTHER.getIsSalesTaxable, True)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()