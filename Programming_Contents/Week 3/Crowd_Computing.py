import statistics
import random
import matplotlib.pyplot as plt

Estimates=[1000, 1010, 1786, 2000, 1500, 1500, 100, 120, 150, 150, 150, 170]
for i in range(15):
    Estimates.append(random.randint(300,600))
y=[]

Estimates.sort ()
tv=int(0.1*(len(Estimates)))
Estimates=Estimates [tv:]
Estimates=Estimates [: len(Estimates)-tv]
for i in range(len(Estimates)):
    y.append(5)
plt.plot (Estimates, y, 'r--')
plt.plot([statistics.mean(Estimates)], [5],'ro')
plt.plot([statistics.median(Estimates)], [5],'bs')
plt.plot( [375], [5],'g^')
plt.show()