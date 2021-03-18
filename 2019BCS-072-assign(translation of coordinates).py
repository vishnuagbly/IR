import numpy as np

def getRotationMatrix(axis, theta):
    theta = (theta / 180) * np.pi
    if axis == 'x':
        return np.array(((1, 0, 0),(0, np.cos(theta), -np.sin(theta)), (0, np.sin(theta), np.cos(theta))))
    if axis == 'y':
        return np.array(((np.cos(theta), 0, np.sin(theta)), (0, 1, 0), (-np.sin(theta), 0, np.cos(theta))))
    if axis == 'z':
        return np.array(((np.cos(theta), -np.sin(theta), 0), (np.sin(theta), np.cos(theta), 0), (0, 0, 1)))
    raise Exception("invalid axis")

def getTransformedPoint(all_axises, point, thetas, translation):
    rMatrix = np.array(((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    for i in range(len(all_axises)):
        axis = all_axises[i].lower()
        if not (axis == 'x' or axis == 'y' or axis == 'z'):
            print("invalid axis")
            return

        tempRMatrix = getRotationMatrix(axis, thetas[i])
        rMatrix = np.matmul(rMatrix, tempRMatrix)
    translationMatrix = np.concatenate((rMatrix, np.transpose(translation).reshape((3, 1))), axis=1)
    translationMatrix = np.concatenate((translationMatrix, [(0, 0, 0, 1)]), axis=0)
    point = np.concatenate((point, [1]), axis=0).reshape(4, 1)
    # print(translationMatrix)
    # print(point)
    res = np.matmul(translationMatrix, point)
    return res



total = int(input("enter total number of successive rotations: "))
axis = []
theta = []
for i in range(total):
    axis.append(input("enter rotation of frame abt axis(x/y/z): "))
    theta.append(float(input("enter rotation degree in anticlockwise direction: ")))
translation = np.array(input("enter translation vector: ").strip().split(), float)
point = np.array(input("enter point in current frame: ").strip().split(), float)
res = getTransformedPoint(axis, point, theta, translation)
print('coord of points in main frame: ', res[0][0], " ", res[1][0], " ", res[2][0])
