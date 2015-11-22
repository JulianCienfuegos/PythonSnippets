"""
A stupid plot demonstrating the relationship between right triangles and circles.

Melvyn Ian Drag. 21 November 2015.
"""

import matplotlib.pyplot as plt
import numpy as np

def crd_txt(a,b):
	return '(' + str(a)[:5] + ', ' +  str(b)[:5] +  ')'

n = 200
theta = np.linspace(0, 2*np.pi, n)
X = np.cos(theta)
Y = np.sin(theta)

fig = plt.figure(figsize=(15,10))
fig.suptitle('Trigonometry and Circles', fontsize=20)
ax1 = fig.add_subplot(131)
line,=ax1.plot([],[], marker='o', markersize=10, linestyle='None',c='red')
angle_line,=ax1.plot([],[],lw=3,c='b')
x_line,=ax1.plot([],[],lw=3,c='b')
y_line,=ax1.plot([],[],lw=3,c='b')
ax1.plot(X, Y, lw=3, c='black')
ax1.set_xlim((-2,2))
ax1.set_ylim((-2,2))
ax1.set_title('Circle Plot')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
t1 = ax1.text(0,1.5,'')
ax1.set(adjustable='box-forced', aspect='equal')
ax1.grid(True)

ax2 = fig.add_subplot(132)
ax2.plot(theta, X, lw=3,c='black')
cos_pt, = ax2.plot([], [], marker='o', markersize=10, linestyle='None',c='red')
ax2.set_title('Cosine Plot')
ax2.set_xlim(0, 2*np.pi)
ax2.set_ylim(-1,1)
ax2.set_xlabel('Theta')
ax2.set_ylabel('X')
t2 = ax2.text(2,0.5,'')
#ax2.set(adjustable='box-forced', aspect='equal')
ax2.grid(True)

ax3 = fig.add_subplot(133)
ax3.plot(theta, Y, lw=3,c='black')
sin_pt, = ax3.plot([],[],marker='o', markersize=10, linestyle='None',c='red')
ax3.set_title('Sine Plot')
ax3.set_xlim(0, 2*np.pi)
ax3.set_ylim(-1,1)
ax3.set_xlabel('Theta')
ax3.set_ylabel('Y')
t3 = ax3.text(4,0.5,'')
#ax3.set(adjustable='box-forced', aspect='equal')
ax3.grid(True)
plt.ion()
plt.show()

iters = 0; max_iters = 1
while iters < max_iters:
	for i in range(n):
		line.set_xdata(X[i])
		line.set_ydata(Y[i])
		angle_line.set_xdata([0,X[i]])
		angle_line.set_ydata([0,Y[i]])
		x_line.set_xdata([0,X[i]])
		x_line.set_ydata([0,0])
		y_line.set_xdata([X[i],X[i]])
		y_line.set_ydata([0,Y[i]])

		txt1 = crd_txt(X[i], Y[i])
		t1.set_text(txt1)

		cos_pt.set_xdata(theta[i])
		cos_pt.set_ydata(X[i])
		txt2 = crd_txt(theta[i], X[i])
		t2.set_text(txt2)

		sin_pt.set_xdata(theta[i])
		sin_pt.set_ydata(Y[i])
		txt3 = crd_txt(theta[i], Y[i])
		t3.set_text(txt3)

		plt.draw()
		plt.pause(0.001) # Modify this for different speeds.
	iters+=1