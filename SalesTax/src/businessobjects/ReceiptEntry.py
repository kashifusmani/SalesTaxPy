'''
Created on Jun 23, 2014

@author: kashifu
'''

class ReceiptEntry(object):
    '''
    classdocs
    '''


    def __init__(self, item, itemSalesTax, totalPrice):
        '''
        Constructor
        '''
        self.item = item
        self.itemSalesTax = itemSalesTax
        self.totalPrice = totalPrice
    
    @property
    def getItem(self):
        return self.item
    @property
    def getItemSalesTax(self):
        return self.itemSalesTax
    @property
    def getTotalPrice(self):
        return self.totalPrice