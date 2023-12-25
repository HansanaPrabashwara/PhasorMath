"""Create Phasor objects with different formats and provide capability to do basic phsor calculations.
"""

import numpy as np
from abc import ABC, abstractmethod
from .conversions import *

class Phasor(ABC):
    """An abstract class for Phasor objects

    Args:
        ABC (ABC): abc.ABC superclass
    """
    @abstractmethod
    def __init__(self):
        self.complex = 0
        self.modulus = 0
        self.radian = 0
        self.degree = 0
        self.roundOff = 2
        

class PhasorPD(Phasor):
    """Initialize Phasor objects in Polor Coordinates with degree as the angle unit

    Args:
        Phasor (Phasor): Abstract Phasor parent class
    """
    
    def __init__(self,modulus, degree, roundOff = 2):
        """Initiate PhasorPD objects

        Args:
            modulus (int/float): modulus 
            degree (_type_): angle in degrees
            roundOff (int, optional): Decimalpoints to be roundoff. Defaults to 2.
        """
        self.modulus = modulus
        self.degree = degree % 360
        self.radian = PolarDegreeToPolarRadians(degree)  % (2*np.pi)
        self.complex = PolarDegreeToRectangle(modulus, degree)
        self.roundOff = roundOff


    def __add__(self, other):
        """Add two phasor objects together wit '+' operator.

        Args:
            other (Phasor): Other Phasor object to be added

        Raises:
            TypeError: If the second object is not a Phasor object. 

        Returns:
            PhasorPD: Return addition.
        """
        if isinstance(other, Phasor):
            mod, deg = RectangularToPolarDegree(self.complex+other.complex)
            return PhasorPD(mod,deg, self.roundOff)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Addition can only be performed with Phasor instances.")

    
    def __sub__(self, other):
        """Substract of two phasor objects with '-' operatoe. 

        Args:
            other (Phasor): Other Phasor object to be substracted

        Raises:
            TypeError: If the second object is not a Phasor object. 

        Returns:
             Return the defference between the phasor objects.
        """
        if(isinstance(other, Phasor)):
            mod, deg = RectangularToPolarDegree(self.complex-other.complex)
            return PhasorPD(mod,deg, self.roundOff)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Substraction can only be performed with Phasor instances.")


    def __mul__(self, other):
        """Multiply the Phasor object with another Phasor object or with a numerical object together with '*' operator 

        Args:
            other (Phasor): Other Phasor object to be added

        Raises:
            TypeError: If the second object is not a Phasor object or numerical object. 

        Returns:
            PhasorPD: Returns multipication of the phasor object with another Phasor object or another numerical object.
        """
        if(isinstance(other, Phasor)):
            mod, deg = RectangularToPolarDegree(self.complex * other.complex)
            return PhasorPD(mod,deg, self.roundOff)
        elif isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            mod, deg = RectangularToPolarDegree(self.complex * other)
            return PhasorPD(mod,deg, self.roundOff)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Multiplication can only be performed with Phasor instances or with numerical instances.")


    def __truediv__(self, other):
        """Divide the Phasor object with another Phasor object or with a numerical object together with '*' operator 

        Args:
            other (Phasor/float/int/complex): Phasor object or the numerical value as the divisor

        Raises:
            ZeroDivisionError: If the divisor is Phasor object and value is zero 
            ZeroDivisionError: If the divisor is numerical object and value is zero
            TypeError: If the divisor object is not a Phasor object or a numerical object

        Returns:
            PhasorPD: Returns the division of the Phasor object with the divisor object
        """
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
        """Returns the power of an phasor object by using '**' operator

        Args:
            power (int/float): The exponent 

        Returns:
            PhasorPD: Returns the power of the Phasor
        """
        mod, deg = RectangularToPolarDegree(self.complex ** power)
        return PhasorPD(mod,deg, self.roundOff)
       

    def __invert__(self):
        """Return the complex conjugate of the Phasor object.

        Returns:
            PhasorPD: Returns the conjugate. 
        """
        return PhasorPD(self.modulus, self.degree, self.roundOff)
    
    
    def __str__(self):
        """Return information of Phasor object

        Returns:
            String: Returns modulus and angle in degree
        """
        mod,ang = RectangularToPolarDegree(self.complex)
        return f"{round(mod,self.roundOff)} \u2220 {round(ang,self.roundOff)}\u00b0"
    

    def __repr__(self):
        """Return information of Phasor object

        Returns:
            String: Returns modulus and angle in degree
        """
        mod,ang = RectangularToPolarDegree(self.complex)
        return f"{round(mod,self.roundOff)} \u2220 {round(ang,self.roundOff)}\u00b0"



