'''
Created on Jun 24, 2014

@author: kashifu
'''
import unittest
from businessobjects.Item import Item
from businessobjects.ItemOrigin import ItemOrigin
from businessobjects.ItemType import ItemType
from decimal import Decimal

class ItemTest(unittest.TestCase):


    def testConstructorAndProperties(self):
        itemPrice = Decimal(20)
        itemDescription = "box of chocolate"
        item = Item(ItemOrigin.IMPORTED, ItemType.FOOD, itemPrice, itemDescription)
        self.assertEquals(item.getItemOrigin, ItemOrigin.IMPORTED)
        self.assertEquals(item.getItemType, ItemType.FOOD)
        self.assertEquals(item.getItemPrice, itemPrice)
        self.assertEquals(item.getItemDescription, itemDescription)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()