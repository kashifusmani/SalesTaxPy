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
from businessobjects.Receipt import Receipt

class ReceiptTest(unittest.TestCase):


    def testConstructorAndProperties(self):
        itemPrice = Decimal(20)
        itemDescription = "box of chocolate"
        item = Item(ItemOrigin.IMPORTED, ItemType.FOOD, itemPrice, itemDescription)
        itemSalesTax = Decimal(1)
        totalPrice = Decimal(21)
        receiptEntry = ReceiptEntry(item, itemSalesTax, totalPrice)
        totalReceiptSalesTax = Decimal(1)
        totalReceiptPrice = Decimal(21)
        receipt = Receipt([receiptEntry], totalReceiptSalesTax, totalReceiptPrice)
        self.assertEqual(receipt.getReceiptEntryList.__len__(), 1)
        self.assertEquals(receipt.getTotalReceiptSalestax, totalReceiptSalesTax)
        self.assertEquals(receipt.getTotalReceiptPrice, totalReceiptPrice)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()