class PhasorPR(Phasor):
    """Initialize Phasor objects in Polor Coordinates with radians as the angle unit

    Args:
        Phasor (Phasor): Abstract Phasor parent class
    """
    def __init__(self,modulus, radian, roundOff = 2):
        """Initiate PhasorPR objects

        Args:
            modulus (int/float): modulus 
            radian (int/float): angle in radians
            roundOff (int, optional): Decimalpoints to be roundoff. Defaults to 2.
        """
        self.modulus = modulus
        self.radian = radian % (2*np.pi)
        self.degree = PolarRadiansToPolarDegree(radian)  % 360
        self.complex = PolarRadiansToRectangular(modulus, radian)
        self.roundOff = roundOff



    def __add__(self, other):
        """Add two phasor objects together with '+' operator.

        Args:
            other (Phasor): Other Phasor object to be added

        Raises:
            TypeError: If the second object is not a Phasor object. 

        Returns:
            PhasorPR: Returns addition.
        """
        if isinstance(other, Phasor):
            mod, rad = RectangularToPolarRadians(self.complex+other.complex)
            return PhasorPR(mod,rad, self.roundOff)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Addition can only be performed with Phasor instances.")

    
    def __sub__(self, other):
        """Substract of two phasor objects with '-' operator. 

        Args:
            other (Phasor): Other Phasor object to be substracted

        Raises:
            TypeError: If the second object is not a Phasor object. 

        Returns:
            PhasorPR:  Return the defference between the phasor objects.
        """
        if(isinstance(other, Phasor)):
            mod, rad = RectangularToPolarRadians(self.complex-other.complex)
            return PhasorPR(mod,rad, self.roundOff)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Substraction can only be performed with Phasor instances.")


    def __mul__(self, other):
        """Multiply the Phasor object with another Phasor object or with a numerical object together with '*' operator 

        Args:
            other (Phasor): Other Phasor object to be added

        Raises:
            TypeError: If the second object is not a Phasor object or numerical object. 

        Returns:
            PhasorPR: Returns multipication of the phasor object with another Phasor object or another numerical object.
        """
        if(isinstance(other, Phasor)):
            mod, rad = RectangularToPolarDegree(self.complex * other.complex)
            return PhasorPR(mod, rad, self.roundOff)
        elif isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            mod, rad = RectangularToPolarDegree(self.complex * other)
            return PhasorPR(mod, rad, self.roundOff)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Multiplication can only be performed with Phasor instances.")


    def __truediv__(self, other):
        """Divide the Phasor object with another Phasor object or with a numerical object together with '*' operator 

        Args:
            other (Phasor/float/int/complex): Phasor object or the numerical value as the divisor

        Raises:
            ZeroDivisionError: If the divisor is Phasor object and value is zero 
            ZeroDivisionError: If the divisor is numerical object and value is zero
            TypeError: If the divisor object is not a Phasor object or a numerical object

        Returns:
            PhasorPR: Returns the division of the Phasor object with the divisor object
        """
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
        """Returns the power of an phasor object by using '**' operator

        Args:
            power (int/float): The exponent 

        Returns:
            PhasorPR: Returns the power of the Phasor
        """
        mod, rad = RectangularToPolarRadians(self.complex ** power)
        return PhasorPR(mod ,rad, self.roundOff)
       

    def __invert__(self):
        """Return the complex conjugate of the Phasor object.

        Returns:
            PhasorPR: Returns the conjugate. 
        """
        "Find the complex conjugate of the phasor by ' ` ' "
        return PhasorPR(self.modulus, -self.radian, self.roundOff)
    
    
    def __str__(self):
        """Return information of Phasor object

        Returns:
            String: Returns modulus and angle in radians
        """
        mod,ang = RectangularToPolarRadians(self.complex)
        return f"{round(mod,self.roundOff)} \u2220 {round(ang,self.roundOff)} \u33AD"
    

    def __repr__(self):
        """Return information of Phasor object

        Returns:
            String: Returns modulus and angle in radians
        """
        mod,ang = RectangularToPolarRadians(self.complex)
        return f"{round(mod,self.roundOff)} \u2220 {round(ang,self.roundOff)} \u00b0"




