import typing
import random
from math import *
import numpy as np
from matplotlib import pyplot as plt
import glm

def PerlinNoise1D(x : float, n_octaves : int = 1) -> float : 
    def noise(x):
        random.seed(x)
        r = random.random()*2-1
        return r


    def Interpolation(x : float) -> float :
        t = 6*(x**5) - 15*(x**4) + 10*(x**3)
        return t

    y = 0
    for i in range(n_octaves):
        scale = 2**i
        xt = x * scale
        dy0 = noise(floor(xt))
        dy1 = noise(floor(xt)+1)
        t = xt - floor(xt)
        w = Interpolation(t)
        # dy0 = (t)*(1-w)*dy0
        # dy1 = (1-t)*(w)*dy1
        dy0 = (t)*Interpolation(1-t)*dy0
        dy1 = (1-t)*Interpolation(t)*dy1
        y += dy0 - dy1

    return y

def PerlinNoise2D(pt : typing.Set) -> float :
    def noiseVec2(x):
        random.seed(x)
        theta = random.random() * 2 * pi
        rVec = (cos(theta), sin(theta))
        return rVec

    def Interpolation(x : float) -> float :
        t = 6*(x**5) - 15*(x**4) + 10*(x**3)
        return t

    # generate 4 rander vectors
    vec2_00 = noiseVec2( floor(pt[0]+0)*1347 + floor(pt[1]+0)*19 )
    vec2_01 = noiseVec2( floor(pt[0]+0)*1347 + floor(pt[1]+1)*19 )
    vec2_10 = noiseVec2( floor(pt[0]+1)*1347 + floor(pt[1]+0)*19 )
    vec2_11 = noiseVec2( floor(pt[0]+1)*1347 + floor(pt[1]+1)*19 )

    # vectors from 4 corner to pt
    pt_00 = (pt[0] - floor(pt[0])    , pt[1] - floor(pt[1])    )
    pt_01 = (pt[0] - floor(pt[0])    , pt[1] - floor(pt[1]) - 1)
    pt_10 = (pt[0] - floor(pt[0]) - 1, pt[1] - floor(pt[1])    )
    pt_11 = (pt[0] - floor(pt[0]) - 1, pt[1] - floor(pt[1]) - 1)

    # distance in 2 dimension
    tx = pt[0] - floor(pt[0])
    ty = pt[1] - floor(pt[1])

    # calculate noise value like bilinear interpolation
    # find two interpolation value at y=floor(pt[1]) and y=floor(pt[1])+1 first
    z0 = 0
    z0 += (pt_00[0] * vec2_00[0] + pt_00[1] * vec2_00[1]) * Interpolation(1-tx)
    z0 += (pt_10[0] * vec2_10[0] + pt_10[1] * vec2_10[1]) * Interpolation(tx)

    z1 = 0
    z1 += (pt_01[0] * vec2_01[0] + pt_01[1] * vec2_01[1]) * Interpolation(1-tx)
    z1 += (pt_11[0] * vec2_11[0] + pt_11[1] * vec2_11[1]) * Interpolation(tx)

    z = 0
    z += z0 * Interpolation(1-ty)
    z += z1 * Interpolation(ty)

    return z

