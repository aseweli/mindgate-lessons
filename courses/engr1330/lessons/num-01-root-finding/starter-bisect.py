f = lambda x: x**3 - 2*x - 5
xl, xu = 2, 3
xm = (xl + xu) / 2
es, ea, i = 0.01, 100, 0

while ea > es:
    i = i + 1
    # TODO: if f(xl)*f(xm) > 0 move xl to xm, otherwise move xu to xm
    old = xm
    xm = (xl + xu) / 2
    ea = 0              # TODO: approximate relative error in percent
print("iterations:", i)
print("root:", round(xm, 6))
