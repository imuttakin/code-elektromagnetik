"""
ef_demo.py

Program untuk me-plot medan listrik.
Mekanismenya adalah dengan menyusun muatan-muatan titik
untuk membentuk suatu ditribusi diskrit yang dapat dipandang sebagai kontinyu
dalam batasan bahwa jarak antar muatan adalah kecil.
Beberapa fungsi menunjukkan bagaimana ini dapat dilakukan
untuk membuat beberapa distribusi umum.

referensi:
    https://github.com/woznia62/E_fields
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def mkcharge(ax, ay, q, x, y):
    """
    Function: mkcharge()
    This function creates a point charge of magnitude q at position (ax,ay).
    """
    Ex = q*(x-ax) / ((x-ax)**2 + (y-ay)**2)**(1.5)
    Ey = q*(y-ay) / ((x-ax)**2 + (y-ay)**2)**(1.5)
    if q > 0:
        ch_point = Circle((ax,ay), q*0.05, color='r', alpha=0.6)
    else:
        ch_point = Circle((ax,ay), q*0.05, color='b', alpha=0.6)
    lout = [Ex, Ey, ch_point]
    # get current axis and add cirle to plot
    plt.gcf().gca().add_artist(ch_point)
    return lout

def dipole(q1, q2, a):
    """Function: dipole()
    Plot the electric field lines of two point charges seperated by a distance 2*a"""
#    plt.figure(figsize=(20, 14))
    plt.figure(figsize=(5, 3.5))
    xlim = (a+2); ylim = (a+2)
    plt.axes = plt.gca()
    plt.axes.set_xlim([-xlim,xlim])
    plt.axes.set_ylim([-ylim,ylim])
    x = np.linspace(-xlim, xlim, 60)
    y = np.linspace(-ylim, ylim, 60)
    x, y = np.meshgrid(x, y)
    E1 = mkcharge(0, a/2, q1, x, y)
    E2 = mkcharge(0, -a/2, q2, x, y)
    Ex = E1[0] + E2[0]
    Ey = E1[1] + E2[1]
    color = np.log(np.sqrt(np.abs(Ex) + np.abs(Ey)))
#    plt.streamplot(x, y, Ex/np.sqrt(Ex**2+Ey**2), Ey/np.sqrt(Ex**2+Ey**2), color=color, linewidth=1, cmap=plt.cm.inferno, density=2, arrowstyle='->', arrowsize=1.5)
    plt.streamplot(x, y, Ex/np.sqrt(Ex**2+Ey**2), Ey/np.sqrt(Ex**2+Ey**2), color=color, linewidth=0.5, cmap=plt.cm.jet, density=1, arrowstyle='->', arrowsize=1.0)
    #color = u + v
    #streamplot(x, y, Ex/sqrt(Ex**2+Ey**2), Ey/sqrt(Ex**2+Ey**2), color=color, linewidth=1, cmap=plt.cm.seismic, density=2, arrowstyle='->', arrowsize=1.5)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    #plt.savefig('electric_dipole.pdf', transparent=True, bbox_inches='tight', pad_inches=0)
    #plt.colorbar()
    plt.show()


def capacitor(a):
#    plt.figure(figsize=(20, 14), dpi=80)
    plt.figure(figsize=(5, 3.5))
    xlim = (a+2); ylim = (a+2)
    plt.axes = plt.gca()
    plt.axes.set_xlim([-xlim,xlim])
    plt.axes.set_ylim([-ylim,ylim])
    x = np.linspace(-xlim, xlim, 60)
    y = np.linspace(-ylim, ylim, 60)
    x, y = np.meshgrid(x, y)
    Lx = []
    Ly = []
    Ex = 0
    Ey = 0
    for m in range(-30,30):
        EFt = mkcharge(0.015*m, a/2, 1, x, y)
        Lx.append(EFt[0])
        Ly.append(EFt[1])
    for n in range(-30,30):
        EFb = mkcharge(0.015*n, -a/2, -1, x, y)
        Lx.append(EFb[0])
        Ly.append(EFb[1])
    for xelem in Lx:
        Ex += xelem
    for yelem in Ly:
        Ey += yelem
    color = np.log(np.sqrt(np.abs(Ex) + np.abs(Ey)))
#    plt.streamplot(x, y, Ex/np.sqrt(Ex**2+Ey**2), Ey/np.sqrt(Ex**2+Ey**2), color=color, linewidth=1, cmap=plt.cm.inferno, density=2, arrowstyle='->', arrowsize=1.5)
    plt.streamplot(x, y, Ex/np.sqrt(Ex**2+Ey**2), Ey/np.sqrt(Ex**2+Ey**2), color=color, linewidth=0.5, cmap=plt.cm.jet, density=1, arrowstyle='->', arrowsize=1.0)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    #plt.savefig('capacitor.pdf', transparent=True, bbox_inches='tight', pad_inches=0)
    #plt.colorbar()
    plt.show()
