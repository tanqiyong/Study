class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        a, b = 0, 1
        for i in range(item):
            a, b = b, a+b
        return a


for n in Fib():
    print(n, end=",")
s = Fib()
print(s)
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(callable(s))
