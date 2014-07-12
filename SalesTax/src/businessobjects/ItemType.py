'''
Created on Jun 22, 2014

@author: kashifu
'''
from enum import Enum
class ItemType(Enum):
    '''
    classdocs
    '''
    FOOD = (False)
    MEDICAL_PRODUCT = (False)
    BOOK = (False)
    PERFUME = (True)
    OTHER = (True)
    
    def __init__(self, isSalesTaxable):
        '''
        Constructor
        '''
        self.isSalesTaxable = isSalesTaxable
    @property
    def getIsSalesTaxable(self):
        return self.isSalesTaxable
        