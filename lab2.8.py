class ELine:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p


class EPoint:
    def __init__(self, point, line):
        self.x = point[0]
        self.y = point[1]
        self.line = line

    def __add__(self, o):
        if self.x is None or self.y is None:
            return o
        if o.x is None or o.y is None:
            return self

        if self != o:
            _lambda = (self.y - o.y) * pow((self.x - o.x), self.line.p - 2, self.line.p) % self.line.p
        else:
            _lambda = (3 * self.x ** 2 + self.line.a) * pow(2 * self.y, self.line.p - 2, self.line.p) % self.line.p

        x = (_lambda ** 2 - self.x - o.x) % self.line.p
        y = (_lambda * (self.x - x) - self.y) % self.line.p
        return EPoint((x, y), self.line)

    def __sub__(self, o):
        if self.x is None or self.y is None:
            return EPoint((o.x, -o.y), o.line)
        if o.x is None or o.y is None:
            return self
        return self + EPoint((o.x, -o.y), o.line)

    def __mul__(self, k):
        sum = EPoint((None, None), self.line)
        tmp = self
        while k > 0:
            if k % 2:
                sum += tmp
            k //= 2
            tmp += tmp
        return sum

    def __str__(self):
        return f'({self.x}, {self.y})'


eLine = ELine(-1, 1, 751)

P = EPoint((39, 171), eLine)

print(P * 108)
