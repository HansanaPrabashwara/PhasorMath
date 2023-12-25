"""Convert symmetrical components to unbalanced three phase and convert unbalanced three phase to symmetrical components."""

from .phasor import *
import numpy as np

class SCtoU:
    """Generate the corresponding unbalanced three-phase system using symmetrical components.
    """
    def __init__(self,A0,A1,A2, roundOff=2):
        """Initalizes SCToUnbalanced objects

        Args:
            A0 (Phasor): Zero component of A
            A1 (Phasor): Positive component of A
            A2 (Phasor): Negative component of A
            roundOff (int, optional): Amount of decimal points to be rounded off. Defaults to 2.

        Raises:
            TypeError: If A1 is not a Phasor object 
            TypeError: If A2 is not a Phasor object
            TypeError: If A3 is not a Phasor object
        """
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
        """Convert all Phasor objects to rectangular coordinates.
        """
        RecList = []
        for i in self.unbalanced:
            RecList.append(toRec(i))
        self.unbalanced = RecList
    

    def toRadList(self):
        """Convert all Phasor objects to polar coordinates where angle is in radians.
        """
        RadList = []
        for i in self.unbalanced:
            RadList.append(toRad(i))
        self.unbalanced = RadList
    

    def toDegList(self):
        """Convert all Phasor objects to polar coordinates where angle is in degrees.
        """
        DegList = []
        for i in self.unbalanced:
            DegList.append(toDeg(i))
        self.unbalanced = DegList


    def __str__(self):
        """Return the unbalanced system in a String format

        Returns:
            String: Unbalanced three-phase system 
        """        
        return f"""
    A - {self.unbalanced[0]}
    B - {self.unbalanced[1]}
    C - {self.unbalanced[2]}

"""

    def __repr__(self):
        """Return the unbalanced system in a String format

        Returns:
            String: Unbalanced three-phase system 
        """   
        return f"""
    A - {self.unbalanced[0]}
    B - {self.unbalanced[1]}
    C - {self.unbalanced[2]}

"""




class UtoSC:
    """Convert unbalanced three phase system int symmetrical components.
    """
    def __init__(self,A,B,C, roundOff=2):
        """Initialize unblancedToSC objects

        Args:
            A (Phasor): Phasor A
            B (Phasor): Phasor B
            C (Phasor): Phasor C
            roundOff (int, optional): Number of decimat points to be roundoff. Defaults to 2.

        Raises:
            TypeError: if A is not a Phasor object
            TypeError: if B is not a Phasor object
            TypeError: if C is not a Phasor object
        """
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
        """Convert all Phasor objects to rectangular coordinates.
        """
        RecList = []
        for i in self.components:
            RecList.append(toRec(i))
        self.components = RecList
    

    def toRadList(self):
        """Convert all Phasor objects to polar coordinates where angle is in radians.
        """
        RadList = []
        for i in self.components:
            RadList.append(toRad(i))
        self.components = RadList
    

    def toDegList(self):
        """Convert all Phasor objects to polar coordinates where angle is in degrees.
        """
        DegList = []
        for i in self.components:
            DegList.append(toDeg(i))
        self.components = DegList


    def zero(self):
        """Print zero components 

        Returns:
            String: Zero components
        """        
        return f"""Zero Symmetric Components :
    A0 - {self.zero[0]}
    B0 - {self.zero[1]}
    C0 - {self.zero[2]}   

"""
    
    def positive(self):
        """Print positive components

        Returns:
            String: Positive components
        """        
        return f"""Positive Symmetric Components :
    A1 - {self.positive[0]}
    B1 - {self.positive[1]}
    C1 - {self.positive[2]}

"""
    
    def negative(self):
        """Print negative components

        Returns:
            String: Negative components
        """        
        return f"""Negative Symmetric Components :
    A2 - {self.negative[0]}
    B2 - {self.negative[1]}
    C2 - {self.negative[2]}

"""


    def __str__(self):
        """Print all symmetrical components

        Returns:
            String: All symmetrical components
        """        
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
         """Print all symmetrical components

        Returns:
            String: All symmetrical components
        """  
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
