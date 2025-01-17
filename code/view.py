import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib import cm
import numpy as np
import random


def read(filename, c, limit=None):
    ox, oy, oz = [], [], []
    with open(filename) as f:
        for line in f.readlines():
            line = str.split(line)
            if len(line) == 4 and int(line[3]) == c:
                ox.append(float(line[0]))
                oy.append(float(line[1]))
                oz.append(float(line[2]))
    if limit is not None:
        c = list(zip(ox, oy, oz))
        random.shuffle(c)
        ox[:], oy[:], oz[:] = zip(*c)
        return np.array(ox)[:limit], np.array(oy)[:limit], np.array(oz)[:limit]
    return np.array(ox), np.array(oy), np.array(oz)


def draw(x, y1, l1, y2, l2):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(x, y1, label=l1)
    ax2 = ax1.twinx()
    ax2.plot(x, y2, label=l2)
    ax1.legend()
    ax2.legend()
    # plt.legend()
    plt.show()


def draw3d(x, y, z):
    fig = plt.figure()
    a = Axes3D(fig)
    a.scatter(x, y, z, c='b')
    a.set_ylabel('Pressure Difference')
    a.set_xlabel('Flow Difference')
    a.set_zlabel('Leak Size')
    a.set_rasterized(True)
    plt.savefig('oil.eps', format='eps')
    # plt.show()


def draw3d_compare(x, y, z1, z2):
    fig = plt.figure()
    a = Axes3D(fig)
    a.scatter(x, y, z1, c='b')
    a.scatter(x, y, z2, c='r')
    a.set_ylabel('Pressure Difference')
    a.set_xlabel('Flow Difference')
    a.set_zlabel('Leak Size')
    a.set_rasterized(True)
    red = patches.Patch(color='r', label='initial brb output')
    blue = patches.Patch(color='b', label='original leak size')
    plt.legend(handles=[red, blue])
    plt.savefig('oil_compare_after.eps', format='eps')
    # plt.show()


def draw2d(x, y, xlabel=None, ylabel=None):
    plt.figure()
    plt.plot(x, y)
    plt.ylim()
    if xlabel is not None:
        plt.xlabel(xlabel)
    if ylabel is not None:
        plt.ylabel(ylabel)
    plt.show()


def draw2d2(ax, ay, bx, by, xlabel, ylabel, rlabel, blabel):
    plt.figure()
    plt.plot(ax, ay, 'r')
    plt.plot(bx, by, 'b')
    # red = patches.Patch(color='r', label=rlabel)
    # blue = patches.Patch(color='b', label=blabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(handles=[red, blue])
    plt.show()


def draw_surf(x, y, z):
    fig = plt.figure()
    ax = Axes3D(fig)
    surf = ax.plot_surface(x, y, z, cmap='jet', alpha=1, linewidth=0, antialiased=True, shade='False')
    # surf.set_facecolor((0, 0, 0, 0))
    plt.show()


def draw_mesh(x, y, z):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(x, y, z, rstride=5, cstride=5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z:activation weight')
    ax.set_rasterized(True)
    # plt.savefig('fig_exp_half.eps', format='eps')
    plt.show()


def vec(z):
    zo = np.array([-4., -3., -2., -1., 0., 1., 2., 3., 4.])
    zt = np.array([0., 0., 0., 0., 1., 0., 0., 0., 0.])
    zz = np.zeros((9,))
    for i in range(9):
        if abs(z - zo[i]) <= 1.0:
            zz[i] = 1.0 - abs(z-zo[i])
    return np.sum(np.square(zt-zz))


def cal(x, y):
    # return (1.0 - np.sqrt(0.5 * vec(x))) * (1.0 - np.sqrt(0.5 * vec(y)))

    return np.exp(-0.25*x*x-0.25*y*y)


def main():
    x, y = np.arange(-4, 4, 0.1), np.arange(-4, 4, 0.1)
    x, y = np.meshgrid(x, y)
    n = x.shape[0]
    z = np.zeros((n, n,))
    for i in range(n):
        for j in range(n):
            xt, yt = x[i][j], y[i][j]
            z[i][j] = cal(xt, yt)
    draw_mesh(x, y, z)


if __name__ == "__main__":
    # matplotlib.use('Agg')
    main()
