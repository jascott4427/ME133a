'''hw4p1.py

   This is skeleton code for HW4 Problem 1.  Please EDIT.

   This should simply use NumPy to implement the known forward
   kinematics and Jacobian functions for the 3 DOF robot.

'''

import numpy as np


#   
#  Forward Kinematics
#
def fkin(q):
    thetap, theta1, theta2 = q
    x = -np.sin(thetap)*(np.cos(theta1)+np.cos(theta1+theta2))
    y = np.cos(thetap)*(np.cos(theta1)+np.cos(theta1+theta2))
    z = np.sin(theta1)+np.sin(theta1+theta2)
    return np.array([x, y, z])


#
#  Jacobian
#
def Jac(q):
    thetap, theta1, theta2 = q
    j00 = -np.cos(thetap)*(np.cos(theta1)+np.cos(theta1+theta2))
    j01 = np.sin(thetap)*(np.sin(theta1)+np.sin(theta1+theta2))
    j02 = np.sin(thetap)*np.sin(theta1+theta2)
    j10 = -np.sin(thetap)*(np.cos(theta1)+np.cos(theta1+theta2))
    j11 = -np.cos(thetap)*(np.sin(theta1)+np.sin(theta1+theta2))
    j12 = -np.cos(thetap)*np.sin(theta1+theta2)
    j20 = 0
    j21 = np.cos(theta1)+np.cos(theta1+theta2)
    j22 = np.cos(theta1+theta2)

    J = np.array([[j00, j01, j02],
                  [j10, j11, j12],
                  [j20, j21, j22]])
    return J


#
#  Main Code
#
#  This simply tests the above functions.
#
def main():
    # Run the test case.  Suppress infinitesimal numbers.
    np.set_printoptions(suppress=True)

    # First (given) test case with following joint coordinates.
    print("TEST CASE #1:")
    q1 = np.radians(np.array([20, 40, -30]))
    print('q:\n',       q1)
    print('fkin(q):\n', fkin(q1))
    print('Jac(q):\n',  Jac(q1))

    # Second test case with following joint coordinates.
    print("TEST CASE #2")
    q2 = np.radians(np.array([30, 20, 50]))
    print('q:\n',       q2)
    print('fkin(q):\n', fkin(q2))
    print('Jac(q):\n',  Jac(q2))

if __name__ == "__main__":
    main()
