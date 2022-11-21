import typing
import random
from math import *
import numpy as np
from matplotlib import pyplot as plt

def WorleyNoise2D(size = (64, 64),# height * width
    nPoints = 10, 
    repeat = False) -> np.ndarray:

    res = np.empty(shape=size)

    randPoints = np.random.random(size=(nPoints, 2))
    if(repeat):
        randPoints = np.vstack((randPoints, randPoints + np.array([[-1, -1]])))
        randPoints = np.vstack((randPoints, randPoints + np.array([[-1,  0]])))
        randPoints = np.vstack((randPoints, randPoints + np.array([[-1,  1]])))
        randPoints = np.vstack((randPoints, randPoints + np.array([[ 0, -1]])))
        randPoints = np.vstack((randPoints, randPoints + np.array([[ 0,  1]])))
        randPoints = np.vstack((randPoints, randPoints + np.array([[ 1, -1]])))
        randPoints = np.vstack((randPoints, randPoints + np.array([[ 1,  0]])))
        randPoints = np.vstack((randPoints, randPoints + np.array([[ 1,  1]])))

    for y in range(size[0]):
        for x in range(size[1]):
            dis = randPoints - np.array([[x/size[1],y/size[0]]])
            dis = np.sqrt(dis[:,0]**2 + dis[:,1]**2)
            res[y,x] = dis.min()

    ptsImg = np.zeros(shape=size)
    for randPoint in randPoints[:nPoints]:
        ptsImg[int(randPoint[1]*size[1]), int(randPoint[0]*size[0])] = 10

    return res, ptsImg

def WorleyNoise3D(size = (64, 64),# length * height * width
    nPoints = 10, 
    repeat = False) -> np.ndarray:

    res = np.empty(shape=size)

    randPoints = np.random.random(size=(nPoints, 2))
    if(repeat):
        randPoints = np.vstack((randPoints, randPoints + np.array([[-1, -1]])))
        randPoints = np.vstack((randPoints, randPoints + np.array([[-1,  0]])))
        randPoints = np.vstack((randPoints, randPoints + np.array([[-1,  1]])))
        randPoints = np.vstack((randPoints, randPoints + np.array([[ 0, -1]])))
        randPoints = np.vstack((randPoints, randPoints + np.array([[ 0,  1]])))
        randPoints = np.vstack((randPoints, randPoints + np.array([[ 1, -1]])))
        randPoints = np.vstack((randPoints, randPoints + np.array([[ 1,  0]])))
        randPoints = np.vstack((randPoints, randPoints + np.array([[ 1,  1]])))

    for y in range(size[0]):
        for x in range(size[1]):
            dis = randPoints - np.array([[x/size[1],y/size[0]]])
            dis = np.sqrt(dis[:,0]**2 + dis[:,1]**2)
            res[y,x] = dis.min()

    ptsImg = np.zeros(shape=size)
    for randPoint in randPoints[:nPoints]:
        ptsImg[int(randPoint[1]*size[1]), int(randPoint[0]*size[0])] = 10

    return res, ptsImg
if __name__ == "__main__":
    result = np.zeros(shape=(128, 128))
    for i in range(3):
        frame, ptsImg = WorleyNoise2D(size=(128, 128), nPoints=(i+1)*10, repeat = True)
        frame = frame / frame.max()
        result = result + frame

        plt.imshow(result)
        plt.savefig(f"WorleyNoise2D.png")