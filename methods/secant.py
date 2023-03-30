from methods.method import Method

class SecantMethod(Method):
    def __init__(self, nonlinear_equation):
        self.nonlinear_equation = nonlinear_equation

    def execute(self):
        return self.find_root()

    def find_root(self):
        print("> Please enter your initial guesses x0 and x1: ", end="")
        x0, x1 = map(float, input().split())
        print("> Please enter your epsilon: ", end="")
        self.EPS = float(input())

        for i in range(int(1e6)):
            fx0 = self.nonlinear_equation.f(x0)
            fx1 = self.nonlinear_equation.f(x1)
            x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
            if abs(x2 - x1) < self.EPS:
                return x2
            x0, x1 = x1, x2

        return "There is no solution!"