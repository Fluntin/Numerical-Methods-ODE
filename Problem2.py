#Sto smo dobili od lika....
t_start = 0
y0 = 1
x0 = 1
t_slut = 10
N=1000
h = (t_slut-t_start)/N

    
t_värde = [t_start]
x_värde = [x0]
y_värde = [y0]

while t_värde[-1] < t_slut:
    t_next = t_värde[-1] + h
    y_next = y_värde[-1] + h * f(x_värde[-1], y_värde[-1], h)
    t_värde.append(t_next)
    y_värde.append(y_next)

# My Diff eq system:
def f(x, y, h):
    return (x + h * y, y - h * x)


import matplotlib.pyplot as plt

# Plot
plt.plot(t_värde, y_värde, '-o', label='y(t)')  # '-o' will also mark the points
plt.xlabel('t')
plt.ylabel('y')
plt.title('euler_method')
plt.legend()
plt.grid(True)
plt.show()