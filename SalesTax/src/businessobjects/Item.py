'''
Created on Jun 22, 2014

@author: kashifu
'''

class Item(object):
    '''
    classdocs
    '''


    def __init__(self, itemOrigin, itemType, itemPrice, itemDescription):
        '''
        Constructor
        '''
        self.itemOrigin = itemOrigin
        self.itemType = itemType
        self.itemPrice = itemPrice
        self.itemDescription = itemDescription
        
    @property
    def getItemPrice(self):
        return self.itemPrice
    @property
    def getItemOrigin(self):
        return self.itemOrigin
    @property
    def getItemType(self):
        return self.itemType
    @property
    def getItemDescription(self):
        return self.itemDescription

# make private method name start with __as__