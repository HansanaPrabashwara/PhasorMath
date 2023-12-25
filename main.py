
from src.Phasor.phasor import *
from src.Phasor.plot import Plot
from src.Phasor.sc import *

a = PhasorPD(100, 45)

print(a * 3)

b = PhasorPR(200, 3.14)
print(b)

print(toRec(b+a))

c = unbalancedToSC(a,b,a+b)
d = SCToUnbalanced(a,b,a-b)
Plot(a)
Plot(c)
Plot(d)



