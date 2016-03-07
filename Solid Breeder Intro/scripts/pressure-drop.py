import numpy as np
import matplotlib.pyplot as plt
color_idx = [[0./255,107./255,164./255], 
             [255./255, 128./255, 14./255], 
             [171./255, 171./255, 171./255], 
             [89./255, 89./255, 89./255],
             [44./255, 160./255, 44./255],
             [95./255, 158./255, 209./255],
             [200./255, 82./255, 0./255],
             [255./255, 152./255, 150./255]]



d_p = 0.001
u0lb = 0.02
dx = 20/240.
dt = dx*u0lb

pi = 1.87
po = 1.714

rho0 = 1
mu = 4.17e-6

dp =( (pi-po)/3) * (dx**2/dt**2)*3
print(dp)

L = dx * 263 * d_p #m
phi = 0.64
nu = 0.0008516

vs = np.linspace(0, 10, 100)

Re = vs*d_p/nu
dpk = 180.*mu/d_p**2 * (phi**2)/(1-phi)**3 * vs

plt.plot(Re, dpk/10**3, linewidth=2, color = color_idx[0])
plt.grid('on')
plt.xlabel('Particle Reynolds Number')
plt.ylabel('Pressure Drop (kPa)')
plt.show()