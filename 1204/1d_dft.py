import numpy as np, math
import matplotlib.pyplot as plt

def exp(knN):
    th = -2 * math.pi * knN
    return complex(math.cos(th), math.sin(th))

def dft(g):
    N = len(g)
    dst = [sum(g[n] * exp(k*n/N) for n in range(N)) for k in range(N)]
    return np.array(dst)

def idft(G):
    N = len(G)
    dst = [sum(G[n] * exp(-k * n/N) for n in range(N)) for k in range(N)]
    return np.array(dst) / N

fmax = 1000
dt = 1/fmax
t = np.arange(0, 1, dt)

g1 = np.sin(2 * np.pi * 50 * t)
g2 = np.sin(2 * np.pi * 120 * t)
g3 = np.sin(2 * np.pi * 260 * t)
g = g1 * 0.6 + g2 * 0.9 + g3 * 0.2

N = len(g)
df = fmax/N
f = np.arange(0, N, df)
G = dft(g) * dt
g2 = idft(G) / dt

plt.figure(figsize=(10,10))
plt.subplot(3,1,1), plt.plot(t[0:200], g[0:200]), plt.title("org signal")
plt.subplot(3,1,2), plt.plot(f, np.abs(G)), plt.title("dft amplitude")
plt.subplot(3,1,3), plt.plot(t[0:200], g2[0:200]), plt.title("idft signal")
plt.show()