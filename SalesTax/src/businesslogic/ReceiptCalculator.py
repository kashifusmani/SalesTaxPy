'''
Created on Jun 22, 2014

@author: kashifu
'''

from businessobjects.Receipt import  Receipt
from businessobjects.ReceiptEntry import ReceiptEntry


class ReceiptCalculator(object):
    
    def __init__(self, taxManager):
        self.taxManager = taxManager
        
    def printReceipt(self, itemList):
        receiptStr = ''
        totalSalesTax = 0
        totalCost = 0
        for item in itemList:
            itemSalesTax = self.taxManager.calculateTax(item)
            itemTotalCost = item.getItemPrice + itemSalesTax 
            receiptStr += '1 ' + item.getItemOrigin.name + ' ' + item.getItemType.name + ' : ' + str(itemTotalCost) + '\n'
            totalSalesTax += itemSalesTax
            totalCost += itemTotalCost
        receiptStr += 'Sales Tax: ' + str(totalSalesTax) +'\n'
        receiptStr += 'Total: ' + str(totalCost) +'\n'
        return receiptStr # return {totalSalesTax: .., blah}, let caller deal with printing 
    
    def calculateReceipt(self, itemList):        
        receiptEntryList = []
        totalReceiptSalesTax = 0
        totalReceiptPrice = 0
        
        for item in itemList:
            itemSalesTax = self.taxManager.calculateTax(item)
            itemTotalPrice = item.getItemPrice + itemSalesTax
            receiptEntry = ReceiptEntry(item, itemSalesTax, itemTotalPrice)
            receiptEntryList.append(receiptEntry)
            totalReceiptSalesTax += itemSalesTax
            totalReceiptPrice += itemTotalPrice
        receipt = Receipt(receiptEntryList, totalReceiptSalesTax, totalReceiptPrice)
        return receipt
    
    