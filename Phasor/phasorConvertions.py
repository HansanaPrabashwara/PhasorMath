from Phasor.phasor import Phasor
from Phasor.phasorRe import PhasorRe
from Phasor.phasorPR import PhasorPR
from Phasor.phasorPD import PhasorPD


def toRec(phasorObject):
    if isinstance(phasorObject, Phasor):
        return PhasorRe(phasorObject.complex, phasorObject.roundOff) 
    else:
        raise TypeError(f"Unsupported argument type: {type(phasorObject)}.")
        

def toRad(phasorObject):
    if isinstance(phasorObject, Phasor):
        return PhasorPR(phasorObject.modulus, phasorObject.radian, phasorObject.roundOff) 
    else:
        raise TypeError(f"Unsupported argument type: {type(phasorObject)}.")


def toDeg(phasorObject):
    if isinstance(phasorObject, Phasor):
        return PhasorPD(phasorObject.modulus, phasorObject.degree, phasorObject.roundOff) 
    else:
        raise TypeError(f"Unsupported argument type: {type(phasorObject)}.")


