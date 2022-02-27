import numpy as np

def extreme(M):
    T = []
    minimum = 0
    maksimum = 0

    for i in range(1,len(M)):
        if (M[i][0] < M[minimum][0] or (M[i][0] == M[minimum][0] and M[i][1] < M[minimum][1])):
            minimum = i
        if (M[i][0] > M[maksimum][0] or (M[i][0] == M[maksimum][0] and M[i][1] < M[maksimum][1])):
            maksimum = i
    T.append(minimum)
    T.append(maksimum)
    return T

def determinan(p1,p2,array):
    if ((p1[0] == p2[0] and p1[0] == array[0]) or (p1[1] == p2[1] and p1[1] == array[1])):
        return 0
    return (p1[0]*p2[1] + array[0]*p1[1] + p2[0]*array[1] - array[0]*p2[1] - p2[0]*p1[1] - p1[0]*array[1])

def leftPoints(p1,p2,M,left):
    T = []

    for i in range(len(M)):
        if (p1 != i and p2 != i):
            det = determinan(M[p1],M[p2],M[i])
            if (left):
                if (det > 0):
                    T.append(i)
            else:
                if (det < 0):
                    T.append(i)
    return T

def distance(p1,p2,M,p3):
    a = M[p1][1] - M[p2][1]
    b = M[p2][0] - M[p1][0]
    c = M[p1][0]*M[p2][1] - M[p2][0]*M[p1][1]

    jarak = abs((a*M[p3][0] + b*M[p3][1] + c)/((a**2 + b**2)**0.5))
    return jarak

def maxDistance(p1,p2,points,M):
    maksimum = points[0]

    for i in range(1,len(points)):
        jarak = distance(p1,p2,M,points[i])
        if (jarak > distance(p1,p2,M,maksimum)):
            maksimum = points[i]
    return maksimum
       

def ConvexLeft(p1,p2,M,left):
    T = []

    if (left):
        leftpoints = leftPoints(p1,p2,M,True)
        if (leftpoints == []):
            T.append([p1,p2])
        else:
            p3 = maxDistance(p1,p2,leftpoints,M)
            T1 = ConvexLeft(p1,p3,M,True)
            T2 = ConvexLeft(p3,p2,M,True)
            for arr in T1:
                T.append(arr)
            for arr in T2:
                T.append(arr)
    else:
        rightpoints = leftPoints(p1,p2,M,False)
        if (rightpoints == []):
            T.append([p1,p2])
        else:
            p3 = maxDistance(p1,p2,rightpoints,M)
            T1 = ConvexLeft(p1,p3,M,False)
            T2 = ConvexLeft(p3,p2,M,False)
            for arr in T1:
                T.append(arr)
            for arr in T2:
                T.append(arr)
    return T 

def FullConvex(M):
    Hasil = []

    p1 = extreme(M)[0]
    pn = extreme(M)[1]
    Hasil1 = ConvexLeft(p1,pn,M,True)
    Hasil2 = ConvexLeft(p1,pn,M,False)

    for arr in Hasil1:
        Hasil.append(arr)
    for arr in Hasil2:
        Hasil.append(arr)
    Hasil = np.array(Hasil)
    return Hasil

class ConvexHull:
    def __init__ (this,M):
        this.simplices = FullConvex(M)