"""This module provides functionalities to convert complex nnumbers to differnt complex notaions
"""

from abc import abstractmethod
import numpy as np
from math import sqrt, pi


@abstractmethod
def RectangularToPolarRadians(complex):
    """Return the corresponding modulus and radian angle for given complex number 

    Args:
        complex (complex): Complex form of the phasor

    Returns:
        modulus,angle: Modulus value and angle value in radians
    """    
    modulus = np.absolute(complex)
    angle = np.angle(complex)
    return modulus,angle


@abstractmethod
def RectangularToPolarDegree(complex):
    """Return the corresponding modulus and degree angle for given complex number 

    Args:
        complex (complex): Complex form of the phasor

    Returns:
        float,float: Modulus value and angle value in degrees
    """
    modulus = np.absolute(complex)
    angle = np.angle(complex, deg=True)
    return modulus,angle


@abstractmethod
def PolarDegreeToPolarRadians(angle):
    """Convert degree angle to radians

    Args:
        angle (float): Angle in degree

    Returns:
        float: 
    """    
    angle = np.deg2rad(angle)
    return angle


@abstractmethod
def PolarRadiansToPolarDegree(angle):
    """Convert radian angle to degrees.

    Args:
        angle (float): Angle size in radians

    Returns:
        float: Angle in degrees
    """
    angle = np.rad2deg(angle)
    return angle


@abstractmethod
def PolarRadiansToRectangular(modulus, angle):
    """Convert polar coordinates to rectangular coordinates when angle is in radians.

    Args:
        modulus (float): Modulus of the complex notation.
        angle (float): Angle in radians.

    Returns:
        complex: Rectangular coordinates.
    """
    real = modulus* np.cos(angle)
    imag = modulus* np.sin(angle)
    return complex(real, imag)


@abstractmethod
def PolarDegreeToRectangle(modulus, angle):
    """Convert polar coordinates to rectangular coordinates when angle is in degrees

    Args:
        modulus (float): Modulus of the complex notation
        angle (float): Angle in degrees

    Returns:
        complex: Rectangular coordinates
    """
    angle = np.deg2rad(angle)
    return PolarRadiansToRectangular(modulus, angle)


@abstractmethod
def RoundOff(value, roundOffPoints):
    """Roundoff the given value to its given decimal points.

    Args:
        value (float): Value to be rounded off. 
        roundOffPoints (int): Decimal points to be rounded off.

    Returns:
        float: Rounded off value
    """
    return round(value,roundOffPoints)


    