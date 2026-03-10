import numpy as np 
import matplotlib.pyplot as plt

# Først definerer vi funksjonene f(x) og df(x) som vi løste for hånd. 
def f(x):
    return np.e**(-x/4)*np.arctan(x)

# Funksjonen som har rot som definerer toppunktet.
def topppunkt_f(x):
    return np.arctan(x) - (4)/(x**2 + 1)

# Startverdiere regnet ut med penn og papir.
a = 1
b = 3
n = 16 # Dette kalkulerte vi med penn, papir og kalkulator.

for i in range(n):
    m = (b + a)/2

    if topppunkt_f(a)*topppunkt_f(m) < 0:
        b = m
    else:
        a = m
print(m)


# Dette er en alternativ metode der vi stopper når vi har kommet frem til 
# antall desimalers pressisjon som vi måtte ønske. 
a = 1
b = 3

while abs(b-a) > 0.00005:
    m = (b+a)/2
    if topppunkt_f(m) < 0:
        a = m
    else: 
        b = m

print(m)


# Plotting:

x = np.linspace(-1, 5, 1000)


plt.plot(x, f(x))
plt.plot(x, topppunkt_f(x))
plt.axis('equal')
plt.grid()
plt.scatter(m, f(m), color='red')
plt.show()
