Sotropa Konstantinos-Rafael
import numpy
from matplotlib import pyplot
import math
def convex_function(x):
    return x**2 - 15*x + 2
def convex_function_derivative(x):
    return 2*x - 15


def gradient_descent(x, n):
    return x - n*convex_function_derivative(x)
def gradient_descent_sinus(x, n):
    return x - n*math.cos(x)

#x^2 - 40x + 60
if _name_ == "_main_":
    while True:
        print("Press 0 to close the program")
        print("Press 1 to show the convergence to the global minimum")
        print("Press 2 to show the convergence slightly faster")
        print("Press 3 to show that if n too large it can lead to divergence")
        print("Press 4 to show that if the function is non-convex it converges to a local minimum")
        n = int(input("Choose option: "))
        match n:
            case 0:
                break
            case 1:
                print("--------")
                x = numpy.linspace(-50, 100, 200)
                grad = [-40]
                grad_result = [convex_function(grad[-1])]
                for i in range(50):
                    grad.append(gradient_descent(grad[-1], 0.09))
                    grad_result.append(convex_function(grad[-1]))
                pyplot.plot(x, convex_function(x)) #x represents the values from the domain and convex_function(x) the values of f(x)
                pyplot.scatter(grad, grad_result, facecolors='none', color="red") #grad contains the values from the gradient descent
                pyplot.show()
            case 2:
                print("--------")
                x = numpy.linspace(-50, 100, 200)
                grad = [-40]
                grad_result = [convex_function(grad[-1])]
                for i in range(50):
                    grad.append(gradient_descent(grad[-1], 0.225))
                    grad_result.append(convex_function(grad[-1]))
                pyplot.plot(x, convex_function(x)) #x represents the values from the domain and convex_function(x) the values of f(x)
                pyplot.scatter(grad, grad_result,  color="red", facecolors="none")
                pyplot.show()
            case 3:
                print("--------")
                x = numpy.linspace(-1000, 1000, 5000)
                grad = [-2]
                grad_result = [convex_function(grad[-1])]
                for i in range(22):
                    grad.append(gradient_descent(grad[-1], 1.09)) #as n is greater than 1, the series will diverge
                    grad_result.append(convex_function(grad[-1]))
                print(grad)
                pyplot.plot(grad, grad_result, color="red")
                pyplot.plot(x, convex_function(x)) #x represents the values from the domain and convex_function(x) the values of f(x)
                pyplot.show()