'''
Created on Jun 22, 2014

@author: kashifu
'''
from enum import Enum
class ItemOrigin(Enum):
    '''
    classdocs
    '''
    IMPORTED = (True)
    NON_IMPORTED = (False)

    def __init__(self, isImportDutyTaxable):
        '''
        Constructor
        '''
        self.isImportDutyTaxable = isImportDutyTaxable
    @property
    def getIsImportDutyTaxable(self):
        return self.isImportDutyTaxable