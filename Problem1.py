def euler_method(f, y0, t0, t_final, h):
    
    t_värde = [t0]
    y_värde = [y0]

    while t_värde[-1] < t_final:
        t_next = t_värde[-1] + h
        y_next = y_värde[-1] + h * f(t_värde[-1], y_värde[-1])

        t_värde.append(t_next)
        y_värde.append(y_next)

    return t_värde, y_värde

def euler_bakåt(f, y0, t0, t_final, h):
    t_värde = [t0]
    y_värde = [y0]

    while t_värde[-1] < t_final:
        t_next = t_värde[-1] + h
        y_next = y_värde[-1] + h * f(t_värde[-1], y_värde[-1])

        t_värde.append(t_next)
        y_värde.append(y_next)

    return t_värde, y_värde

def rk_fyra(f, y0, t0, t_final, h):
    #kickstart
    t_värde = [t0]
    y_värde = [y0]
    
    while t_värde[-1] < t_final:
        
        k1=f(t_värde[-1], y_värde[-1])
        k2=f(t_värde[-1]+h/2, y_värde[-1]+h/2*k1)
        k3=f(t_värde[-1]+h/2, y_värde[-1]+h/2*k2)
        k4=f(t_värde[-1]+h, y_värde[-1]+h*k3)
    
        t_next = t_värde[-1] + h
        y_next = y_värde[-1] + h/6*(k1+2*k2+2*k3+k4)

        t_värde.append(t_next)
        y_värde.append(y_next)

    return t_värde, y_värde

    
    
# My Diff eq: dy/dt = -y
def f(t, y):
    return -y

#Sto smo dobili od lika....
t_start = 0
y0 = 1
t_slut = 10
N=1000
h = (t_slut-t_start)/N

#Do Euler
t_värde, y_värde = euler_method(f, y0, t_start, t_slut, h)

import matplotlib.pyplot as plt

# Plot
plt.plot(t_värde, y_värde, '-o', label='y(t)')  # '-o' will also mark the points
plt.xlabel('t')
plt.ylabel('y')
plt.title('euler_method')
plt.legend()
plt.grid(True)
plt.show()

#Do RK4
t_värde, y_värde = rk_fyra(f, y0, t_start, t_slut, h)

# Plot
plt.plot(t_värde, y_värde, '-o', label='y(t)')  # '-o' will also mark the points
plt.xlabel('t')
plt.ylabel('y')
plt.title('rk_fyra')
plt.legend()
plt.grid(True)
plt.show()

