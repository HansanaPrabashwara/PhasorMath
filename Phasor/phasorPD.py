from .conversions import *
from Phasor.phasor import Phasor
import numpy as np


class PhasorPD(Phasor):
    
    def __init__(self,modulus, degree, roundOff = 2):
        self.modulus = modulus
        self.degree = degree % 360
        self.radian = PolarDegreeToPolarRadians(degree)  % (2*np.pi)
        self.complex = PolarDegreeToRectangle(modulus, degree)
        self.roundOff = roundOff


    # operations

    def __add__(self, other):
        """Add phasor instances"""
        if isinstance(other, Phasor):
            mod, deg = RectangularToPolarDegree(self.complex+other.complex)
            return PhasorPD(mod,deg, self.roundOff)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Addition can only be performed with Phasor instances.")

    
    def __sub__(self, other):
        """Substract phasor instances"""
        if(isinstance(other, Phasor)):
            mod, deg = RectangularToPolarDegree(self.complex-other.complex)
            return PhasorPD(mod,deg, self.roundOff)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Substraction can only be performed with Phasor instances.")


    def __mul__(self, other):
        """Multiply phashor instances"""
        if(isinstance(other, Phasor)):
            mod, deg = RectangularToPolarDegree(self.complex * other.complex)
            return PhasorPD(mod,deg, self.roundOff)
        elif isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            mod, deg = RectangularToPolarDegree(self.complex * other)
            return PhasorPD(mod,deg, self.roundOff)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Multiplication can only be performed with Phasor instances.")


    def __truediv__(self, other):
        """Divide phashor Instances"""
        if(isinstance(other, Phasor)):
            if other.complex == 0:
                raise ZeroDivisionError("Divisor phasor is zero")
            else:
                mod, deg = RectangularToPolarDegree(self.complex / other.complex)
                return PhasorPD(mod,deg, self.roundOff)
        elif isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            if other == 0:
                raise ZeroDivisionError("Divisor is zero")
            else:
                mod, deg = RectangularToPolarDegree(self.complex / other)
                return PhasorPD(mod,deg, self.roundOff)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Division can only be performed with Phasor instances.")


    def __pow__(self, power):
        """Provide the power functionality for phasors"""
        mod, deg = RectangularToPolarDegree(self.complex ** power)
        return PhasorPD(mod,deg, self.roundOff)
       

    def __invert__(self):
        "Find the complex conjugate of the phasor by ' ` ' "
        return PhasorPD(self.modulus, self.degree, self.roundOff)
    
    
    def __str__(self):
        mod,ang = RectangularToPolarDegree(self.complex)
        return f"{round(mod,self.roundOff)} \u2220 {round(ang,self.roundOff)}\u00b0"
    

    def __repr__(self):
        mod,ang = RectangularToPolarDegree(self.complex)
        return f"{round(mod,self.roundOff)} \u2220 {round(ang,self.roundOff)}\u00b0"

    