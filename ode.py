import matplotlib.pyplot as plt
import numpy as np

def dy_dx(y, x):
    return 1-y**2

def on_click(event):
    global xi, yi, d1, d2, scatter,annot
    if event.inaxes is not None:
        if scatter is not None:
            scatter.remove()
        if annot is not None:
            annot.remove()
        xi, yi = event.xdata, event.ydata
        h=0.1
        d1=a-xi
        d2=a+xi
        x_positive=np.arange(xi,xi+d1,h)
        x_negative=np.arange(xi,xi-d2,-h)
        y_positive=[yi]
        y_negative=[yi]
    
    for x in x_positive[1:]:
        y = y_positive[-1] + dy_dx(y_positive[-1], x - h) * h
        y_positive.append(y)

# Integrate backward (negative x-values)
    for x in x_negative[1:]:
      y = y_negative[-1] - dy_dx(y_negative[-1], x + h) * h
      y_negative.append(y)

# Combine the solutions, reversing the negative part
    yy = y_negative[::-1][:-1] + y_positive  # Exclude the duplicate yi
    xx = np.concatenate((x_negative[::-1][:-1], x_positive))
    scatter=ax.scatter(xi,yi,color='blue')
    annot=ax.annotate(f'({xi:.2f},{yi:.2f})',xy=(xi,yi), xycoords='data')
    line.set_data(xx, yy)
    fig.canvas.draw()


scatter=None
annot=None
a,b=5,5
xi = 0
yi = 1
d1=a-xi
d2=a+xi
h = 0.1  # Step size



# Define the range for x values
x_positive = np.arange(xi, xi + d1, h)  # positive x-values
x_negative = np.arange(xi, xi - d2, -h) # negative x-values

# Initialize lists to store the solutions
y_positive = [yi]
y_negative = [yi]

# Integrate forward (positive x-values)
for x in x_positive[1:]:
    y = y_positive[-1] + dy_dx(y_positive[-1], x - h) * h
    y_positive.append(y)

# Integrate backward (negative x-values)
for x in x_negative[1:]:
    y = y_negative[-1] - dy_dx(y_negative[-1], x + h) * h
    y_negative.append(y)

# Combine the solutions, reversing the negative part
yy = y_negative[::-1][:-1] + y_positive  # Exclude the duplicate yi
xx = np.concatenate((x_negative[::-1][:-1], x_positive))

# Plotting

X, Y = np.meshgrid(np.linspace(-a, b, 20), np.linspace(-a, b, 20))

U = 1.00
V = dy_dx(Y, X)
N = np.sqrt(U**2 + V**2)
U = U / N
V = V / N
fig, ax = plt.subplots()

plt.quiver(X, Y, U, V, angles="xy",alpha=0.5,headaxislength=0)
line,=plt.plot(xx, yy, 'r-', label='Numerical Solution')
plt.title('Numerical Solution of Differential Equation')
scatter=plt.scatter(xi,yi)
annot=plt.annotate(f'({xi},{yi}',xy=(xi,yi), xycoords='data')
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.legend()
plt.grid(True,alpha=0.4)
cid = fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()
