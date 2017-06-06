'''
Created on May 18, 2017

@author: dongi
'''


from operator import itemgetter
from itertools import combinations
from ..adjustModel import AdjustModel

class ShiftAdjustModel(AdjustModel):
    def __init__(self, row_length, col_length, headerdata, parent = None):
        super().__init__(row_length, col_length, headerdata, parent)
    
    def getContractData(self, name):
        return self.contractDataDict[name].getContractData()
                 
