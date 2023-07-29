from .conversions import *
from Phasor.phasor import Phasor
import numpy as np


class PhasorPR(Phasor):
    
    def __init__(self,modulus, radian, roundOff = 2):
        self.modulus = modulus
        self.radian = radian % (2*np.pi)
        self.degree = PolarRadiansToPolarDegree(radian)  % 360
        self.complex = PolarRadiansToRectangular(modulus, radian)
        self.roundOff = roundOff


     # operations

    def __add__(self, other):
        """Add phasor instances"""
        if isinstance(other, Phasor):
            mod, rad = RectangularToPolarRadians(self.complex+other.complex)
            return PhasorPR(mod,rad, self.roundOff)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Addition can only be performed with Phasor instances.")

    
    def __sub__(self, other):
        """Substract phasor instances"""
        if(isinstance(other, Phasor)):
            mod, rad = RectangularToPolarRadians(self.complex-other.complex)
            return PhasorPR(mod,rad, self.roundOff)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Substraction can only be performed with Phasor instances.")


    def __mul__(self, other):
        """Multiply phashor instances"""
        if(isinstance(other, Phasor)):
            mod, rad = RectangularToPolarDegree(self.complex * other.complex)
            return PhasorPR(mod, rad, self.roundOff)
        elif isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            mod, rad = RectangularToPolarDegree(self.complex * other)
            return PhasorPR(mod, rad, self.roundOff)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Multiplication can only be performed with Phasor instances.")


    def __truediv__(self, other):
        """Divide phashor Instances"""
        if(isinstance(other, Phasor)):
            if other.complex == 0:
                raise ZeroDivisionError("Divisor phasor is zero")
            else:
                mod, rad = RectangularToPolarRadians(self.complex / other.complex)
                return PhasorPR(mod,rad, self.roundOff)
        elif isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            if other == 0:
                raise ZeroDivisionError("Divisor is zero")
            else:
                mod, rad = RectangularToPolarRadians(self.complex / other)
                return PhasorPR(mod,rad, self.roundOff)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Division can only be performed with Phasor instances.")


    def __pow__(self, power):
        """Provide the power functionality for phasors"""
        mod, rad = RectangularToPolarRadians(self.complex ** power)
        return PhasorPR(mod ,rad, self.roundOff)
       

    def __invert__(self):
        "Find the complex conjugate of the phasor by ' ` ' "
        return PhasorPR(self.modulus, -self.radian, self.roundOff)
    
    
    def __str__(self):
        mod,ang = RectangularToPolarRadians(self.complex)
        return f"{round(mod,self.roundOff)} \u2220 {round(ang,self.roundOff)} \u33AD"
    

    def __repr__(self):
        mod,ang = RectangularToPolarRadians(self.complex)
        return f"{round(mod,self.roundOff)} \u2220 {round(ang,self.roundOff)} \u00b0"



    