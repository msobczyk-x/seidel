import numpy as np
import sys
import random

A = np.array([[12, 12], [8, 10], [3, 2], [2, 3], [1, 1]])

B = np.array([1200, 1500, 500, 600, 200])
C = np.array([[1, 1.5]])


def Seidel(A, B, C):
    #pierwszy if z pseudokodu
    if len(C[0]) == 1:
        return max(np.linalg.solve(A, B))
    #drugi if z pseudokodu
    if len(A) == len(C[0]):
        return np.linalg.solve(A, B)
        #to jest eliminacja gaussa poniżej
        """ 
        print("A", A)
        print("B", B)
        n = len(C[0])
        a = np.zeros((n,n+1))
        x = np.zeros(n)
        for i in range(0,n):
            for j in range(n+1):
                if j == (n+1):
                    a[i][j] = B[i]
                else:
                    a[i][j] = A[i][j-1]
        for i in range(n):
            if A[i][i] == 0.0:
                sys.exit("Divide by zero detected!")

            for j in range(i + 1, n):
                ratio = A[j][i] / A[i][i]

                for k in range(n + 1):
                    A[j][k] = a[j][k] - ratio * a[i][k]


# Back Substitution
        x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

        for i in range(n - 2, -1, -1):
            x[i] = a[i][n]

            for j in range(i + 1, n):
                x[i] = x[i] - a[i][j] * x[j]

            x[i] = x[i] / a[i][i]
            
        return x """
    if len(A) == 0 :
        print("Cant solve")
        return 0
    #pick a random constraint to eliminate
    i = random.randint(0, len(A) - 1)
    hA = A[i]
    hB = B[i]
    AS = np.delete(A, i, 0)
    BS = np.delete(B, i, 0)
    xP = Seidel(AS, BS, C)
    print("xP", xP)
    #if x* satisfies h, czyli że spełniamy warunek
    if (xP[0]*hA[0] + xP[1]*hA[1]) <= hB:
        if xP[0] > 0 and xP[1] > 0:
            return xP
        
    else:
        Ap = np.delete(A, i, 0)
        Bp = np.delete(B, i, 0)
        return Seidel(Ap, Bp, C)

rozw= Seidel(A, B, C)
print(rozw)
