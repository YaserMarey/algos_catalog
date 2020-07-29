# Fast Fourier Transform is an algorithm to efficiently multiply polynomials among many other applications
# Fast Fourier Transform is a divide and conquer that splits the X(n) sequence of values recursively
# performs DFT on pairs of elements and then combines the results

import numpy as np


# O(N^2) DFT calculation
def dft(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


# D&C FFT: You can think of FFT as a method to apply DFT recursively by split domain space
# that utilizes specific value points that achieve further reduction in computations needed.
def fft(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    if N % 2 > 0:
        raise ValueError("must be a power of 2")
    elif N <= 2:
        return dft(x)
    else:
        X_even = fft(x[::2])
        X_odd = fft(x[1::2])
        terms = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + terms[:int(N / 2)] * X_odd,
                               X_even + terms[int(N / 2):] * X_odd])


# Another function to compute the Fourier Transform.
# This time, we make use of vector operations instead of recursion.

def fft_v(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    if np.log2(N) % 1 > 0:
        raise ValueError("must be a power of 2")

    N_min = min(N, 2)

    n = np.arange(N_min)
    k = n[:, None]
    M = np.exp(-2j * np.pi * n * k / N_min)
    X = np.dot(M, x.reshape((N_min, -1)))

    while X.shape[0] < N:
        X_even = X[:, :int(X.shape[1] / 2)]
        X_odd = X[:, int(X.shape[1] / 2):]
        terms = np.exp(-1j * np.pi * np.arange(X.shape[0])
                       / X.shape[0])[:, None]
        X = np.vstack([X_even + terms * X_odd,
                       X_even - terms * X_odd])
    return X.ravel()


import time


def main():
    # Validate results
    x = np.random.random(1024)
    np.allclose(dft(x), np.fft.fft(x))

    # timeit

    t0 = time.time()
    dft(x)
    t1 = time.time()
    print(t1 - t0)

    t0 = time.time()
    np.fft.fft(x)
    t1 = time.time()
    print(t1 - t0)

    # Validate results
    x = np.random.random(1024)
    np.allclose(fft(x), np.fft.fft(x))

    # timeit
    t0 = time.time()
    dft(x)
    t1 = time.time()
    print(t1 - t0)

    t0 = time.time()
    fft(x)
    t1 = time.time()
    print(t1 - t0)

    t0 = time.time()
    np.fft.fft(x)
    t1 = time.time()
    print(t1 - t0)

    # Validate results
    x = np.random.random(1024)
    np.allclose(fft_v(x), np.fft.fft(x))

    # timeit
    t0 = time.time()
    fft(x)
    t1 = time.time()
    print(t1 - t0)

    t0 = time.time()
    fft_v(x)
    t1 = time.time()
    print(t1 - t0)

    t0 = time.time()
    np.fft.fft(x)
    t1 = time.time()
    print(t1 - t0)


if __name__ == '__main__':
    main()
