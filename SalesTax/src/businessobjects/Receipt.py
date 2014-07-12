'''
Created on Jun 23, 2014

@author: kashifu
'''

class Receipt(object):
    '''
    classdocs
    '''


    def __init__(self, receiptEntryList, totalReceiptSalesTax, totalReceiptPrice):
        '''
        Constructor
        '''
        self.receiptEntryList = receiptEntryList
        self.totalReceiptSalesTax = totalReceiptSalesTax
        self.totalReceiptPrice = totalReceiptPrice
        
    @property
    def getReceiptEntryList(self):
        return self.receiptEntryList
    @property
    def getTotalReceiptSalestax(self):
        return self.totalReceiptSalesTax
    @property
    def getTotalReceiptPrice(self):
        return self.totalReceiptPrice
    