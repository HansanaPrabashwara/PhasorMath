from Phasor.phasorPD import PhasorPD
from Phasor.phasorPR import PhasorPR
from Phasor.phasorConvertions import *
from SymmetricalComponents.unbalancedToSC import unbalancedToSC
from SymmetricalComponents.SCToUnbalanced import SCToUnbalanced
from Plot.plotPhasor import Plot
a = PhasorPD(100, 45)

print(a*3)

b = PhasorPR(200, 3.14)
print(b)

print(toRec(b+a))

c = unbalancedToSC(a,b,a+b)
d = SCToUnbalanced(a,b,a-b)
Plot(a)
Plot(c)
Plot(d)
