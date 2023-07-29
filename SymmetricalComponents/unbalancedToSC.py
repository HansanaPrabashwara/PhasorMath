from Phasor.phasor import Phasor
from Phasor.phasorPD import PhasorPD
import numpy as np
from Phasor.phasorConvertions import *

class unbalancedToSC:
    def __init__(self,A,B,C, roundOff=2):
        if isinstance(A, Phasor):
            self.A = A
            if isinstance(B, Phasor):
                self.B = B
                if isinstance(C, Phasor):
                    self.C = C
                else:
                    raise TypeError(f"Unsupported argument type: {type(C)}.")
            else:
                raise TypeError(f"Unsupported argument type: {type(B)}.")
        else:
            raise TypeError(f"Unsupported argument type: {type(A)}.") 

        self.roundOff = roundOff
        self.deltaInverse = np.array([
                [PhasorPD(1,0,self.roundOff), PhasorPD(1,0,self.roundOff),PhasorPD(1,0,self.roundOff)],
                [PhasorPD(1,0,self.roundOff), PhasorPD(1,120,self.roundOff),PhasorPD(1,120,self.roundOff)**2],
                [PhasorPD(1,0,self.roundOff), PhasorPD(1,120,self.roundOff)**2,PhasorPD(1,120,self.roundOff)]
            ], dtype=Phasor)/3
        
        self.threePhasors = np.array([self.A,self.B,self.C], dtype=Phasor)
        self.components = np.dot(self.deltaInverse, self.threePhasors)

        self.zero = [self.components[0],self.components[0],self.components[0]]
        self.positive = [self.components[1],self.components[1]*PhasorPD(1,120,self.roundOff),self.components[1]*(PhasorPD(1,120,self.roundOff)**2)]
        self.negative = [self.components[2],self.components[2]*(PhasorPD(1,120,self.roundOff)**2),self.components[2]*PhasorPD(1,120,self.roundOff)]
        
        self.allComponents = [self.zero,self.positive,self.negative]
        


    def toRecList(self):
        RecList = []
        for i in self.components:
            RecList.append(toRec(i))
        self.components = RecList
    

    def toRadList(self):
        RadList = []
        for i in self.components:
            RadList.append(toRad(i))
        self.components = RadList
    

    def toDegList(self):
        DegList = []
        for i in self.components:
            DegList.append(toDeg(i))
        self.components = DegList


    def zero(self):
        return f"""Zero Symmetric Components :
    A0 - {self.zero[0]}
    B0 - {self.zero[1]}
    C0 - {self.zero[2]}   

"""
    
    def positive(self):
        return f"""Positive Symmetric Components :
    A1 - {self.positive[0]}
    B1 - {self.positive[1]}
    C1 - {self.positive[2]}

"""
    
    def negative(self):
        return f"""Negative Symmetric Components :
    A2 - {self.negative[0]}
    B2 - {self.negative[1]}
    C2 - {self.negative[2]}

"""


    def __str__(self):
        return f"""
    A0 - {self.zero[0]}
    A1 - {self.positive[0]}
    A2 - {self.negative[0]}

    B0 - {self.zero[1]}
    B1 - {self.positive[1]}
    B2 - {self.negative[1]}

    C0 - {self.zero[2]}
    C1 - {self.positive[2]}
    C2 - {self.negative[2]}

"""

    def __repr__(self):
         return f"""
    A0 - {self.zero[0]}
    A1 - {self.positive[0]}
    A2 - {self.negative[0]}

    B0 - {self.zero[1]}
    B1 - {self.positive[1]}
    B2 - {self.negative[1]}

    C0 - {self.zero[2]}
    C1 - {self.positive[2]}
    C2 - {self.negative[2]}

"""
