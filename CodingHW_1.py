
import numpy as np
import math


A = np.array([[1, -2.3], [4.5, np.e**2]])
B = ([[6, 2, 4, -3], [np.pi, 9, 3.6, -2.1]])
C = ([[3.7, -2.4, 0], [4, 1.8, -11.6], [2.3, -3.3, 5.9]])

x_col = np.array([5, math.sin(4), -3])
x = np.reshape(x_col, (3, 1))

y_row = np.array([8, -6])
y = np.reshape(y_row, (1, 2))


z_col = np.array([3, 0, math.tan(2), -4.7])
z = np.reshape(z_col, (4,1))

# Problem 1
A1 = 3*x
A2 = np.transpose(z) @ np.transpose(B) + y
A3 = (C @ x)
A4 = (A @ B)
A5 = np.transpose(B) @ np.transpose(A)

# Problem 2
x = np.linspace(-4,1,73)
A6 = x.reshape(1,73)

y = np.zeros(73)
for i in range(73):
    y[i] = np.cos(i)

A7 = y.reshape(1, 73)
C2 = x*y
A8 = C2.reshape(1, 73)
print(A8.shape)
D2 = x/y
A9 = D2.reshape(1, 73)
print(A9.shape)
E2 = x**3 - y
A10 = E2.reshape(1, 73)
print(A10.shape)

# Problem 3
Y1 = 2.5 * 3 * (1 - (3/20))
Y2 = 2.5 * Y1 * (1 - (Y1/20))
Y3 = 2.5 * Y2 * (1 - (Y2/20))
A11 = Y3
print("A11 = ")
print(A11)

P1 = 3.2 * 8 * (1 - (8/14))
P2 = 3.2 * P1 * (1 - (P1/14))
P3 = 3.2 * P2 * (1 - (P2/14))
P4 = 3.2 * P3 * (1 - (P3/14))
A12 = P4

print(P4)

M1 = 5 * np.exp(2.6 * (1-(5/12)))
M2 = M1 * np.exp(2.6 * (1-(M1/12)))
M3 = M2 * np.exp(2.6 * (1-(M2/12)))
A13 = M3
print(A13)

W1 = 2 * np.exp(3 * (1- (2/25)))
W2 = W1 * np.exp(3 * (1- (W1/25)))
W3 = W2 * np.exp(3 * (1- (W2/25)))
W4 = W3 * np.exp(3 * (1- (W3/25)))
A14 = W4
print(A14)

A15 = 0












