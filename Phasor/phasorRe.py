from .conversions import *
from Phasor.phasor import Phasor
import numpy as np


class PhasorRe(Phasor):
    
    def __init__(self,complex, roundOff = 2):
        self.complex = complex
        self.modulus,self.radian = RectangularToPolarRadians(complex) 
        self.radian = self.radian % (2 * np.pi)
        self.degree = PolarRadiansToPolarDegree(self.radian) % 360
        self.roundOff = roundOff


    # operations

    def __add__(self, other):
        """Add phasor instances"""
        if isinstance(other, Phasor):
            return PhasorRe(self.complex + other.complex, self.roundOff)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Addition can only be performed with Phasor instances.")

    
    def __sub__(self, other):
        """Substract phasor instances"""
        if(isinstance(other, Phasor)):
            return PhasorRe(self.complex - other.complex ,  self.roundOff)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Substraction can only be performed with Phasor instances.")


    def __mul__(self, other):
        """Multiply phashor instances"""
        if(isinstance(other, Phasor)):
            return PhasorRe(self.complex * other.complex,  self.roundOff)
        elif isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            return PhasorRe(self.complex * other)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Multiplication can only be performed with Phasor instances or numbers.")


    def __truediv__(self, other):
        """Divide phashor Instances"""
        if(isinstance(other, Phasor)):
            if other.complex == 0:
                raise ZeroDivisionError("Divisor phasor is zero")
            else:
                return PhasorRe(self.complex / other.complex,  self.roundOff)
        elif isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            if other == 0:
                raise ZeroDivisionError("Divisor is zero")
            else:
                return PhasorRe(self.complex * other)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Division can only be performed with Phasor instances or numbers.")


    def __pow__(self, value):
        """Provide the power functionality for phasors"""
        return PhasorRe(self.complex ** value,  self.roundOff)
       

    def __invert__(self):
        "Find the complex conjugate of the phasor by ' ` ' "
        return PhasorRe(np.conjugate(self.complex), self.roundOff)
    

    def __str__(self):
        return f"{complex(round(self.complex.real, self.roundOff),round(self.complex.imag, self.roundOff))}"
    

    def __repr__(self):
        return f"{complex(round(self.complex.real, self.roundOff),round(self.complex.imag, self.roundOff))}"


    