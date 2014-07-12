'''
Created on Jun 24, 2014

@author: kashifu
'''
import unittest
from businessobjects.Item import Item
from businessobjects.ItemOrigin import ItemOrigin
from businessobjects.ItemType import ItemType
from decimal import Decimal
from businessobjects.ReceiptEntry import ReceiptEntry

class ReceiptEntryTest(unittest.TestCase):


    def testConstructorAndProperties(self):
        itemPrice = Decimal(20)
        itemDescription = "box of chocolate"
        item = Item(ItemOrigin.IMPORTED, ItemType.FOOD, itemPrice, itemDescription)
        itemSalesTax = Decimal(1)
        totalPrice = Decimal(21)
        receiptEntry = ReceiptEntry(item, itemSalesTax, totalPrice)
        self.assertEqual(receiptEntry.getItem, item)
        self.assertEquals(receiptEntry.getItemSalesTax, itemSalesTax)
        self.assertEquals(receiptEntry.getTotalPrice, totalPrice)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()