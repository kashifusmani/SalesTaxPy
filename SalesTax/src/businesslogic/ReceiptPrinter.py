'''
Created on Jun 23, 2014

@author: kashifu
'''
from businessobjects.Item import Item
from businessobjects.ItemOrigin import ItemOrigin
from businessobjects.ItemType import ItemType
from businesslogic.TaxManager import TaxManager
from decimal import Decimal
from businesslogic.ReceiptCalculator import ReceiptCalculator
class ReceiptPrinter(object):
    '''
    classdocs
    '''

    def __init__(self, receiptCalculator):
        '''
        Constructor
        '''
        self.receiptCalculator = receiptCalculator
        
    @property
    def getReceiptCalculator(self):
        return self.receiptCalculator
    
    def printReceipt(self, itemList):
        receipt = self.getReceiptCalculator.calculateReceipt(itemList)
        receiptStr = ''
        for receiptEntry in receipt.getReceiptEntryList:
            receiptStr += '1 '
            if (receiptEntry.getItem.getItemOrigin == ItemOrigin.IMPORTED):
                receiptStr += receiptEntry.getItem.getItemOrigin.name + ' '
            receiptStr += receiptEntry.getItem.getItemDescription + " : "
            receiptStr += str(receiptEntry.getTotalPrice) + '\n'
        receiptStr += 'Sales Tax: ' + str(receipt.getTotalReceiptSalestax) + '\n'
        receiptStr += 'Total: ' + str(receipt.getTotalReceiptPrice)
        print(receiptStr)
        return receiptStr
    
if __name__ == "__main__":
    itemOne = Item(ItemOrigin.IMPORTED, ItemType.PERFUME, Decimal(27.99), "perfume")
    itemTwo = Item(ItemOrigin.NON_IMPORTED, ItemType.PERFUME, Decimal(18.99), "perfume")
    itemThree = Item(ItemOrigin.NON_IMPORTED, ItemType.MEDICAL_PRODUCT, Decimal(9.75), "medicine")
    itemFour = Item(ItemOrigin.IMPORTED, ItemType.FOOD, Decimal(11.25), "chocolate")
    taxManager = TaxManager()
    receiptCalculator = ReceiptCalculator(taxManager)
    receiptPrinter = ReceiptPrinter(receiptCalculator)
    receiptPrinter.printReceipt([itemOne, itemTwo, itemThree, itemFour])