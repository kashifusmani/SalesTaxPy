'''
Created on Jun 24, 2014

@author: kashifu
'''
import unittest
from businessobjects.Item import Item
from businessobjects.ItemOrigin import ItemOrigin
from businessobjects.ItemType import ItemType
from decimal import Decimal
from businesslogic.TaxManager import TaxManager
from decimal import getcontext

class TaxManagerTest(unittest.TestCase):
        
    def testImportedNotSalesTaxableItemTax(self):
        taxManager = TaxManager()
        itemPrice = Decimal(20)
        itemDescription = "box of chocolate"
        item = Item(ItemOrigin.IMPORTED, ItemType.FOOD, itemPrice, itemDescription)
        tax = taxManager.calculateTax(item)
        self.assertEqual(tax, Decimal(1))
    
    def testImportedAndSalesTaxableItemTax(self):
        taxManager = TaxManager()
        itemPrice = Decimal(200)
        itemDescription = "box of chocolate"
        item = Item(ItemOrigin.IMPORTED, ItemType.PERFUME, itemPrice, itemDescription)
        tax = taxManager.calculateTax(item)
        self.assertEqual(tax, Decimal(30.00))
    
    def testNonImportedNotSalesTaxableItemTax(self):
        taxManager = TaxManager()
        itemPrice = Decimal(20)
        itemDescription = "box of chocolate"
        item = Item(ItemOrigin.NON_IMPORTED, ItemType.FOOD, itemPrice, itemDescription)
        tax = taxManager.calculateTax(item)
        self.assertEqual(tax, Decimal(0))
    
    def testNonImportedSalesTaxableItemTax(self):
        taxManager = TaxManager()
        itemPrice = Decimal(200)
        itemDescription = "box of chocolate"
        item = Item(ItemOrigin.NON_IMPORTED, ItemType.PERFUME, itemPrice, itemDescription)
        tax = taxManager.calculateTax(item)
        self.assertEqual(tax, Decimal(20.00))
    
    def testCalculatedTaxIsRoundedToNearestPointFive(self):
        taxManager = TaxManager()
        itemPrice = Decimal(199.4)
        itemDescription = "box of chocolate"
        item = Item(ItemOrigin.NON_IMPORTED, ItemType.PERFUME, itemPrice, itemDescription)
        tax = taxManager.calculateTax(item)
        '''The actual tax on this item 10% of 199.4 which is 19.94, but our algorithm should 
        return 19.95 instead'''
        getcontext().prec = 4
        self.assertEqual(tax, Decimal(19.95))
        
    def testCalculatedTaxDoesNotContainMoreThanTwoNumbersAfterDecimal(self):
        pass
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()