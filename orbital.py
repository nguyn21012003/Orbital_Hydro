import numpy as np
from scipy.special import factorial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as cm
from matplotlib.animation import FuncAnimation
import csv
from celluloid import Camera


class Orbital:
    def __init__(self, n: int, l: int, m: int, a: float = 1.0):
        self.n = n
        self.l = l
        self.m = m
        self.a = a

    def LaguerrePolys(self, m: int, alpha: int, x):
        L = 0
        for i in range(0, m + 1):
            L += (-1) ** i * factorial(m + alpha) / (factorial(m - i) * factorial(alpha + i) * factorial(i)) * x**i
        return L

    def radial_wave(self, r):
        n, l, a = self.n, self.l, self.a
        x = 2 * r / (n * a)
        alpha = 2 * l + 1
        m = n - l - 1
        L = self.LaguerrePolys(m, alpha, x)
        R = np.sqrt((2 / (n * a)) ** 3 * factorial(n - l - 1) / (2 * n * factorial(n + l))) * np.exp(-r / (n * a)) * (2 * r / (n * a)) ** l * L
        return R

    def Legendre_wave(self, m: int, l: int, theta):
        x = np.cos(theta)
        P = 0
        for k in range((l - m) // 2 + 1):
            term = (((-1) ** k) * factorial(2 * l - 2 * k)) / (factorial(k) * factorial(l - k) * factorial(l - 2 * k - m))
            term *= x ** (l - 2 * k - m)
            P += term
        P *= ((-1) ** m) * (1 - x**2) ** (m / 2) / (2**l)
        return P

    def spherical_harmonics(self, theta, phi):
        m, l = self.m, self.l
        P = self.Legendre_wave(m, l, theta)
        Y = np.sqrt((2 * l + 1) * factorial(l - m) / (4 * np.pi * factorial(l + m))) * np.exp(1j * m * phi) * P
        return Y

    def draw(self, N: int):
        r = np.random.rand(N) * 20
        theta = np.arccos(2 * np.random.rand(N) - 1)
        phi = 2 * np.pi * np.random.rand(N)

        R = self.radial_wave(r)
        Y = self.spherical_harmonics(theta, phi)
        psi = R * Y
        prob = abs(psi) ** 2

        prob /= prob.max()
        mask = np.random.rand(N) < prob

        r, theta, phi = r[mask], theta[mask], phi[mask]

        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(theta)

        return x, y, z, prob[mask]


def main():
    n = 3
    l = 2
    m = 0

    N = 500000
    orbital = Orbital(n, l, m)
    x, y, z, prob = orbital.draw(N)

    # fig = plt.figure(figsize=(7, 7))
    # ax = fig.add_subplot(projection="3d")
    # scat = ax.scatter(x, y, z, c=prob + prob.max() / 2, s=1, cmap="plasma")
    # ax.view_init(elev=-1, azim=40)
    #
    # ax.set_xlim(min(x), max(x))
    # ax.set_ylim(min(y), max(y))
    # ax.set_zlim(min(z), max(z))
    # ax.set_axis_off()
    #
    # def update(frame):
    #     M = len(x)
    #     dx = 0.5 * np.random.randn(M)
    #     dy = 0.5 * np.random.randn(M)
    #     dz = 0.5 * np.random.randn(M)
    #
    #     scat._offsets3d = (x + dx, y + dy, z + dz)
    #     return (scat,)
    #
    # nframes = 36
    # anim = FuncAnimation(fig, update, frames=nframes + 1, interval=150, blit=False)
    # plt.show()

    with open("orbital.csv", "w", newline="") as file:
        header = ["x", "y", "z", "psi"]
        writer = csv.DictWriter(file, fieldnames=header, delimiter=",")
        writer.writeheader()
        for i in range(len(x)):
            row = {"x": x[i], "y": y[i], "z": z[i], "psi": prob[i]}

            writer.writerow(row)
    return None


if __name__ == "__main__":
    main()
