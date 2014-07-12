'''
Created on Jun 22, 2014

@author: kashifu
'''
from decimal import Decimal
from decimal import getcontext
import math


class TaxManager(object):
    '''
    classdocs
    '''

    SALES_TAX_RATE = Decimal(0.1)
    IMPORT_DUTY_TAX_RATE = Decimal(0.05)
    ROUND_UP_FACTOR = Decimal(0.05)
    getcontext().prec = 4
    def __init__(self):
        '''
        Constructor
        '''
    def calculateTax(self, item):
        totalTax = Decimal(0)
        # if the item is sales taxable or not
        if(item.getItemType.getIsSalesTaxable):
            totalTax = totalTax + self.__calculateSalesTax__(item.getItemPrice)
        # if item is duty taxable or not
        if(item.getItemOrigin.getIsImportDutyTaxable):
            totalTax = totalTax + self.__caclulateImportDutyTax__(item.getItemPrice)
        totalTax = self.__roundUpToNearestFactor__(totalTax)
        return self.__truncate__(totalTax)
        
    
    def __calculateSalesTax__(self, basePrice):
        return basePrice * self.SALES_TAX_RATE
    
    def __caclulateImportDutyTax__(self, basePrice):
        return basePrice * self.IMPORT_DUTY_TAX_RATE
    
    def __roundUpToNearestFactor__(self, salesTax):
        return (math.ceil(salesTax / (self.ROUND_UP_FACTOR))) * self.ROUND_UP_FACTOR
    
    def __truncate__(self, salesTax):
        return Decimal('%.2f' % salesTax)
    
    