def PerlinNoise3D(pt : glm.vec3) -> float :
    def noiseVec3(x) -> glm.vec3:
        random.seed(x)
        r1 = random.random()
        r2 = random.random()

        theta = r1 * 2.0 * pi
        phi = asin(r2 * 2.0 - 1.0) + pi / 2.0

        rotMat = glm.mat4(1.0)
        rotMat = glm.rotate(rotMat, theta, glm.vec3(0.0, 1.0, 0.0))
        rotMat = glm.rotate(rotMat, phi, glm.vec3(-1.0, 0.0, 0.0))

        rVec = rotMat * glm.vec3(0, 1, 0)
        return rVec

    def Interpolation(x : float) -> float :
        t = 6*(x**5) - 15*(x**4) + 10*(x**3)
        return t

    # generate 4 rander vectors
    rVec3_000 = noiseVec3( floor(pt[0]+0)*6437 + floor(pt[1]+0)*673 + floor(pt[2]+0)*97)
    rVec3_001 = noiseVec3( floor(pt[0]+0)*6437 + floor(pt[1]+0)*673 + floor(pt[2]+1)*97)
    rVec3_010 = noiseVec3( floor(pt[0]+0)*6437 + floor(pt[1]+1)*673 + floor(pt[2]+0)*97)
    rVec3_011 = noiseVec3( floor(pt[0]+0)*6437 + floor(pt[1]+1)*673 + floor(pt[2]+1)*97)
    rVec3_100 = noiseVec3( floor(pt[0]+1)*6437 + floor(pt[1]+0)*673 + floor(pt[2]+0)*97)
    rVec3_101 = noiseVec3( floor(pt[0]+1)*6437 + floor(pt[1]+0)*673 + floor(pt[2]+1)*97)
    rVec3_110 = noiseVec3( floor(pt[0]+1)*6437 + floor(pt[1]+1)*673 + floor(pt[2]+0)*97)
    rVec3_111 = noiseVec3( floor(pt[0]+1)*6437 + floor(pt[1]+1)*673 + floor(pt[2]+1)*97)

    # vectors from 4 corner to pt
    pt_000 = glm.vec3(pt[0] - floor(pt[0]) - 0, pt[1] - floor(pt[1]) - 0, pt[2] - floor(pt[2]) - 0)
    pt_001 = glm.vec3(pt[0] - floor(pt[0]) - 0, pt[1] - floor(pt[1]) - 0, pt[2] - floor(pt[2]) - 1)
    pt_010 = glm.vec3(pt[0] - floor(pt[0]) - 0, pt[1] - floor(pt[1]) - 1, pt[2] - floor(pt[2]) - 0)
    pt_011 = glm.vec3(pt[0] - floor(pt[0]) - 0, pt[1] - floor(pt[1]) - 1, pt[2] - floor(pt[2]) - 1)
    pt_100 = glm.vec3(pt[0] - floor(pt[0]) - 1, pt[1] - floor(pt[1]) - 0, pt[2] - floor(pt[2]) - 0)
    pt_101 = glm.vec3(pt[0] - floor(pt[0]) - 1, pt[1] - floor(pt[1]) - 0, pt[2] - floor(pt[2]) - 1)
    pt_110 = glm.vec3(pt[0] - floor(pt[0]) - 1, pt[1] - floor(pt[1]) - 1, pt[2] - floor(pt[2]) - 0)
    pt_111 = glm.vec3(pt[0] - floor(pt[0]) - 1, pt[1] - floor(pt[1]) - 1, pt[2] - floor(pt[2]) - 1)

    # distance in 3 dimension
    t = pt_000

    # calculate noise value like bilinear interpolation
    # interpolation z axis
    a00 = 0
    a00 += glm.dot(pt_000 , rVec3_000) * Interpolation(1-t[2])
    a00 += glm.dot(pt_001 , rVec3_001) * Interpolation(t[2])

    a01 = 0
    a01 += glm.dot(pt_010 , rVec3_010) * Interpolation(1-t[2])
    a01 += glm.dot(pt_011 , rVec3_011) * Interpolation(t[2])

    a10 = 0
    a10 += glm.dot(pt_100 , rVec3_100) * Interpolation(1-t[2])
    a10 += glm.dot(pt_101 , rVec3_101) * Interpolation(t[2])

    a11 = 0
    a11 += glm.dot(pt_110 , rVec3_110) * Interpolation(1-t[2])
    a11 += glm.dot(pt_111 , rVec3_111) * Interpolation(t[2])

    # interpolation y axis
    b0 = 0
    b0 += a00 * Interpolation(1-t[1])
    b0 += a01 * Interpolation(t[1])

    b1 = 0
    b1 += a10 * Interpolation(1-t[1])
    b1 += a11 * Interpolation(t[1])
    
    # interpolation x axis
    c = 0
    c += b0 * Interpolation(1-t[0])
    c += b1 * Interpolation(t[0])

    return c

if __name__ == "__main__":
    #%% test 1D Perlin Noise
    for n_octaves in range(1,6):
        y = [PerlinNoise1D(i/100, n_octaves) for i in range(500)]
        plt.plot(y)
        plt.xlabel("x")
        plt.ylabel("noise(x)")
        plt.title(f"PerlinNoise1D with {n_octaves} octaves")
        plt.show()
        ## save result as image
        # plt.savefig(f"PerlinNoise Result/PerlinNoise1D_{n_octaves}_octaves.png")
        # plt.cla()

    #%% test 2D Perlin Noise
    frame = np.empty(shape=(512, 512))
    for y in range(frame.shape[0]):
        for x in range(frame.shape[1]):
            frame[y,x] = PerlinNoise2D((x/64, y/64))
    plt.title(f"PerlinNoise2D")
    plt.imshow(frame)
    plt.show()
    # save result as image
    # plt.savefig(f"PerlinNoise Result/PerlinNoise2D.png")

    #%% test 3D Perlin Noise
    # print(PerlinNoise3D(glm.vec3(2.3, 6.4, 4.9)))
    frameNum = 30
    for i in range(frameNum):
        print(f"\r {i+1:02d}/{frameNum:02d}", end="")
        frame = np.empty(shape=(256, 256))
        for y in range(frame.shape[0]):
            for x in range(frame.shape[1]):
                frame[y,x] = PerlinNoise3D(glm.vec3(x/64, y/64, i/10))
        plt.title(f"PerlinNoise3D")
        plt.imshow(frame)
        plt.show()
        # save result as image
        # plt.savefig(f"PerlinNoise Result/PerlinNoise3D_{i}.png")