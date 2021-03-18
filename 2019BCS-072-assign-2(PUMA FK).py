import numpy as np
from numpy import cos, sin, pi

a2, a3, d3, d4 = map(float, input("Enter a2, a3, d3, d4 values respectively: ").strip().split())
thetas = np.array(input("Enter 6 angles values: ").strip().split(), float)
end_effector_coord = np.array(input("Enter end effector coord: ").strip().split(), float).transpose()
end_effector_coord = np.append(end_effector_coord, 1)

thetas = (thetas / 180)* pi

DH_PARAMETER = [[0, 0, 0, thetas[0]],
                [-90, 0, 0, thetas[1]],
                [0, a2, d3, thetas[2]],
                [-90, a3, d4, thetas[3]],
                [90, 0, 0, thetas[4]],
                [-90, 0, 0, thetas[5]]]

tMatrices = []
main_tMatrix = np.identity(4)

for i in range(len(DH_PARAMETER)):
    alpha, a, d, theta = DH_PARAMETER[i]
    tMatrices.append(np.array([[cos(theta), -sin(theta), 0, a],
                               [cos(alpha)*sin(theta), cos(alpha)*cos(theta), -sin(alpha), -d*sin(alpha)],
                               [sin(alpha)*sin(theta), sin(alpha)*cos(theta), cos(alpha), d*cos(alpha)],
                               [0, 0, 0, 1]]))

    main_tMatrix = main_tMatrix @ tMatrices[-1]

final_coord = main_tMatrix @ end_effector_coord
print("final coord: ", np.delete(final_coord, -1))
