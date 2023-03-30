import random
from methods.method import Method

class FIXEDPOINTIterationMethod(Method):
    def __init__(self, nonlinear_equation):
        self.nonlinear_equation = nonlinear_equation

    def execute(self):
        return self.find_root()

    def find_root(self):
        a, b = map(float, input("> Please enter your interval [a, b]: ").split())
        eps = float(input("> Please enter your epsilon: "))
        x1 = random.uniform(a, b)
        prev_val = -1e9
        iter_count = 0

        while iter_count < int(1e6):
            iter_count += 1
            fx1 = self.nonlinear_equation.f(x1)

            if abs(fx1) < eps and abs(prev_val - x1) < eps:
                return x1

            if not a <= x1.real <= b:
                return "There is no solution!"

            x1 = self.nonlinear_equation.f_equiv(x1)
            prev_val = x1

        return "There is no solution!"