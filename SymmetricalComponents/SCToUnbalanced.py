from Phasor.phasor import Phasor
from Phasor.phasorPD import PhasorPD
import numpy as np
from Phasor.phasorConvertions import *

class SCToUnbalanced:
    def __init__(self,A0,A1,A2, roundOff=2):
        if isinstance(A0, Phasor):
            self.A0 = A0
            if isinstance(A1, Phasor):
                self.A1 = A1
                if isinstance(A2, Phasor):
                    self.A2 = A2
                else:
                    raise TypeError(f"Unsupported argument type: {type(A2)}.")
            else:
                raise TypeError(f"Unsupported argument type: {type(A1)}.")
        else:
            raise TypeError(f"Unsupported argument type: {type(A0)}.") 

        self.roundOff = roundOff
        self.delta = np.array([
                [PhasorPD(1,0,self.roundOff), PhasorPD(1,0,self.roundOff),PhasorPD(1,0,self.roundOff)],
                [PhasorPD(1,0,self.roundOff), PhasorPD(1,120,self.roundOff)**2,PhasorPD(1,120,self.roundOff)],
                [PhasorPD(1,0,self.roundOff), PhasorPD(1,120,self.roundOff),PhasorPD(1,120,self.roundOff)**2]  
            ], dtype=Phasor)
        
        self.threeComponents = np.array([self.A0,self.A1,self.A2], dtype=Phasor)
        self.unbalanced = np.dot(self.delta, self.threeComponents)
        

    def toRecList(self):
        RecList = []
        for i in self.unbalanced:
            RecList.append(toRec(i))
        self.unbalanced = RecList
    

    def toRadList(self):
        RadList = []
        for i in self.unbalanced:
            RadList.append(toRad(i))
        self.unbalanced = RadList
    

    def toDegList(self):
        DegList = []
        for i in self.unbalanced:
            DegList.append(toDeg(i))
        self.unbalanced = DegList


    def __str__(self):
        return f"""
    A - {self.unbalanced[0]}
    B - {self.unbalanced[1]}
    C - {self.unbalanced[2]}

"""

    def __repr__(self):
        return f"""
    A - {self.unbalanced[0]}
    B - {self.unbalanced[1]}
    C - {self.unbalanced[2]}

"""
