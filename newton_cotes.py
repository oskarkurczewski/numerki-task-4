from numpy import e


def simpson(a, b, f, w):
    h = (b - a) / 2
    # integral = (e ** (- (a ** 2) * function(a)
    #                   + 4 * e ** (- ((a + b) / 2) ** 2) * function(((a + b) / 2))
    #                   + e ** - (b ** 2)) * function(b)) * h / 3
    integral = h / 3 * ((w(a) * f(a))
                      + 4 * (w(a + b / 2) * w(a + b / 2))
                      + (w(b) * f(b)))
    return integral


def advanced_simpson(left, right, function, weight, epsilon):
    integral = simpson(left, right, function, weight)
    isNotAccurate = True
    n = 2
    while isNotAccurate:
        new_integral = 0
        h = (right - left) / (2 * n)
        a = left
        b = a + 2 * h
        for i in range(n):
            i = simpson(a, b, function, weight)
            new_integral += i
            a = b
            b += 2 * h
        if abs(new_integral - integral) < epsilon:
            isNotAccurate = False
            integral = new_integral
        else:
            integral = new_integral
            n += 1
    return integral


def newton_cotes(function, weight, epsilon):
    a = 0
    delta = 1
    sum = 0
    isNotAccurate = True
    while isNotAccurate:
        integral = advanced_simpson(a, a + delta, function, weight, epsilon)
        sum += integral
        a += delta
        if abs(integral) <= abs(epsilon):
            isNotAccurate = False
    return sum
