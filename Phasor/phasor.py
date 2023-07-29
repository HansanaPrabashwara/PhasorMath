# from .conversions import  *
import numpy as np


class Phasor:
    def __init__(self):
        self.complex = 0
        self.modulus = 0
        self.radian = 0
        self.degree = 0
        self.roundOff = 2


    # def setDecimals(self, decimalPoints):
    #     self.roundOff = decimalPoints
    

    # def setRectangular(self, complex):
    #     self.complex = complex
    #     self.modulus,self.radian = RectangularToPolarRadians(complex) % (2 * np)
    #     self.degree = PolarRadiansToPolarDegree(self.radian) % 360


    # def setPolarDegree(self, modulus, degree):
    #     self.modulus = modulus
    #     self.degree = degree % 360
    #     self.radians = PolarDegreeToPolarRadians(modulus,degree)  % (2*np.pi)
    #     self.complex = PolarDegreeToRectangle(modulus, degree)
        

    # def setPolarRadians(self, modulus, radian):
    #     self.modulus = modulus
    #     self.radian = radian % (2*np.pi)
    #     self.degree = PolarRadiansToPolarDegree(modulus,radian)  % 360
    #     self.complex = PolarRadiansToRectangular(modulus, radian)