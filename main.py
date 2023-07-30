
from Phasor.phasor import *
from Phasor.plot import Plot
from Phasor.phasor import *
from Phasor.sc import *

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



