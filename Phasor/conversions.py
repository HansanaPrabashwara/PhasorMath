import numpy as np
from math import sqrt, pi




def RectangularToPolarRadians(complex):
    modulus = np.absolute(complex)
    angle = np.angle(complex)
    return modulus,angle


def RectangularToPolarDegree(complex):
    modulus = np.absolute(complex)
    angle = np.angle(complex, deg=True)
    return modulus,angle


def PolarDegreeToPolarRadians(angle):
    angle = np.deg2rad(angle)
    return angle


def PolarRadiansToPolarDegree(angle):
    angle = np.rad2deg(angle)
    return angle


def PolarRadiansToRectangular(modulus, angle):
    real = modulus* np.cos(angle)
    imag = modulus* np.sin(angle)
    return complex(real, imag)


def PolarDegreeToRectangle(modulus, angle):
    angle = np.deg2rad(angle)
    return PolarRadiansToRectangular(modulus, angle)


def RoundOff(value, roundOffPoints):
    return round(value,roundOffPoints)


    