class PhasorRe(Phasor):
    """Initialize Phasor objects in Rectangulatr Coordinates with complex numbers

    Args:
        Phasor (Phasor): Abstract Phasor parent class
    """
    
    def __init__(self,complex, roundOff = 2):
        """Initiate PhasorRe objects

        Args:
            complex (complex): Rectangular coordinates of the phasor
            roundOff (int, optional): Decimalpoints to be roundoff. Defaults to 2.
        """
        self.complex = complex
        self.modulus,self.radian = RectangularToPolarRadians(complex) 
        self.radian = self.radian % (2 * np.pi)
        self.degree = PolarRadiansToPolarDegree(self.radian) % 360
        self.roundOff = roundOff


    def __add__(self, other):
        """Add two phasor objects together with '+' operator.

        Args:
            other (Phasor): Other Phasor object to be added

        Raises:
            TypeError: If the second object is not a Phasor object. 

        Returns:
            PhasorRe: Returns addition.
        """
        if isinstance(other, Phasor):
            return PhasorRe(self.complex + other.complex, self.roundOff)
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}. Addition can only be performed with Phasor instances.")

    
    def __sub__(self, other):
        """Substract of two phasor objects with '-' operator. 

        Args:
            other (Phasor): Other Phasor object to be substracted

        Raises:
            TypeError: If the second object is not a Phasor object. 

        Returns:
            PhasorRe: Return the defference between the phasor objects.
        """
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
        """Multiply the Phasor object with another Phasor object or with a numerical object together with '*' operator 

        Args:
            other (Phasor): Other Phasor object to be added

        Raises:
            TypeError: If the second object is not a Phasor object or numerical object. 

        Returns:
            PhasorRe: Returns multipication of the phasor object with another Phasor object or another numerical object.
        """
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
        """Returns the power of an phasor object by using '**' operator

        Args:
            power (int/float): The exponent 

        Returns:
            PhasorRe: Returns the power of the Phasor
        """
        return PhasorRe(np.conjugate(self.complex), self.roundOff)
    

    def __str__(self):
        """Return information of Phasor object

        Returns:
            String: Returns the phasor in rectangular coordinates
        """
        return f"{complex(round(self.complex.real, self.roundOff),round(self.complex.imag, self.roundOff))}"
    

    def __repr__(self):
        """Return information of Phasor object

        Returns:
            String: Returns the phasor in rectangular coordinates
        """
        return f"{complex(round(self.complex.real, self.roundOff),round(self.complex.imag, self.roundOff))}"



def toRec(phasorObject):
    """Convert any type of phaasor object to PhasorRe object.

    Args:
        phasorObject (Phasor): Phasor object to be converted.

    Raises:
        TypeError: If the argument is not a phasor object.

    Returns:
        PhasorRe: Phasor object with rectangular coordinates.
    """
    if isinstance(phasorObject, Phasor):
        return PhasorRe(phasorObject.complex, phasorObject.roundOff) 
    else:
        raise TypeError(f"Unsupported argument type: {type(phasorObject)}.")
        

def toRad(phasorObject):
    """Convert any type of phasor object to PhasorPR object.

    Args:
        phasorObject (Phasor): Phasor object to be converted.

    Raises:
        TypeError: If the argument is not a phasor object.

    Returns:
        PhasorPR: Phasor object with polar coordiantes with angles in radians.
    """
    if isinstance(phasorObject, Phasor):
        return PhasorPR(phasorObject.modulus, phasorObject.radian, phasorObject.roundOff) 
    else:
        raise TypeError(f"Unsupported argument type: {type(phasorObject)}.")


def toDeg(phasorObject):
    """Convert any type of phasor object to PhasorPD object.

    Args:
        phasorObject (Phasor): Phasor object to be converted.

    Raises:
        TypeError: If the argument is not a phasor object.

    Returns:
        PhasorPD: Phasor object with polar coordiantes with angles in degrees.
    """
    if isinstance(phasorObject, Phasor):
        return PhasorPD(phasorObject.modulus, phasorObject.degree, phasorObject.roundOff) 
    else:
        raise TypeError(f"Unsupported argument type: {type(phasorObject)}.")

