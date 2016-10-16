__author__ = 'artyomd'
import numpy as np

def gradientDescent(x, y, theta, alpha, m):
    xTrans = x.transpose()
    z=0
    while z==0:
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        cost = float(np.sum(loss * loss) / (2 * m))
        gradient = np.dot(xTrans, loss) / m
        theta1 = theta - alpha * gradient
        theta = theta1 - alpha * gradient
        diff = theta-theta1
        if((diff==0).all()):
            z=1
    return theta
def func(a,b):
    i=0
    while i<len(a):
        a[i].insert(0,1)
        i+=1
    x = np.array(a)
    y=np.array(b)
    m, n = np.shape(x)
    alpha = 0.001
    theta = np.ones(n)
    theta = gradientDescent(x, y, theta, alpha, m)
    return theta
print func([[0, -1,7], [2, 3, 6]], [3, 1])